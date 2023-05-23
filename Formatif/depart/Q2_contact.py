class Contact:
    def __init__(self, nom,prenom,adresse = "inconnu" ,email = "inconnu",num_telephone = "inconnu") -> None:
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.email = email
        self.num_telephone = num_telephone

        if self.email == "inconnu" or self.num_telephone == "inconnu":
            pass
        else:
                raise ValueError("Il faut un email ou un numéro de téléphone")
        def mettre_a_jour_info(self):
            pass



print()
contact_complet = Contact("Anastazie","Nisha","165 rue Pieux", "nisha.A@gmail","5142-111-7272")
contact_valide = Contact("Miklos","Warner",email="nisha.A@gmail")
contact_invalide = Contact("Erkan","Severie","165 rue Pieux")
print()