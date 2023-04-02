from battleship_ import *

def test():

    def test_get_coordinates():
        bateaux = ['E4', 'A6', 'A3', 'D2', 'C5', 'E1']
        for cible in bateaux:
            print(cible, get_coordinates(cible, 6))
            assert(len(get_coordinates(cible,6))) == 2

    #test_get_coordinates()


    def test_dessiner():
        dessiner_rate(40)

    #test_dessiner()


    def test_prochaine_partie():
        dessins(16, 4)
        joueur = {"nom": "jj", "trouves":[[0, 0]], "rates":[[0,1], [1,1]], "points": 1}
        dessins(joueur, 16, 4)
        dessins(joueur, 16, 4)
        turtle.exitonclick()

    #test_prochaine_partie()


    def test_gagnant():
        joueurs = [{'nom': 'Joueur 1', 'bateaux': ['C5', 'D6', 'F5', 'C6', 'D4'], 'trouves': [], 'rates': [], 'points': 2},
                    {'nom': 'Joueur 2', 'bateaux': ['A2', 'A3', 'E3', 'D2', 'E6'], 'trouves': [], 'rates': [], 'points': 5}]
        
        gagnant(joueurs)
    #test_gagnant()

test()