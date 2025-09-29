class CompteBancaire:
    def __init__(self, numero_compte, nom, solde):
        self.numeroCompte = numero_compte
        self.nom = nom
        self.solde = solde

    def versement(self, montant):
        self.solde += montant
        print(f"Versement de {montant} effectué. Nouveau solde: {self.solde}")

    def retrait(self, montant):
        self.solde -= montant
        print(f"Retrait de {montant} effectué. Nouveau solde: {self.solde}")
        if self.solde < 0:
            self.agios()

    def agios(self):
        agios = abs(self.solde) * 0.05
        self.solde -= agios
        print(f"Agios de {agios} prélevés. Nouveau solde: {self.solde}")

    def afficher(self):
        print(f"Compte n°{self.numeroCompte}, Titulaire: {self.nom}, Solde: {self.solde}")