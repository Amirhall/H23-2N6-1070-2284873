# comment intaller un module qu'on n'a pas déjà installé dans python
# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/
# Dans le terminal              pip install requests

# fakerapi.it/en
from traceback import print_exc
import requests
import json

BASE_URL = 'https://fakerapi.it/api/v1'


# pour avoir seulement X produits
# l'API nous offre /products?_quantity=X

# Q1)   faire une demande de 1 produit1 (GET/products?_quantity=1) et conservez le résultat dans une variable
Rep = requests.get('https://fakerapi.it/api/v1/products?_quantity=1')



# json.dump permet d'ajouter des arguments
# indent pour spécifier le niveau d'imbrication des éléments de la réponse
# et que ce soit plus facile à comprendre la structure de la réponse

# Q2)  faites un dumps de la réponse obtenue en Q1 avec un niveau d'indentation de 4  et conservez le résultat dans une variable
RepQ2 = json.dumps(Rep.json(), indent=4)


# Q3)  Le résultat obtenu en Q2 est un string et doit être changé en un dictionnaire avec json.load  et conservez le résultat dans une variable
# using json.loads() method
RepQ3 = json.loads(RepQ2)

#Si je regarde seulement ce qui m’intéresse
#dict_re         5
#           sultat = {
#             "data": [       
#             {
#                "id": 1,
#                "name": "Blanditiis aut in quia omnis.",
#                 "net_price": 2.15,
#                 "taxes": 22,
#                "price": "2.62",
#                 "categories": [
#                     2,
#                     3,
#                  ],
#             }
#             ]
#        }


# Donc, dict_resultat est un dictionnaire. La clé "data" me donne une liste. Qui n'a qu'un seul item pour le moment

#  dict_resultat["data"][0]  me donnerais un dictionnaire contenant les infos du produit
# #                            avec l'id, le name,..et le price que je recherche, ainsi qu'une liste de categories
#  Pour le moment, avec un produit, je peut obtenir le 'price' du produit et vérifier s'il est dans la catégorie 3.

# Q4)  Obtenez le premier élément du dictionnaire avec la clé 'data' dans une variable

RepQ4 = RepQ3["data"][0]

#  Donc on obtient quelque chose comme
# {'id': 1, 'name': 'Blanditiis aut in quia omnis.', 'net_price': 2.15, 'taxes': 22, 'price': '2.62', 'categories': [2, 3, 5]}


#  Q5) Obtenez le prix et changez le en un float
RepQ5 = RepQ4["price"]

float(RepQ5)

#  Q6)  Utilisez in pour vérifier si 3 fait partie des categories du dictionnaire des categories du produit
if '3' in RepQ5:
    cat = True
else:
    cat = False
#  Q7)  Imprimez le prix et si le produit est dans la catégorie 3 ou non
#       Quelque chose comme: "Le produit a le prix de 3945.01 et on peut savoir s'il est dans la catégorie 3: False"
print(f"Le produit a le prix de {RepQ5} et on peut savoir s'il est dans la catégorie 3: {cat}")







#  Si ce que je veux éventuellement obtenir serait le 'price' moyen des produits de moins de 100000 qui sont dans la catégorie 3.
#  Voyons si on peut faire cela avec le resultat de 5 produits

# # faire une demande de 25 produits (GET/products?_quantity=25)
response = requests.get(f"{BASE_URL}/products?_quantity=25&_locale=fr_CA")


 
# # json.dumps permet d'ajouter des arguments
# # indent permet de spécifier le niveau d'imbication des éléments de la réponse
resultat = json.dumps(response.json(),indent=4)


# changer un string en un dictionnaire avec json.load
# using json.loads() method
dict_resultat = json.loads(resultat)
# le data de liste_resultat est une liste de dictionnaire de produits


liste_produits = dict_resultat["data"]

total_prix = 0
cpt_produits_dans_categorie3 = 0
for produit in liste_produits:
    if (3 in produit["categories"] and prix<100000):
        total_prix += prix
        cpt_produits_dans_categorie3 += 1
moyenne = total_prix /  cpt_produits_dans_categorie3
print(f"Parmi les 25 produits que j'ai obtenu, il y a {cpt_produits_dans_categorie3} produits dans la catégorie 3 et leur prix moyen est de  {round(moyenne,2)}")

