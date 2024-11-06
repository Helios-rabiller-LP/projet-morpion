
structure = [ " " for _ in range(9)]

def afficher_board(structure):
    for i in range(3):
        print(structure[3*i] + " | " + structure[3*i + 1] + " | " + structure[3*i + 2])
        if i <2:
            print("--+--+--")

afficher_board(structure)