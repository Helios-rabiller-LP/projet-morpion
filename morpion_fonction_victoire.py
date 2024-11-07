grille= ['1','2','3',
         '4','5','6',
         '7','8','9']
joueur_actif= ""
jeu_fini = False
gagnant = ""

# la fonction permet de choisir quel joueur on veut être entre "X" et "O"
# joueur_actif = le joueur actuelle aprés input
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

# On construit la structure du morpion et on implémente une variable grille qui a pour valeur une liste          
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

# la fonction qui permet de vérifier si on a un gagnant ou une égalité ou bien si on conclut qu'il n'y a pas de gagnant ni d'égalité
# les conditions de victoire son déterminer par les 8 façons de gagner dans le morpion les 3 colonnes les 3 lignes et les 2 diagonales
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
    elif all(cell in ['X', 'O'] for cell in grille):
        jeu_fini = True
    else:
        jeu_fini= False

def tour(joueur):
    print("tour du Joueur "+ joueur)
    coup = input("Sélectionner un nombre de 1 a 9 dans la grille pour placer votre pion :")
    check = False
    while check == False :
    
      while coup not in['1','2','3','4','5','6','7','8','9']:
        coup = input("Sélectionner un nombre de 1 a 9 dans la grille pour placer votre pion :")
      coup = int(coup) - 1

      if grille[coup] == "1" or grille[coup] == "2" or grille[coup] == "3" or grille[coup] == "4" or grille[coup] == "5" or grille[coup] == "6" or grille[coup] == "7" or grille[coup] == "8" or grille[coup] =="9" :
          check = True
      else :
          print("vous ne pouvez pas vous placez ici !")
    grille[coup] = (joueur)
    the_grid()
    



def jouer():
    rotation_joueur()
    the_grid()
    while jeu_fini == False :
        tour(joueur_actif)
        victoire()
        if joueur_actif == "X":
            joueur_actif = "O"
        else:
            joueur_actif = "X"
    if gagnant == "X" or gagnant == "O":
        print("Le vainqueur est le Joueur ", gagnant)
    else :
        print("Match Nul!")
jouer()
