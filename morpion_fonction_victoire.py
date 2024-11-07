grille= ['1','2','3',
         '4','5','6',
         '7','8','9']
joueur_actif= ""
jeu_fini = False
gagnant = ""
def rotation_joueur():
    global joueur_actif
    joueur_actif= input("Quel joueur voulez vous être X ou O ? : ")
    while True:
        joueur_actif =joueur_actif.upper() # on passe tous str en majuscule
        if joueur_actif == "X":
            print("vous êtes le Joueur X le Joueur 2 sera O")
            break
        elif joueur_actif == "O":
            print("Vous êtes le Joueur O le Joueur 2 sera X")
            break
        else:
            joueur_actif= input("Quel joueur voulez vous être X ou O ? : ")
            
def the_grid():
    print("\n")
    print("|-------|-------|-------|")
    print(f"|   {grille[0]}   |   {grille[1]}   |   {grille[2]}   |")
    print("|-------|-------|-------|")
    print(f"|   {grille[3]}   |   {grille[4]}   |   {grille[5]}   |")
    print("|-------|-------|-------|")
    print(f"|   {grille[6]}   |   {grille[7]}   |   {grille[8]}   |")
    print("|-------|-------|-------|")
    print("\n")


def victoire():
    global jeu_fini
    global gagnant
    if grille[0] == grille[1] == grille[2]:
        jeu_fini = True
        gagnant = grille[2]
    elif grille[3] == grille[4] == grille[5]:
        jeu_fini = True
        gagnant = grille[5]
    elif grille[6] == grille[7] == grille[8]:
        jeu_fini = True
        gagnant = grille[8]
    elif grille[0] == grille[3] == grille[6]:
        jeu_fini = True
        gagnant = grille[6]
    elif grille[1] == grille[4] == grille[7]:
        jeu_fini = True
        gagnant = grille[7]
    elif grille[2] == grille[5] == grille[8]:
        jeu_fini = True
        gagnant = grille[8]
    elif grille[0] == grille[4] == grille[8]:
        jeu_fini = True
        gagnant = grille[8]
    elif grille[2] == grille[4] == grille[6]:
        jeu_fini = True
        gagnant = grille[6]
    elif "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" not in grille:
        jeu_fini = True
    else:
        jeu_fini= False
def jouer():
    rotation_joueur()
    the_grid()
jouer()
