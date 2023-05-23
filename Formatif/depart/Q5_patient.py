# Ajouter les propiétés grandeur_pouces et poids_livres
# 1 pouce = 2,54 centimètres
# 1 kilogramme = 2,20462 livres

# La fonction round() permet d'obtenir seulement un certain nombre de chiffres après la virgule.

class Patient:
    def __init__(self,nom,grandeur,poids,age,num_telephone) -> None:
        self.nom = nom
        self.grandeur = grandeur    # en centimètres
        self.poids = poids          #en kilogrammes
        self.age = age
        self.num_telephone = num_telephone
        
    def Grandeur_pouce(self):
        Pouce = self.grandeur



patient_1 = Patient("Anneth Yull", 163, 52, 47, "514-116-9595")
print()
print(f'  {patient_1.nom} a {patient_1.age} ans, mesure {patient_1.grandeur}cm et pèse {patient_1.poids}Kg.')
print(f'  {patient_1.nom} a {patient_1.age} ans, mesure {patient_1.grandeur_pouces} pouces et pèse {patient_1.poids_livres} livres.')
print()

# Ces lignes devront produire les résultats :
    #   Anneth Yull a 47 ans, mesure 163cm et pèse 52Kg.
    #   Anneth Yull a 47 ans, mesure 64.17 pouces et pèse 114.64 livres.