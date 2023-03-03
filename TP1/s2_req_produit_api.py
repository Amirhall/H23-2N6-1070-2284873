from itertools import product
import json, s1_lire_csv_ventes
from textwrap import indent
import os, requests
from urllib import request

from s1_lire_csv_ventes import Dic1
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Maintenant que nous avons un script capable de lire et décoder le fichier csv.
# Nous voulons ajouter des informations à liste de produits de chaque client
#       le prix de chaque produit et sa catégorie

# Les informations sur les produits proviennent du site du magasin.
# Vous devez aller chercher les informations à l'aide du module requests.

listes1 = s1_lire_csv_ventes.liste1
url = requests.get("https://fakestoreapi.com/products")
productdumps = json.dumps(url.json(),indent=4)
ProductsInfo = json.loads(productdumps)
for dico in listes1:
    commande = dico["commande"]
    for orders in commande:
        for catalog in ProductsInfo:
            if catalog["id"] == orders["ProductId"]:
                orders.update({"price": catalog["price"], "category" : catalog["category"]})

                


print(listes1)