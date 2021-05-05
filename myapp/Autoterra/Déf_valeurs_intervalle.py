def def_valeurs():
    humid1=input("Pourcentage d'humidité de l'air minimum recherché")
    humid2=input("Pourcentage d'humidité de l'air maximum recherché")
    while humid2 <= humid1:
        print("Il y a une erreur, votre pourcentage maximal est inférieur ou égal minimum")
        humid2 = input("Pourcentage d'humidité de l'air maximum recherché")
    print("Votre taux d'humidité doit être compris entre",humid1,"et",humid2)


#humid1 = ()
#humid2 = ()
#def_valeurs(humid1,humid2)
#humid1 = humid1
#humid2 = humid2