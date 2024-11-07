
def start():
    gamer_one()
    structure()

grille =["-","-","-"
        ,"-","-","-"
        ,"-","-","-"]

# Le joueur choisit son symbole
joueur_actuel = ""
end_game = False
gagnant = ""

def jouer():
    gamer_one()
    affichage_grille()
    while end_game == False :
        tour(gamer_one)
        verifier_fin_de_jeu(i)

def gamer_one():
    global gamer_one
    gamer_one = input("Please, choose (X) or (O) : ")
    while True:
        gamer_one = gamer_one.upper()
        if gamer_one == "X" :
            print("You choose X. Gamer two have O")
            break
        elif gamer_one == "O" :
            print("You choose O. Gamer two have X")
            break
        else:
            gamer_one = input("Please, choose (X) or (O) : ")

# Définir la grille de jeu
def structure():
    print("\n")
    print("---------------")
    print( " |" ,grille[0], "|" ,grille[1], "|" ,grille[2], "| " + "    1 | 2 | 3" )
    print("---------------")
    print( " |" ,grille[3], "|" ,grille[4], "|" ,grille[5], "| " + "    4 | 5 | 6" )
    print("---------------")
    print( " |" ,grille[6], "|" ,grille[7], "|" ,grille[8], "| " + "    7 | 8 | 9" )
    print("---------------")
    print("\n")


def turn(gamer) :
    print("It's turn of gamer : ", gamer)
    pos = input("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 : ")

    valide = False
    while valide == False :

        while pos not in ["1","2","3","4","5","6","7","8","9"] :
            pos = input("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 : ")
        pos = int(pos) - 1

        if grille[pos] == "-" :
            valide = True
        else :
            print("Vous ne pouvez pas accéder à cette postition")

    grille[pos] = gamer_one
    affichage_grille()

def verififer_victoire():
    global end_game
    global gagnant
    if grille[0] == grille[1] == grille[2] and grille[2] != "-" :
        end_game = True
        gagnant = grille[1]
    if grille[3] == grille[4] == grille[5] and grille[5] != "-" :
        end_game = True
        gagnant = grille[2]
    if grille[6] == grille[7] == grille[8] and grille[8] != "-" :
        end_game = True
        gagnant = grille[3]
    if grille[0] == grille[1] == grille[2] and grille[2] != "-" :
        end_game = True
        gagnant = grille[1]



start()










