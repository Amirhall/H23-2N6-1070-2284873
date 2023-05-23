# Complétez la classe AnimalDeCompagnie et modifiez les classes Chien et Chat
# Les classes Chat et Chien doivent hériter de la classe AnimalDeCompagnie
# Faites en sorte de minimiser la répétition de code.

class Animaldecompanie:
    def __init__(self,nom,age,proprietaire) -> None:
        self.nom = nom
        self.age = age
        self.proprietaire = proprietaire

class Chien(Animaldecompanie):
    def __init__(self,nom,age,proprietaire) -> None:
        super().__init__(nom,age,proprietaire)
    
    def flatter(self):
        return(f"{self.nom} est heureux")
    
    def aboyer(self):
        return("Woof")

class Chat(Animaldecompanie):
    def __init__(self,nom,age,proprietaire) -> None:
        super().__init__(nom,age,proprietaire)
    
    def flatter(self):
        return(f"{self.nom} est heureux")
    
    def miauler(self):
        return("Meow")


chien_1 = Chien("Rex", 6, "Lynwood")
chat_1 = Chat("Neige", 13, "Saara")
print()
print(f"{chien_1.proprietaire} flatte son compagnion de {chien_1.age} ans. {chien_1.flatter()}, il aboit : {chien_1.aboyer()}")
print(f"{chat_1.proprietaire} flatte son compagnion de {chat_1.age} ans. {chat_1.flatter()}, il miaule : {chat_1.miauler()}")
print()
# Ces lignes devrait donner le résultat suivant :
        # Lynwood flatte son compagnion de 6 ans. Rex est heureux, il aboit : Woof
        # Saara flatte son compagnion de 13 ans. Neige est heureux, il miaule : Meow