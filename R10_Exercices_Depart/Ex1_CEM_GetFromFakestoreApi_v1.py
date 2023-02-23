
from argparse import MetavarTypeHelpFormatter
import re
import requests
import json


base_url="https://fakestoreapi.com"

# Q1 Écrivez une fonction appelée request_carts qui aura 1 paramètre
#   soit le nombre de carts que vous voulez aller chercher
#   Le nombre de cart doit être donné lors de l'appel de la fonction 
#           mais s'il n'est pas donné il faut que cela ne cause pas d'erreur
#   Si le nombre de cart n'est pas donné lors de l'appel, 
#           donnez un message comme quoi il faut préciser le nombre de carts 
#           et arrêter l'exécution de la fonction
#   Vérifiez que le nombre donné lors de l'appel est entre 1 et 10
#   Si ce n'est pas le cas, 
#          donnez un message comme quoi il faut demander entre 1 et 10 carts, 
#          en précisant le nombre de carts qui avait été demandé
#   Si on passe autre chose qu'un nombre entier en paramètre 
#          faites un message comme quoi il faut entrer un nombre entre 1 et 10

#   La fonction doit retourner les carts obtenu avec la requête get du site webs. Mais seulement si le nombre de carts demandés est entre 1 et 10

def request_carts(nbcart = 0):
    rep = requests.get(f"{base_url}/carts?limit={nbcart}")
    rep2 = rep.json()
    return rep2
    
if request_carts() is None:
    print("il faut preciser le nombre de cart")
elif request_carts < 1 and request_carts() > 10:
    print(f"il faut entre 1 et 10 carts et non {request_carts()}")
elif type(request_carts()) != int:
    print("il faut entrer un nombre entre 1 et 10")
request_carts()

# Q2 Écrivez une fonction appelée request_products qui aura 1 paramètre
#   soit le nombre de produits que vous voulez aller chercher
#   Le nombre de produit doit soit être donné lors de l'appel de la fonction
#                             soit être demandé à l'usager s'il n'est pas donné
#   Vérifiez que le nombre demandé est entre 1 et 10
#   Limitez cette valeur à 10 si l'usager en demande plus et donnez un message comme quoi vous avez cette limite
#   Si le nombre demandé est moins de 1, obtenez 1 produit tout simplement

#   La fonction doit retourner le nombre de produits demandés, si le nombre est entre 1 et 10









