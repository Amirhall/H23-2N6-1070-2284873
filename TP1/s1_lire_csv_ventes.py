from ast import Index
from asyncore import read
import csv
import os
from textwrap import indent
import json
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Vous devez lire et extraire les informations du csv "data_ventes.csv"
# Le format de ce csv ne permet pas d'extraire les données très facilement.
# Regardez-le avant de commencer.

# Pour chaque client, il y la quantité de chacun des produits qu'ils ont achetés. 
# Les ids des produits sont dans l'en-tête et en ordre. 
# Donc les valeurs dans la colonne prodID1 correspondent à la quantité du produit dont l'ID est 1.
# Il en est ainsi pour chacun des 20 produits disponibles.

# Le but ultime de ce script est d'arriver à une liste, contenant pour chaque client
dic = 0
with open("data_ventes.csv", "r", encoding="utf-8") as date_vente :
    reader = csv.reader(date_vente)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    FirstLine = next(reader)
    liste1 = []
    ProductList = []
    Dic1 = {}
    y = 3
    for line in reader:
        for index, val in enumerate(line):
            line2 = val[3:]
            Dic1 = { "ProductId": index, "quantity":line2[index]}
            ProductList.append(Dic1)
            y = y + 1
        dictionnaire = {FirstLine[0] : line[0], FirstLine[1] : line[1], FirstLine[2] : line[2], "commande" : ProductList}
        liste1.append(dictionnaire)
        #ProductList.append({FirstLine[line] : line[line]})
        #liste1.append(ProductList)
        
    print(json.dumps(liste1,indent = 4))







        # for lignes in line:
        # print(line)
        # json.dumps(line,indent =4)
        #x = {["UserId" : line[0]]
        #print(json.dumps(x,indent = 4))       