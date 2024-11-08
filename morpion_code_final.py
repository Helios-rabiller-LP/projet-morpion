Grid= ['1','2','3',
         '4','5','6',
         '7','8','9']
active_player= ""
end_game = False
winner = ""

# la fonction permet de choisir quel joueur on veut être entre "X" et "O"
# active_player = le joueur actuelle aprés input
def player_choice():
    global active_player
    active_player= input("Quel joueur voulez vous être X ou O ? : ")
    while True:
        active_player =active_player.upper() # on passe tous str en majuscule
        if active_player == "X":
            print("vous êtes le Joueur X le Joueur 2 sera O")
            break
        elif active_player == "O":
            print("Vous êtes le Joueur O le Joueur 2 sera X")
            break
        else:
            active_player= input("Quel joueur voulez vous être X ou O ? : ")
 

# On construit la structure du morpion et on implémente une variable Grid qui a pour valeur une liste          
def the_grid():
    print("\n")
    print("|-------|-------|-------|")
    print(f"|   {Grid[0]}   |   {Grid[1]}   |   {Grid[2]}   |")
    print("|-------|-------|-------|")
    print(f"|   {Grid[3]}   |   {Grid[4]}   |   {Grid[5]}   |")
    print("|-------|-------|-------|")
    print(f"|   {Grid[6]}   |   {Grid[7]}   |   {Grid[8]}   |")
    print("|-------|-------|-------|")
    print("\n")

# la fonction qui permet de vérifier si on a un winner ou une égalité ou bien si on conclut qu'il n'y a pas de winner ni d'égalité
# les conditions de victoire son déterminer par les 8 façons de gagner dans le morpion les 3 colonnes les 3 lignes et les 2 diagonales
def victory():
    global end_game
    global winner
    if Grid[0] == Grid[1] == Grid[2]:
        end_game = True
        winner = Grid[2]
    elif Grid[3] == Grid[4] == Grid[5]:
        end_game = True
        winner = Grid[5]
    elif Grid[6] == Grid[7] == Grid[8]:
        end_game = True
        winner = Grid[8]
    elif Grid[0] == Grid[3] == Grid[6]:
        end_game = True
        winner = Grid[6]
    elif Grid[1] == Grid[4] == Grid[7]:
        end_game = True
        winner = Grid[7]
    elif Grid[2] == Grid[5] == Grid[8]:
        end_game = True
        winner = Grid[8]
    elif Grid[0] == Grid[4] == Grid[8]:
        end_game = True
        winner = Grid[8]
    elif Grid[2] == Grid[4] == Grid[6]:
        end_game = True
        winner = Grid[6]
    elif all(case in ['X', 'O'] for case in Grid):
        end_game = True
    else:
        end_game= False

# Ici on défini
def tour(joueur):
    global active_player
    print("tour du Joueur "+ joueur)
    coup = input("Sélectionner un nombre de 1 a 9 dans la Grid pour placer votre pion :")
    check = False
    while check == False :
    
      while coup not in['1','2','3','4','5','6','7','8','9']:
        coup = input("Sélectionner un nombre de 1 a 9 dans la Grid pour placer votre pion :")
      coup = int(coup) - 1

      if Grid[coup] == "1" or Grid[coup] == "2" or Grid[coup] == "3" or Grid[coup] == "4" or Grid[coup] == "5" or Grid[coup] == "6" or Grid[coup] == "7" or Grid[coup] == "8" or Grid[coup] =="9" :
          check = True
      else :
          print("vous ne pouvez pas vous placez ici !")
    Grid[coup] = (joueur)
    the_grid()
    

def resultat():
    if winner == "X" or winner == "O":
        print("Le vainqueur est le Joueur ", winner)
    else :
        print("Match Nul!")

def play():
    player_choice()
    the_grid()
    global active_player
    while end_game == False :
        tour(active_player)
        victory()
        if active_player == "X":
            active_player = "O"
        else:
            active_player = "X"
    resultat()
    #replay()






def replay():
    global active_player
    global end_game
    global winner
    global Grid
    choix = input("Voulez vous jouez au morpion ? oui/non : ")
    choix = choix.upper()
    while True:
        if choix == "OUI":
            
            winner = ""
            play()
            choix = input("voulez vous rejouer ?")
            choix = choix.upper()
        elif choix == "NON":
            print("passez une bonne journée!")
            break
        else:
            choix = input("je ne comprends que oui/non : ")
            choix = choix.upper()

replay()

