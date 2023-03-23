from telnetlib import GA


class Personne:
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        pass
class Joueur(Personne):
    def __init__(self, no_chandail, position, nom, prenom, date_naissance):
        super().__init__(nom, prenom, date_naissance)
        self.no_chandail = no_chandail
        self.position = position
        pass
class Attaquant(Joueur):
    def __init__(self, nb_tirs_au_but, nb_assistance,  nom, prenom, date_naissance, no_chandail, position):
        super().__init__(  nom, prenom, date_naissance, no_chandail, position)
        self.nb_tirs_au_but = nb_tirs_au_but
        self.nb_assistance = nb_assistance
        pass
class Defenseur(Joueur):
    def __init__(self, nb_interception, nb_passes,  nom, prenom, date_naissance, no_chandail, position) -> None:
        super().__init__( nom, prenom, date_naissance, no_chandail, position)
        self.nb_interception = nb_interception
        self.nb_passes = nb_passes

    def compter_buts(self, totalbuts):
        pass
class Gardien(Joueur):
    def __init__(self, nb_arrets, nb_tirs_essuyes, nom, prenom, date_naissance, no_chandail, position) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_arrets = nb_arrets
        self.nb_tirs_essuyes = nb_tirs_essuyes

    def arreter_tirs(self):
        pass

Gardien_Logan_Ketterer = Gardien(128,208,"Ketterer", "Logan", "9 novembre 1993", 1, "Gardien")
Defenseur_Zachary_Brault_Guillard = Defenseur(32,44, "Brault Gruillard", "Zachary","5 mars 1991",15,"Defenseur")
Attaquant_Sunusi_Ibrahim = Attaquant(23,44, "Ibrahim", "Sunusi", "1 octobre 2002",14, "Attaquant")
list2 = [Gardien_Logan_Ketterer, Defenseur_Zachary_Brault_Guillard, Attaquant_Sunusi_Ibrahim]
for d in [Gardien_Logan_Ketterer, Defenseur_Zachary_Brault_Guillard, Attaquant_Sunusi_Ibrahim]:
    print(d.__dict__)
    
    
class Equipe(Joueur):
    def __init__(self, no_chandail, position, nom, prenom, date_naissance, nbjoueur_la_ligue):
        super().__init__(no_chandail, position, nom, prenom, date_naissance)