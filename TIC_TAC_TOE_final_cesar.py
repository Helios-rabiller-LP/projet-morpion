
# variables globales du jeu:
joueur_actuel= ""
grille = ["¤","¤","¤","¤","¤","¤","¤","¤","¤"]
fin_jeu = False 
gagnant = ""
joueur = joueur_actuel

#fonctions du jeu a appeler en debut de programme:
def jouer():
    choix_joueur()          #1
    affichage_grille()      #2
    
    # et conditions principales du jeu (en boucle) pendant le jeu (programme):
    while fin_jeu == False :
        tour(joueur_actuel) #3
        verifier_fin_jeu()  #4
        joueur_suivant()    #5
        if fin_jeu == False:
            return tour(joueur_actuel)
    
    resultat()              #6
    
# 1) fonction definir les joueurs:
def choix_joueur():
    global joueur_actuel #appel le joueur actuel dans les differentes fonctions du jeu
    joueur_actuel = input("Veuillez taper X ou O svp: ")
    while True: 
        joueur_actuel= joueur_actuel.upper() # met x ou o en Majuscule
        if joueur_actuel == "X":
            print("vous avez choisis X, le joueur 2 aura O.") 
            break
        elif joueur_actuel == "O":
            print("vous avez choisis O, le joueur 2 aura X.")  
            break
        else:
            joueur_actuel = input("Veuillez taper X ou O svp: ")
 
# 2) fonction definir l'affichage
def affichage_grille():
   
    print("*************")                                                              
    print("{", grille[0], "|", grille[1],"|", grille[2],"}     <---- 1|2|3")
    print("----+---+----")
    print("{", grille[3], "|", grille[4],"|", grille[5],"}     <---- 4|5|6")
    print("----+---+----")
    print("{", grille[6], "|", grille[7],"|", grille[8],"}     <---- 7|8|9")
    print("*************")
   
#3) definition des tours de jeu:
def tour(joueur): 
    print("Joueur ----", joueur,"---- à vous de jouer." )
    pos = input("veuillez sélectionner un chiffre entre 1 et 9: ")
    
    pos_valide = False
    while pos_valide == False:
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos = input("veuillez selectionner un espace vide: ")
        pos = int(pos) -1  # transformation chaine de caractere en entier pour verif 
        
        #finir la verification:
        if grille[pos] == "¤": # si "position disponible"
            pos_valide = True 
        else:
            print("Position non disponible ! Gamberge !")
    
    grille[pos] = joueur
    affichage_grille()

# fonctions de verifications a appeler avant victoire:
def verifier_fin_jeu():
    verifier_victoire()
    verif_match_nul()
    


# verification de victoire: 
def verifier_victoire():
    global fin_jeu
    global gagnant
    
    #victoire sur lignes:
    if grille[0]== grille[1]== grille[2] and grille[2] != "¤" :
        fin_jeu= True
        gagnant= grille[1]
        
    if grille[3]== grille[4]== grille[5] and grille[5] != "¤" :
        fin_jeu= True
        gagnant= grille[2] 
           
    if grille[6]== grille[7]== grille[8] and grille[8] != "¤" :
        fin_jeu= True
        gagnant= grille[8]
    
    #victoire sur colonnes: 
    if grille[0]== grille[3]== grille[6] and grille[6] != "¤" :
        fin_jeu= True
        gagnant= grille[6]
    if grille[1]== grille[4]== grille[7] and grille[7] != "¤" :
        fin_jeu= True
        gagnant= grille[7]
    if grille[2]== grille[5]== grille[8] and grille[8] != "¤" :
        fin_jeu= True
        gagnant= grille[8]    
    
    #victoire sur diagonales :
    if grille[0]== grille[4]== grille[8] and grille[8] != "¤" :
        fin_jeu= True
        gagnant= grille[8]
    if grille[2]== grille[4]== grille[6] and grille[6] != "¤" :
        fin_jeu= True
        gagnant= grille[6]    
 
#verif de match nul:        
def verif_match_nul():
    global fin_jeu #on va modifier cette valeur
    if "¤" not in grille:
        fin_jeu= True

#definir joeur suivant:
def joueur_suivant():
    global joueur_actuel
    if joueur_actuel == "X":   
        joueur_actuel = "O"
    else:
        joueur_actuel = "X"        


def resultat():
    if gagnant == "X" or gagnant == "O":
        print ("Le joueur", gagnant, "a gagné ! Bravo!")
    else:
        print("Le match est nul...")

jouer()

# appelle les fonction "choix_joueur" et "affichage_grille", 
# puis les boucles du programme jusqu'au résultat.
