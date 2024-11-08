def choix_case():
    while True :
        joueur_actuel = "X"
        choix_case = int(input("veillez choisir une case vide entre 0 et 8 : "))
        while joueur_actuel != choix_case :
            print("choisissez une autre case :")
            choix_case = int(input("veillez choisir une case vide entre 0 et 8 : "))
            

    print("c'est au tour du joueur suivant :")