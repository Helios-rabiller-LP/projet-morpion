# Initialiser le plateau de jeu comme une liste avec des cases vides
game_board = [" " for _ in range(9)]


def afficher_board(board):
    # Affiche le plateau en format 3x3
    for i in range(3):
        print(board[3 * i] + "|" + board[3 * i + 1] + "|" + board[3 * i + 2])
        if i < 2:
            print("-+-+-")


def get_player_move():
    # Demande au joueur de saisir un nombre entre 1 et 9 et le convertit en index
    while True:
        move = int(input("Enter a position (1-9): "))
        if 1 <= move <= 9 and game_board[move - 1] == " ":
            return move - 1  # Renvoie l'index correspondant dans la liste (0-8)
        else:
            print("Invalid move. Try again.")

def check_win(board):
    # Vérifie toutes les combinaisons gagnantes
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]  # Diagonales
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None


def tic_tac_toe():
    current_player = "X"
    for _ in range(9):  # Jusqu'à 9 tours possibles
        afficher_board(game_board)
        print(f"Player {current_player}'s turn.")
        move = get_player_move()
        game_board[move] = current_player

        # Vérifie si le joueur actuel a gagné
        winner = check_win(game_board)
        if winner:
            afficher_board(game_board)
            print(f"Player {winner} wins!")
            return
        # Alterne les joueurs
        current_player = "O" if current_player == "X" else "X"

    # Si aucune victoire, c'est une égalité
    afficher_board(game_board)
    print("It's a tie!")


# Démarrer le jeu
tic_tac_toe()
