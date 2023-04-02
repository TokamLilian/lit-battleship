###############################################################################
## {Simuler le jeu bataille navale}
###############################################################################
## Auteur: {Ange Lilian Tchomtchoua Tokam}
## Date: {31 Mars}
## Email: {tokamlilian@gmail.com}
###############################################################################

import turtle
from turtle import * 
import math  
import random        

lettres_collones = ['A', 'B', 'C', 'D', 'E', 'F']                           #la liste de toutes les lettres qui représentent les colonnes

def arc(r, angle):
#Cette fonction permet de tracer un arc de cercle

    longueur_arc = 2 * math.pi * r * angle / 360
    n = int(longueur_arc / 3) + 1
    longueur_etape = longueur_arc / n
    angle_etape = float(angle) / n

    for _ in range(n):
        fd(longueur_etape)
        lt(angle_etape)


def cercle(r):
#Cette fonction permet de dessiner un cercle rouge qui représente un bateau

    turtle.color("red")
    arc(r, 360)
    turtle.color("black")


def carre(cote):
#cette fonction permet de dessiner un carré
    
    for _ in range(4):
        fd(cote); lt(90)


def positionner(x, y):
#Cette fonction permet de positionner la tortue relativement à son emplacement actuel
    
    pu(); fd(x); lt(90); fd(y); rt(90); pd()


def creer_joueur(nom):
    """cette fonction creait les jouers avec les differents attributs
    Args:
        bateaux     est la lettre ainsi que le nombre correspondant au bateau du joueur
        trouves     contient tous les bateaux touchés par l'adversaire 
        rates       contient tous les propositions ratés par l'adversaire
        points      est le nombre de points accumulés dans la partie
    """
    return {
        "nom": nom,
        "bateaux": [],
        "trouves": [],
        "rates": [],
        "points": 0
    }


def shuffle(joueur, cols):                                       
#cette fonction écrit les positions aléatoires des bateaux d'un joueur

    while len(joueur["bateaux"]) < cols-1:                                        #chaque joueur a 5 bateaux
        ligne = int(cols*random.random()) + 1                                     #la position aleatoire d'un bateau
        colonne = int(cols*random.random())
        position = lettres_collones[colonne] + str(ligne)

        if position not in joueur["bateaux"]:                                     #on veut s'assurer que tous les bateaux sont distincts
            joueur["bateaux"].append(position)


def gagnant (joueurs):
#cette fontion retourne le meilleur joueur et son nombre de points
        
        meilleur_joueur = joueurs[0]                                              #le meilleur joueur est le joueur 1 par défaut
        point_max = meilleur_joueur["points"]

        for i in range (len(joueurs)):                                            #on parcoure les points de différents joueurs et
            joueur = joueurs[i]                                                   #si on trouve un joueur qui a plus de point, alors
            point = joueur["points"]                                              #il est le meilleur joeur
            if point > point_max:
                point_max = point
                meilleur_joueur = joueurs[i]["nom"]

        meilleur = [meilleur_joueur, point_max]
        return meilleur


def get_coordinates(cible ,cols):
#cette fontion retourne les coordonées d'une cible proposé

    letter = cible[0]
    number = int(cible[1]) - 1

    colonne = 0

    if letter not in lettres_collones or number > 5 or number < 0:                #on veut s'assurer que les entrées de l'utilisateur correspondent 
        return                                                                    #aux cases du jeux, sinon on retoune demander une nouvelle entrée

    for letters in lettres_collones:                                              #on parcourure les lettres des colonnes pour identifier la position
                                                                                  #de la la lettre dès qu'on la trouve
        if letter == letters: break                             

        else: colonne += 1                                                        #on passe à la prochaine colonne si on a pas encore trouvé la lettre

    ligne = 0                                                                     #la grille étant déssinée de bas vers le haut, on veut avoir la ligne
                                                                                  #qui correspond à la case relativement à la grille 
    for pas in range(1, cols):        

        if number == (cols - pas):  break                                         #on remonte d'une ligne si on n'est pas à au numero de l'entrée

        else:   ligne += 1

    coordinate = [ligne, colonne]                                                 #les coordonnées le la cible sur la grille déssinée par la tortue

    return coordinate


def dessiner_rate(taille):
#cette fonction dessine une case ratée représentée par un carré vert avec une croix à l'intérieure

    turtle.color("green")
    turtle.pensize(2)
    carre(taille)

    hypothenus = taille*math.sqrt(2)
    lt(45);fd(hypothenus);pu();lt(135);fd(taille);pd();lt(135);fd(hypothenus);lt(45)
    fd(-taille)
    turtle.color("black")
    turtle.pensize(1)


