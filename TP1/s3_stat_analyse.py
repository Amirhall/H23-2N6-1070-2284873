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
MenClothing = 0
Jewelery = 0
Electronics = 0
WomanClothing = 0
MontantMenClothing = 0
MontantJewelery = 0
MontantElectronics = 0
MontantWomanClothing = 0

liste = s2_req_produit_api.listes1
for dico in liste:
    CoutCommande = 0
    commande = dico["commande"]
    for orders in commande:
        TotalArticleVendu = TotalArticleVendu + int(orders["quantity"])
        for catalog in s2_req_produit_api.ProductsInfo:
            if catalog["id"] == orders["ProductId"]:
                TotalMontant = TotalMontant + (int(catalog["price"]) * int(orders["quantity"]))
                CoutCommande = CoutCommande + (int(catalog["price"]) * int(orders["quantity"]))
                if catalog["category"] == "men's clothing":
                    MenClothing +=1
                    MontantMenClothing = MontantMenClothing + (int(catalog["price"]) * int(orders["quantity"]))
                if catalog["category"] == "women's clothing":
                    WomanClothing +=1
                    MontantWomanClothing = MontantWomanClothing + (int(catalog["price"]) * int(orders["quantity"]))
                if catalog["category"] == "jewelery":
                    Jewelery +=1
                    MontantJewelery = MontantJewelery + (int(catalog["price"]) * int(orders["quantity"]))
                if catalog["category"] == "electronics":
                    Electronics +=1
                    MontantElectronics = MontantElectronics + (int(catalog["price"]) * int(orders["quantity"]))                           
    if CoutCommande > CommandePlusCher:
        CommandePlusCher = CoutCommande
        Riche = dico["nom"]+ " " + dico["prenom"]
    if CoutCommande < CommandeMoinsCher:
        CommandePlusCher = CoutCommande
        Pauvre = dico["nom"]+ " " + dico["prenom"]

Moyenne = TotalMontant / TotalArticleVendu
with open("Données de vente.txt", "w") as file:
    file.writelines(f"Nombre total d'articles vendus: {TotalArticleVendu} \n") 
    file.writelines(f"Montant total des ventes: {TotalMontant} $\n")
    file.writelines(f"Prix moyen des commandes: {round(Moyenne, 2)} $\n")
    file.writelines(f"Personne ayant fait la commande la plus élevée avec le montant de la commande: {Riche}\n")
    file.writelines(f"Personne ayant fait la commande la moins élevée avec le montant de la commande: {Pauvre}\n")
    file.writelines("\n")
    file.writelines("Par Catégorie: \n")
    file.writelines("\n")
    file.writelines("Man's Clothings: \n")
    file.writelines(f"Nombre total d'articles vendus: {MenClothing} \n")
    file.writelines(f"Montant total des ventes: {MontantMenClothing} $\n")
    file.writelines("\n")
    file.writelines("Woman's Clothing\n")
    file.writelines(f"Nombre total d'articles vendus: {WomanClothing} \n")
    file.writelines(f"Montant total des ventes: {MontantWomanClothing} $\n")
    file.writelines("\n")
    file.writelines("Jewlery\n")
    file.writelines(f"Nombre total d'articles vendus: {Jewelery} \n")
    file.writelines(f"Montant total des ventes: {MontantJewelery} $\n")
    file.writelines("\n")
    file.writelines("Electronics\n")
    file.writelines(f"Nombre total d'articles vendus: {Electronics} \n")
    file.writelines(f"Montant total des ventes: {MontantElectronics} $\n")
    file.writelines("\n")
    
    
    
    # Par catégorie :
#   Nombre total d'articles vendus
#   Montant total des ventes
