#jeu Tic_Tac_Toe 

values = [ " " for x in range(9)]


def structure():
    print(values[0] +  "   |   " + values[1] + " | " + values[2])
    print("----"+ "+"+ "-----"+ "+"+"----")
    print(values[3] +  "   |   " + values[4] + " | " + values[5])
    print("----"+ "+"+ "-----"+ "+"+"----")
    print(values[6] +  "   |   " + values[7]  + " | " + values[8])








def player():
    coup_player = 0 
    while (coup_player <= 0 or coup_player <9):
        coup_player = int(input("ou est ce que vous placez votre pion ? : "))
        if values[coup_player] != str(coup_player):
           print("case prise")
           coup_player = 0 
    values[coup_player] = [coup_player]
    return

player()

         


structure()




    



