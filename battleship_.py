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

lettres_collones = ['A', 'B', 'C', 'D', 'E', 'F']

def arc(r, angle):
#Cette fonction permet de tracer un arc de cercle

    #r (int): Rayon de l'arc
    #angle (int): Angle de l'arc

    longueur_arc = 2 * math.pi * r * angle / 360
    n = int(longueur_arc / 3) + 1
    longueur_etape = longueur_arc / n
    angle_etape = float(angle) / n

    for _ in range(n):
        fd(longueur_etape)
        lt(angle_etape)


def cercle(r):
#Cette fonction permet de dessiner un cercle

    turtle.color("red")
    arc(r, 360)
    turtle.color("black")


def carre(cote):
#cette fonction permet de dessiner un carré

#cote (int): Longueur d'un coté
    
    for _ in range(4):
        fd(cote); lt(90)


def positionner(x, y):
#Cette fonction permet de positionner la tortue relativement à son emplacement actuel

    #x (int): Nombre de pas en x
    #y (int): Nombre de pas en y
    
    pu(); fd(x); lt(90); fd(y); rt(90); pd()


def creer_joueur(nom):
    """cette fonction creais les jouers avec les differents attributs
    Args:
        bateaux     est la lettre ainsi que le nombre correspondant au bateau du joueur
        trouves     contient tous les bateaux adverses touchés
        rates       contient tous les propositions ratés de ce joueur
        points      est le nombre de points accumulés dans la partie
    """
    return {
        "nom": nom,
        "bateaux": [],
        "trouves": [],
        "rates": [],
        "points": 0
    }


def shuffle(joueurs):                                       
#cette fonction écrit les positions aléatoires des bateaux d'un joueur

    for _ in range (5):                                         #chaque joueur a 5 bateaux
        ligne = int(6*random.random()) + 1                      #la position aleatoire d'un bateau
        colonne = int(6*random.random())
        position = lettres_collones[colonne] + str(ligne)
        joueurs["bateaux"].append(position)


def gagnant (joueurs):
        
        meilleur_joueur = joueurs[0]
        point_max = meilleur_joueur["points"]

        for i in range (len(joueurs)):
            joueur = joueurs[i]
            point = joueur["points"]
            if point > point_max:
                point_max = point
                meilleur_joueur = joueurs[i]["nom"]

        meilleur = [meilleur_joueur["nom"], point_max]
        return meilleur


def get_coordinates(cible):                     #cette fontion retourne les coordonées d'une cible proposé
    letter = cible[0];letter.capitalize()
    number = int(cible[1])
    position = 0

    for letters in lettres_collones:
        if letter == letters:
            column = position
            break
        else:
            position += 1

    line = number - 1
    coordinate = [line, column]

    return(coordinate)


def prochaine_partie_rate(joueur, taille, espace, cols):                 #cette fontion dessine les cases ratées

    for rate in joueur["rates"]:                   #pour toutes les coordonnées des propositions ratés
    #on veut aller à la grille correspondante et dessiner un raté

        ligne_i = rate[0]
        colonne_i = rate[1]

        ligne_x = 0
        d = 1
        while True:
            if ligne_i == (cols - d):
                break
            else:
                d += 1
                ligne_x += 1

        positionner(colonne_i * (taille + espace), ligne_x * (taille + espace))
        dessiner_rate(taille)
        positionner(-(colonne_i  * (taille + espace) + taille), -ligne_x * (taille + espace))


def prochaine_partie_touche(joueur, taille, espace, cols):                 #cette fontion dessine les cases touchées

    for touch in joueur["trouves"]:                #pour toutes les coordonnées des cibles touchés
    #on veut aller à la grille correspondante et dessiner un bateau
        
        ligne_i = touch[0]
        colonne_i = touch[1]

        colonne_x = colonne_i - 1
        ligne_x = 0
        d = 1
        while True:
            if ligne_i == (cols - d):
                break
            else:
                d += 1
                ligne_x += 1

        positionner(colonne_i * (taille + espace) + taille/2, ligne_x * (taille + espace))          #on va au milieu du carré pour pouvoir dessiner le cercle
        cercle(8)                                                                                   #dessiner un cercle de rayon 8
        positionner(-colonne_i * (taille + espace) - taille/2, -ligne_x * (taille + espace))        #on va au milieu du carré pour pouvoir dessiner le cercle


