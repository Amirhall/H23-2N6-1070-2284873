# comment intaller un module qu'on n'a pas déjà installé dans python
# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/
# Dans le terminal              pip install requests

# fakerapi.it/en
import requests
import json

BASE_URL = 'https://fakerapi.it/api/v1'


#  Le but est d'obtenir le 'price' moyen des produits de moins de 100000 qui sont dans la catégorie 3.


### - Q1) Faites une demande de 25 produits 

response = requests.get(f"{BASE_URL}/products?_quantity=25&_locale=fr_CA")


 
##  Q2) Utilisez json.dumps et
## indent pour obtenir 4 niveaux d'imbication des éléments de la réponse

resultat = json.dumps(response.json(),indent=4)

#  Q3)  changer un string en un dictionnaire avec json.load
# using json.loads() method
dict_resultat = json.loads(resultat)



# Q4)  Obtenez la liste des produits à partir de la clé 'data' du dictionnaire obtenu en Q3

liste_produits = dict_resultat["data"]


# Q5)  Créez vous deux variables initialisées à 0 au départ. 
#      Une pour accumuler le total des prix, l'autre pour compter le nombre de produits
#      Vous faites une boucle pour passer à travers la liste des produits obtenue en Q4
#           Dans la boucle, vous obtenez le prix du produit et castez-le en float
#           Si le produit a la catégorie 3 et que le prix est inférieur à 100000
#                   ajoutez-le au total des prix
#                   augmenter votre compteur de produit qui satisfont le test précédent
#      Après la boucle calculez la moyenne
#      Finalement imprimez le résultat, qui pourrait ressembler à ceci: 
#            "Parmi les 25 produits que j'ai obtenu, il y a 6 produits dans la catégorie 3 et leur prix moyen est de 12328.94$"



liste_produits = dict_resultat["data"]
print(liste_produits)

total_prix = 0
cpt_produits_dans_categorie3 = 0
for produit in liste_produits:
    prix = produit["price"]
    fprix = int(float(prix))
    if (3 in produit["categories"] and fprix < 100000):
        total_prix += fprix
        cpt_produits_dans_categorie3 += 1
moyenne = total_prix /  cpt_produits_dans_categorie3
print(f"Parmi les 25 produits que j'ai obtenu, il y a {cpt_produits_dans_categorie3} produits dans la catégorie 3 et leur prix moyen est de  {round(moyenne,2)}")
