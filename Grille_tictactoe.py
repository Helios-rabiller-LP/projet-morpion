#definir la grid visuelle et valeur des cases
grid= ['1', '2', '3', '4', '5', '6', '7', '8','9']
def the_grid(grid):
    print(f"{grid[0]}   | {grid[1]}   | {grid[2]}")
    print("----+-----+----")
    print(f"{grid[3]}   | {grid[4]}   | {grid[5]}")
    print("----+-----+----")
    print(f"{grid[6]}   | {grid[7]}   | {grid[8]}")
#appeller la grille
the_grid(grid) 

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
    return False
