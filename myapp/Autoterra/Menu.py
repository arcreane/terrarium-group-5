from Déf_valeurs_intervalle import *


def menu_principal():
    menu = 2
    while menu == 2:
        a = int(input("Que souhaitez-vous faire? \n1. Définir le niveau d’humidité \n2. Accéder à la bibliothèque"))
        if a == 1:
            b = int(input("Que souhaitez-vous faire? \n1. Valeurs \n2. Niveau d’humidité"))
            if b == 1:
                print ("Valeurs")
                def_valeurs()
                menu = int(input("Souhaitez-vous afficher le niveau d'humidité ? \n1. Oui \n2.Non, retournons au menu principal"))
                if menu == 1:
                    print("Niveau d’humidité")
                    #affichage_humid()
                    print("Retour au menu")
                    menu = 2
                elif menu == 2:
                    print("Retour au menu")
            elif b == 2:
                print ("\n Niveau d’humidité")
                #affichage_humid()
                menu = int(input("Souhaitez-vous changer les valeurs ? \n1. Oui \n 2.Non, retournons au menu principal"))
                if menu == 1:
                    print("Valeurs")
                    def_valeurs()
                    print("Retour au menu")
                    menu = 2
                elif menu == 2:
                    print("Retour au menu")
        elif a == 2:
            b = int(input("Que souhaitez-vous faire? \n1. Accéder à la bibliothèque \n2. Niveau d’humidité "))
            if b==1:
                print ("Bibliothèque")
                #bibliothèque()
                menu = int(input("Souhaitez-vous afficher le niveau d'humidité ? \n1. Oui \n 2.Non, retournons au menu principal"))
                if menu == 1:
                    print("Valeurs")
                    def_valeurs()
                    print("Retour au menu")
                    menu = 2
                elif menu == 2:
                    print("Retour au menu")

            elif b == 2:
                print("\n Niveau d’humidité")
                #affichage_humid()
                menu = int(input("Souhaitez-vous afficher le niveau d'humidité ? \n1. Oui \n 2.Non, retournons au menu principal"))
                if menu == 1:
                    print("Valeurs")
                    def_valeurs()
                    print("Retour au menu")
                    menu = 2
                elif menu == 2:
                    print("Retour au menu")

menu_principal()