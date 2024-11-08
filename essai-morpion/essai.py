
 
grille = ["  ", "  ", "  ",
         "  ", "  ", "  ",
         "  ", "  ", "  "]


joueur_actuel = " "

def joueur():
    choix_joueur()
    affichage_grille()

def choix_joueur():
    global joueur_actuel
    joueur_actuel = input("veuilez choisir soit une croix (x), soit un rond (O) : ")
    while True: 
        joueur_actuel = joueur_actuel.upper()
        if joueur_actuel == 'X' :
            print("vous avez choisi (X), le joueur suivant aura (O)")
            break
        elif joueur_actuel == 'O' : 
            print("vous avez choisi (O), le joueur suivant aura (X)")
            break
        else : 
            joueur_actuel = input("veuillez choisir soit une croix (X), soit un rond (O) :")
choix_joueur()



"""
def choix_case():
    global joueur_actuel
    choix_case = input("veuillez choisir une case vide entre 0 et 8 : ")
    ligne = [0, 1, 2,]
    colonne = [0, 1, 2]
    while True :
        if ligne in range(3) :
            if choix_case == ligne : 
                print("votre choix est validé")
                break
            elif choix_case == colonne : 
                print("choix validé")
                break
            else : 
                choix_case = input("case déjà prise")
choix_case()



"""



def choix_case(grille, joueur_actuel):
   while True :
    joueur_actuel = "X"
    case = int(input("choississez une case vide entre 0 et 8 : "))
    if case < 0 or case > 8:
        print("veuillez entrer un nombre entre 0 et 8 :")
    if grille[case] == " " :
        grille[case] = joueur_actuel
        #print("cette case est déjà prise, choisissez une autre case :")
    else :
        print("cette case est déjà prise, choisissez une autre case :")
    choix_case(grille, joueur_actuel)

#choix_case(grille,joueur_actuel)

def affichage_grille():   
    #print("\n"): retour à la ligne
    print("\n")
    print("----------------")
    print("|", grille[0], "|", grille[1], "|", grille[2], "|")
    print("+----+----+----+")
    print("|", grille[0], "|", grille[1], "|", grille[2], "|") 
    print("+----+----+----+")
    print("|", grille[0], "|", grille[1], "|", grille[2], "|")
    print("----------------")

affichage_grille()

choix_case(grille,joueur_actuel)

"""
def victoire():

    if grille[0] ==  grille[1] == grille[2] == joueur_actuel  or \
       grille[3] == grille[4] == grille[5]  == joueur_actuel or \
       grille[6] == grille[7] == grille[8]  == joueur_actuel :
       print("victoire horizentale de : {joueur_actuel}" )
       
    elif grille[0] ==  grille[3] == grille[6] == joueur_actuel  or \
        grille[1] == grille[4] == grille[7] == joueur_actuel or \
        grille[2] == grille[5] == grille[8] == joueur_actuel :

        print("victoire verticale de {joueur_actuel}") 


    elif grille[0] == grille[4] == grille[8] == joueur_actuel :
        print("victoire diagonale de {joueur_actuel}")

    elif grille[2] == grille[4] == grille[6] == joueur_actuel : 
        print("victoire diagonal inversée de {joueur_actuel}")
    else:
        print("retante ta chance")
victoire()
"""
