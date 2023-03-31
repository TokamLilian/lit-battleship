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

#r (int): Longueur du rayon
    arc(r, 360)


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
    return {
        "nom": nom,
        "bateaux": [],
        "trouves": [],
        "points": 0
    }


def shuffle(joueurs):                                       
#cette fonction écrit les positions aléatoires des bateaux d'un joueur

    for _ in range (5):                                         #chaque joueur a 5 bateaux
        lettres_collones = ['A', 'B', 'C', 'D', 'E', 'F']
        ligne = int(6*random.random()) + 1                      #la position aleatoire d'un bateau
        colonne = int(6*random.random())
        position = lettres_collones[colonne] + str(ligne)
        joueurs["bateaux"].append(position)


def gagnant (joueurs):
        
    #for i in range (len(joueurs)):
        meilleur_joueur = joueurs[0]
        point_max = meilleur_joueur["points"]

        for i in range (len(joueurs)):
            joueur = joueurs[i]
            point = joueur["points"]
            if point > point_max:
                point_max = point
                meilleur_joueur = joueurs[i]["nom"]

        meilleur = [meilleur_joueur, point_max]
        return meilleur


def grille (cols, lignes, taille, espace):
#Cette fonction permet de tracer une grille.

#cols (int): Nombre de colonnes
#lignes (int): Nombre de lignes
#taille (int): Taille d'une case
#espace (int): Taille de l'espace entre chaque case

    for x in range(cols):
        for y in range(lignes):
            positionner(x * (taille + espace), y * (taille + espace))
            carre(taille)
            positionner(-x * (taille + espace), -y * (taille + espace))


def dessiner_ligne(hauteur, largueur):
    size = [largueur, hauteur]
    line = turtle.Turtle()
    line.color("blue")
    #line.pensize(1)
    line.begin_fill()
    for _ in range (2):
        for move in size:
            line.fd(move)
            line.lt(90)

    line.end_fill()

    turtle.exitonclick()
    

def dessins():
    cols = 2
    lignes = 2
    taille = 16
    espace = 4
    distance = 20      #la distance entre la ligne bleu et une grille

    hauteur = (lignes * taille) + ((lignes - 1) * espace)   #la hauteur de la ligne separatrice
    largueur = 10
    
    step = (cols * taille) + ((cols - 1) * espace)          #le pas pour aller à la dernière case
    
    grille(cols, lignes, taille, espace)

    #pu(); fd(step + distance)
    positionner(step, 0)

    dessiner_ligne(hauteur, largueur)


def jouer():
    nombre_joueurs = 2
    joueurs = []

    for i in range(nombre_joueurs):                          #on creait les joueurs du jexu avec leurs bateaux
        joueurs.append(creer_joueur(f"Joueur {i + 1}"))

        shuffle(joueurs[i])
        print(joueurs[i]) ##

    #dessins()

    for chanches in range(2):                                #chaque joueurs à droit à 7 chances
        for joueur in range(nombre_joueurs):
        
            if joueur == 0: autre = 1
            if joueur == 1: autre = 0

            print('Jouer',joueur+1)

            cible = input('Visez un bateau adverse: ')

            if cible in joueurs[joueur]["trouves"]:
                print('Vous avex déjà touché ce bateau'); print("")
            
            elif cible in joueurs[autre]["bateaux"]:              #si la cible proposé est parmi les bateaux de l'autre joueur

                print("Touché!"); print("")
                joueurs[joueur]["trouves"].append(cible)        #les bateaux adverse touchés
                joueurs[joueur]["points"] += 1                  #on donne les points du joeuur actuel

            else:
                print('Raté'); print("")

    meilleur = gagnant(joueurs)
    meilleur_jouer = meilleur[0]
    meilleur_point = meilleur[1]

    print('Le meilleur joueur est',meilleur_jouer,'avec',meilleur_point,'points')

    #turtle.exitonclick()


jouer()