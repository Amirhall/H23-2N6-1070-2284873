class Bibliotheque:
    def __init__(self,nom,information_contact) -> None:
        self.nom = nom
        self._information_contact = information_contact
        

    def ajouter_livre(self, livre):
        pass




# Vérification
biblio_1 = Bibliotheque("CEM","111-222-3333")
biblio_2 = Bibliotheque("Banq","521-657-6584")

biblio_1.ajouter_livre("La Passe-Miroir, Tome 1")
biblio_1.ajouter_livre("Le Petit Prince")
biblio_2.ajouter_livre("Divergente, Tome 1")
biblio_2.ajouter_livre("Le Petit Prince")

print()
print(f" Livre à {biblio_1.nom} : {biblio_1.liste_livres}")
print(f" Livre à {biblio_2.nom} : {biblio_2.liste_livres}")
print(f" Livre au Québec : {Bibliotheque.liste_livres_Quebec}")
print()
# Si tout fonctionne, vous devriez obtenir le résultat suivant dans la console :
        #  Livre à CEM : ['La Passe-Miroir, Tome 1', 'Le Petit Prince']
        #  Livre à Banq : ['Divergente, Tome 1', 'Le Petit Prince']
        #  Livre au Québec : ['La Passe-Miroir, Tome 1', 'Le Petit Prince', 'Divergente, Tome 1']