def grille (joueur, cols, lignes, taille, espace):
#Cette fonction permet de tracer une grille.

    for x in range(cols):
        for y in range(lignes):
            coordinate = [y, x]


            if coordinate in joueur["rates"]:                                     #pour dessiner toutes les cases ratées
                positionner(x * (taille + espace), y * (taille + espace))  
                dessiner_rate(taille)
                positionner(-(x * (taille + espace)), -y * (taille + espace))

            elif coordinate in joueur["trouves"]:                                 #pour dessiner toutes les cases trouvées
                positionner(x * (taille + espace) + taille/2, y * (taille + espace))
                cercle(taille/2)
                positionner(-x * (taille + espace) - taille/2, -y * (taille + espace))

            else:                                                                 #pour dessiner toutes les autres cases
                positionner(x * (taille + espace), y * (taille + espace))
                carre(taille)
                positionner(-x * (taille + espace), -y * (taille + espace))


def dessiner_ligne(hauteur, largueur):
#cette fonction dessine une ligne séparatrice entre les deux grilles du jeux

    size = [largueur, hauteur]

    turtle.color("blue")
    turtle.begin_fill()

    for _ in range (2):
        for move in size:
            fd(move)
            lt(90)

    turtle.end_fill()
    turtle.color("black")

    
def dessins(joueurs, taille, espace, cols, lignes, largueur, distance):
#cette fonction fait appel aux dessins des grilles du jeux ainsi que la ligne entre elles

    hauteur = lignes * taille + 2*espace*(lignes-1)                         #la hauteur de la ligne separatrice
    
    step = (cols * taille) + ((cols - 1) * espace) + distance               #le pas pour aller à la dernière case

    for i in range(len(joueurs)):
        joueur = joueurs[i]
        grille(joueur, cols, lignes, taille, espace)

        if i == 0:                                                          #on ne dessine la ligne que après la première
            pu()                                                            #grille pour ce jeux
            positionner(step, 0)
            pd()
            dessiner_ligne(hauteur, largueur)
            pu(); fd(largueur + distance); pd()


def jouer():
#cette fonction est la fonction principale du jeux qui initialise la partie et procède à l'appel d'autres fontions

    nombre_joueurs = 2
    joueurs = []                                            #la liste des joueurs du jeux
    cols = 6
    lignes = 6

    distance = 20                                           #la distance entre la ligne bleu et une grille
    largueur = 10                                           #la largueur de la ligne séparatrice

    taille = 16                                             #la taille d'un carré
    espace = 4                                              #l'espace entre deux carrés

    cont = True                                             #la decision de continuer le jeux ou pas

    for i in range(nombre_joueurs):                          #on creait les joueurs du jexu avec leurs bateaux
        joueurs.append(creer_joueur(f"Joueur {i + 1}"))

        shuffle(joueurs[i], cols)

    #turtle.shape("arrow")                                   #si on veut changer le type de figure de la tortue
    #turtle.hideturtle()                                     #si on decide de cacher la tortue
    dessins(joueurs, taille, espace, cols, lignes, largueur, distance)

    while cont:

        for joueur in range(nombre_joueurs): 

            if joueur == 1: 
                autre = 0
                pu(); goto(0,0); pd()                        #on positionne la tortue à au début de la grille de l'adversaire 

            else: 
                autre = 1
                #on calcul le nombre de pas pour aller aux pieds de la grille du joueur adverse
                steps = (taille * cols) + (cols-1)*espace + largueur + 2*distance
                pu(); goto (steps, 0); pd() 

            print(joueurs[joueur]["nom"])

            while True:
                proposition = input('Visez un bateau adverse: ')
                proposition = proposition.upper().strip()

                cible = get_coordinates(proposition, cols)                  #si un joueur entre une cible non valid, le programme lui demandera
                if cible != None: break                                     #d'entrer une cible à nouveau

            if cible in joueurs[autre]["trouves"]:
                print('Vous avez déjà touché ce bateau'); print("")
            
            elif proposition in joueurs[autre]["bateaux"]:                  #si la cible proposée est parmi les bateaux de l'autre joueur

                print("Touché!"); print("")
                joueurs[autre]["trouves"].append(cible)                     #les bateaux touchés par l'adversaire
                joueurs[joueur]["points"] += 1                              #on donne les points du joueur actuel                                           

            else:
                joueurs[autre]["rates"].append(cible)
                print('Raté!'); print("")

            pu()
            goto(0,0)
            turtle.clear()
            dessins(joueurs, taille, espace,cols, lignes, largueur, distance)          #on redessine la grille avec les cases touchées et/ou ratées

            nombre_touches_0 = joueurs[0]["trouves"]
            nombre_touches_1 = joueurs[1]["trouves"]

            if len(nombre_touches_0) == 5 or len(nombre_touches_1) == 5:                #si un joueur a trouvé tous les bateaux de l'autre, on s'arrete
                cont = False
                break

    meilleur = gagnant(joueurs)
    meilleur_jouer = meilleur[0]
    meilleur_point = meilleur[1]

    print('Le meilleur joueur est',meilleur_jouer,'avec',meilleur_point,'points'); print("")

    print('Clickez sur une grille pour terminer')
    turtle.exitonclick()


jouer()