def dessiner_rate(taille):
    turtle.color("green")
    turtle.pensize(2)
    carre(taille)

    hypothenus = taille*math.sqrt(2)
    lt(45);fd(hypothenus);pu();lt(135);fd(taille);pd();lt(135);fd(hypothenus);lt(45)
    turtle.color("black")


def grille (cols, lignes, taille, espace):
#Cette fonction permet de tracer une grille.

    for x in range(cols):
        for y in range(lignes):
            positionner(x * (taille + espace), y * (taille + espace))
            carre(taille)
            positionner(-x * (taille + espace), -y * (taille + espace))


def dessiner_ligne(hauteur, largueur):
    size = [largueur, hauteur]

    turtle.color("blue")
 
    turtle.begin_fill()
    for _ in range (2):
        for move in size:
            fd(move)
            lt(90)

    turtle.end_fill()
    turtle.color("black")

    
def dessins(taille, espace, cols, lignes, largueur, distance):


    hauteur = (lignes * taille) + ((lignes - 1) * espace)               #la hauteur de la ligne separatrice
    
    
    step = (cols * taille) + ((cols - 1) * espace) + distance           #le pas pour aller à la dernière case
    
    grille(cols, lignes, taille, espace)

    positionner(step, 0)

    dessiner_ligne(hauteur, largueur)

    pu(); fd(largueur + distance)

    grille(cols, lignes, taille, espace)



def jouer():
    nombre_joueurs = 2
    joueurs = []
    cols = 6
    lignes = 6

    distance = 20               #la distance entre la ligne bleu et une grille
    largueur = 10

    taille = 16                 #la taille d'un carré
    espace = 4                  #l'espace entre deux carrés

    for i in range(nombre_joueurs):                          #on creait les joueurs du jexu avec leurs bateaux
        joueurs.append(creer_joueur(f"Joueur {i + 1}"))

        shuffle(joueurs[i])
        print(joueurs[i]) ##

    dessins(taille, espace, cols, lignes, largueur, distance)

    for chanches in range(3):                                #chaque joueurs à droit à 7 chances
        for joueur in range(nombre_joueurs): 

            if joueur == 1: 
                autre = 0
                pu(); goto(0,0); pd()  

            else: 
                autre = 1
                steps = (taille * cols) + (cols-1)*espace + largueur + 2*distance
                pu(); goto (steps, 0); pd() 

            print('Joueur',joueur+1)

            proposition = input('Visez un bateau adverse: ')
            cible = get_coordinates(proposition)

            if cible in joueurs[joueur]["trouves"]:
                print('Vous avez déjà touché ce bateau'); print("")
            
            elif proposition in joueurs[autre]["bateaux"]:              #si la cible proposé est parmi les bateaux de l'autre joueur

                print("Touché!"); print("")
                joueurs[joueur]["trouves"].append(cible)        #les bateaux adverse touchés
                joueurs[joueur]["points"] += 1                  #on donne les points du joeuur actuel

                prochaine_partie_touche(joueurs[joueur], taille, espace, cols) 

            else:
                joueurs[joueur]["rates"].append(cible)
                print('Raté'); print("")
                prochaine_partie_rate(joueurs[joueur], taille, espace, cols)

    meilleur = gagnant(joueurs)
    meilleur_jouer = meilleur[0]
    meilleur_point = meilleur[1]

    print('Le meilleur joueur est',meilleur_jouer,'avec',meilleur_point,'points')

    print('Clickez n\'importe où pour teminer')
    turtle.exitonclick()


jouer()