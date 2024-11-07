
# variables globales du jeu:
joueur_actuel= ""
grille = ["¤","¤","¤","¤","¤","¤","¤","¤","¤"]
fin_jeu = False 
gagnant = ""
choix_partie= ""



#fonctions du jeu a appeler en debut de programme:
def jouer():
    choix_joueur()          #1
    affichage_grille()       #2                    
    
    # et conditions principales du jeu (en boucle) pendant le jeu (programme):
    while fin_jeu == False :
        tour(joueur_actuel) #3
        verifier_fin_jeu()  #4
        joueur_suivant()    #5
        """while fin_jeu == True:
            resultat()
            relancer_partie()      
        else:"""
        resultat()
    relancer_partie()  #6
    
    
    
    
# 1) fonction definir les joueurs:
def choix_joueur():
    global joueur_actuel #appel le joueur actuel dans les differentes fonctions du jeu
    joueur_actuel = input("On Joue? Veuillez taper X ou O svp: ")
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
    while pos_valide == False: # ou : while not pos_valide:
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos = input("veuillez selectionner une case libre: ")
        else:
            pos = int(pos) -1  # transformation chaine de caractere en entier pour verif condition
        """return True"""
        
        #finir la verification:
        if grille[pos] == "¤": # si "position disponible"
            pos_valide = True 
        else:
            print("Position non disponible ! Gamberge !")
            print("Choisir un chiffre entre 1 et 9, tu peux le faire ! : ")
    
        grille[pos] = joueur
        affichage_grille()


# verification de victoire: 
def verifier_victoire():
    global fin_jeu
    global gagnant
    
    #victoire sur lignes:
    if grille[0]== grille[1]== grille[2] and grille[2] != "¤" :
        fin_jeu= True
        gagnant= grille[0]
        
    elif grille[3]== grille[4]== grille[5] and grille[5] != "¤" :
        fin_jeu= True
        gagnant= grille[3] 
           
    elif grille[6]== grille[7]== grille[8] and grille[8] != "¤" :
        fin_jeu= True
        gagnant= grille[6]
    
    #victoire sur colonnes: 
    elif grille[0]== grille[3]== grille[6] and grille[6] != "¤" :
        fin_jeu= True
        gagnant= grille[0]
    elif grille[1]== grille[4]== grille[7] and grille[7] != "¤" :
        fin_jeu= True
        gagnant= grille[1]
    elif grille[2]== grille[5]== grille[8] and grille[8] != "¤" :
        fin_jeu= True
        gagnant= grille[2]    
    
    #victoire sur diagonales :
    elif grille[0]== grille[4]== grille[8] and grille[8] != "¤" :
        fin_jeu= True
        gagnant= grille[0]
    elif grille[2]== grille[4]== grille[6] and grille[6] != "¤" :
        fin_jeu= True
        gagnant= grille[2]    
 
#verif de match nul:        
def verif_match_nul():
    global fin_jeu #on va modifier cette valeur
    if "¤" not in grille:
        fin_jeu= True
        
# fonctions de verifications a appeler avant victoire:
def verifier_fin_jeu():
    verifier_victoire()
    verif_match_nul()
    


#definir joueur suivant:
def joueur_suivant():
    global joueur_actuel
    if joueur_actuel == "X":   
        joueur_actuel = "O"
    else:
        joueur_actuel = "X"        


def resultat():
    if gagnant == "X" or gagnant == "O":
        print ("Le joueur", gagnant, "a gagné ! Bravo!")
        relancer_partie()
        
    else:
        print("Le match est nul...")
    

def relancer_partie():
    global choix_partie
    while fin_jeu == True:
        choix_partie = input("Voulez vous recommencer une partie ? tapez oui ou non : ")
        if choix_partie == "oui" or "OUI":
            jouer()
        elif choix_partie == "non" or "NON":
            break
        else:
            relancer_partie()
        
   
jouer()

# appelle les fonction "choix_joueur" et "affichage_grille", 
# puis les boucles du programme jusqu'au résultat.
