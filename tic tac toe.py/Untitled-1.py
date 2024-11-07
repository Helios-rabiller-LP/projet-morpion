
def afficher_plateau(plateau):
    """Affiche le plateau de jeu."""
    for ligne in plateau:
        print("|".join(ligne))
        print("-----")


def verifier_victoire(plateau, symbole):
    """Vérifie s'il y a une victoire pour le symbole donné."""
    # Vérification des lignes
    for ligne in plateau:
        if all(case == symbole for case in ligne):
            return True

    # Vérification des colonnes
    for colonne in range(3):
        if all(plateau[ligne][colonne] == symbole for ligne in range(3)):
            return True

    # Vérification des diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == symbole:
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] == symbole:
        return True

    return False


def jeu_tic_tac_toe():
    """Fonction principale pour jouer au Tic-Tac-Toe."""
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    symboles = ["X", "O"]
    joueur = 0  # Joueur 1 commence

    while True:
        afficher_plateau(plateau)
        print(f"C'est au joueur {joueur + 1} ({symboles[joueur]}) de jouer.")

        # Demander au joueur de choisir une position
        while True:
            try:
                ligne = int(input("Choisissez la ligne (1-3) : ")) - 1
                colonne = int(input("Choisissez la colonne (1-3) : ")) - 1
                if plateau[ligne][colonne] == " ":
                    plateau[ligne][colonne] = symboles[joueur]
                    break
                else:
                    print("Cette case est déjà occupée. Choisissez une autre position.")
            except (ValueError, IndexError):
                print("Entrée invalide. Veuillez saisir un nombre entre 1 et 3.")

        # Vérifier s'il y a une victoire
        if verifier_victoire(plateau, symboles[joueur]):
            afficher_plateau(plateau)
            print(f"Le joueur {joueur + 1} ({symboles[joueur]}) remporte la partie !")
            break

        # Vérifier s'il y a une égalité
        if all(plateau[ligne][colonne] != " " for ligne in range(3) for colonne in range(3)):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        # Passer au joueur suivant
        joueur = (joueur + 1) % 2


