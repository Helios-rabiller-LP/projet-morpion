""""#definir la grille visuelle et valeur des cases
grille= ['1', '2', '3', '4', '5', '6', '7', '8','9']
def the_grid(grille):
    print(f"{grille[0]}   | {grille[1]}   | {grille[2]}")
    print("----+-----+----")
    print(f"{grille[3]}   | {grille[4]}   | {grille[5]}")
    print("----+-----+----")
    print(f"{grille[6]}   | {grille[7]}   | {grille[8]}")
#appeller la grille
the_grid(grille) 

#verifier la victoire
def verifier_victoire():
    # Vérifier les lignes
    for i in range(0, 9, 3):
        if grille[i] == grille[i+1] == grille[i+2]:
            return True
    # Vérifier les colonnes
    for i in range(3):
        if grille[i] == grille[i+3] == grille[i+6]:
            return True
    # Vérifier les diagonales
    if grille[0] == grille[4] == grille[8]:
        return True
    if grille[2] == grille[4] == grille[6]:
        return True
    return False """ 
    
    # Fonction pour afficher la grille
grille= ['1', '2', '3', '4', '5', '6', '7', '8','9']
def afficher_grille(grille):
    print(f"{grille[0]}   | {grille[1]}   | {grille[2]}")
    print("----+-----+----")
    print(f"{grille[3]}   | {grille[4]}   | {grille[5]}")
    print("----+-----+----")
    print(f"{grille[6]}   | {grille[7]}   | {grille[8]}")
#appeller la grille
afficher_grille(grille)
    
        




