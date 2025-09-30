class Personne:
    def __init__(self, nom, prenom, numero_tel, email):
        self.nom = nom
        self.prenom = prenom
        self.numero_tel = numero_tel
        self.email = email

    def __str__(self):
        return f"Prenom: {self.prenom}, Nom: {self.nom}, Tel: {self.numero_tel}, Email: {self.email}"
    
class Travailleur(Personne):
    def __init__(self, nom, prenom, numero_tel, email, nom_entreprise, adresse_entreprise, tel_pro):
        super().__init__(nom, prenom, numero_tel, email)
        self.nom_entreprise = nom_entreprise
        self.adresse_entreprise = adresse_entreprise
        self.tel_pro = tel_pro

    def __str__(self):
        return (f"{super().__str__()}, Entreprise: {self.nom_entreprise}, Adresse Entreprise: {self.adresse_entreprise}, Tel Pro: {self.tel_pro}")
    
class Etudiant(Travailleur):
    def __init__(self, nom, prenom, numero_tel, email, nom_entreprise, adresse_entreprise, tel_pro, disciplines, types_scientifiques):
        super().__init__(nom, prenom, numero_tel, email, nom_entreprise, adresse_entreprise, tel_pro)
        self.disciplines = disciplines
        self.types_scientifiques = types_scientifiques

    def __str__(self):
        return (f"{super().__str__()}, Disciplines: {self.disciplines}, Types Scientifiques: {self.types_scientifiques}")

etu1 = Etudiant("Morty", "Rick", "123456789", "<morty@gmail.com>", "Universite", "Paris 5", "987654321", ["Math", "Physique"], ["Theorique", "Experimentale"])
print(etu1)
