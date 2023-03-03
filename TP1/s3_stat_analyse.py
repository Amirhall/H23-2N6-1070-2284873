import os, s2_req_produit_api
from shutil import which
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# On cherche ici à produire un fichier texte avec une courte analyse des données de ventes.
# Pour chaque valeur produite, vous devez écrire une phrase indiquant à quoi correspond cette valeur.

# Globalement :
#   Nombre total d'articles vendus
#   Montant total des ventes
#   Prix moyen des commandes

#   Personne ayant fait la commande la plus élevée avec le montant de la commande
#   Personne ayant fait la commande la moins élevée avec le montant de la commande

#Pour des points supplémentaires, vous pouvez aussi extraire les informations suivantes :
# Par catégorie :
#   Nombre total d'articles vendus
#   Montant total des ventes
Riche = ""
Pauvre = ""
CommandePlusCher = 0
CommandeMoinsCher = 99999999999999999999999999
TotalArticleVendu = 0
TotalMontant = 0
liste = s2_req_produit_api.listes1
for dico in liste:
    commande = dico["commande"]
    for orders in commande:
        TotalArticleVendu = TotalArticleVendu + int(orders["quantity"])
        for catalog in s2_req_produit_api.ProductsInfo:
            if catalog["id"] == orders["ProductId"]:
                TotalMontant = TotalMontant + (int(catalog["price"]) * int(orders["quantity"]))
                if catalog["price"] > CommandePlusCher:
                    catalog["price"] = CommandePlusCher
                    Riche = dico["nom"] + " " + dico["prenom"]
                if catalog["price"] < CommandeMoinsCher:
                    catalog["price"] = CommandeMoinsCher
                    Pauvre = dico["nom"] + " " + dico["prenom"]



Moyenne = TotalMontant / TotalArticleVendu
with open("Données de vente.txt", "w") as file:
    file.writelines(f"Nombre total d'articles vendus: {TotalArticleVendu} \n") 
    file.writelines(f"Montant total des ventes: {TotalMontant}\n")
    file.writelines(f"Prix moyen des commandes: {round(Moyenne, 2)}\n")
    file.writelines(f"Personne ayant fait la commande la plus élevée avec le montant de la commande: {Riche}\n")
    file.writelines(f"Personne ayant fait la commande la moins élevée avec le montant de la commande: {Pauvre}\n")
    