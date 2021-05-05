from Déf_valeurs_intervalle import *

def affichage_humid():
    humid="35"
    print("Le taux d'humidité de l'air est actuellement de",humid,"%")
    if humid1 <= humid <= humid2 :
        print ("Le taux d'humidité est correct")
    else:
        print("Le taux d'humidité est incorrect")

affichage_humid()