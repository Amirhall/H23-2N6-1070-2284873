from itertools import product
import json
import os, requests
from urllib import request
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Maintenant que nous avons un script capable de lire et décoder le fichier csv.
# Nous voulons ajouter des informations à liste de produits de chaque client
#       le prix de chaque produit et sa catégorie

# Les informations sur les produits proviennent du site du magasin.
# Vous devez aller chercher les informations à l'aide du module requests.
UserUrl = "https://fakestoreapi.com/users"
RequestUser = requests.get(UserUrl)
UserInfo1 = json.dumps(RequestUser.json(), indent=4)
UserInfo = json.loads(UserInfo1)
#UserId = UserInfo["id"]
#print(UserInfo)
for user in UserInfo:
    userid = UserInfo[1]["id"] 
    print(f"UserId: {userid}")




