class WaterTank:
    """ Classe représentant un réservoir d'eau. """

    volume_total = 0

    def __init__(self,poids: float,capacite_max: float,niveau_remplissage: float):
        self.poids = poids
        self.capacite_max = capacite_max
        self.niveau_remplissage = niveau_remplissage
        WaterTank.volume_total += niveau_remplissage
    
    @property
    def poids_total(self):
        return self.poids + self.niveau_remplissage
    
    def remplir(self, quantite: float):
        quantite_a_ajouter = min(quantite, self.capacite_max - self.niveau_remplissage)
        self.niveau_remplissage += quantite_a_ajouter
        WaterTank.volume_total += quantite_a_ajouter
        print(f"Remplissage effectué. Niveau de remplissage: {self.niveau_remplissage}")
    
    def vider(self, quantite: float):
        quantite_a_retirer = min(quantite, self.niveau_remplissage)
        self.niveau_remplissage -= quantite_a_retirer
        WaterTank.volume_total -= quantite_a_retirer
        print(f"Vidage effectué. Niveau de remplissage: {self.niveau_remplissage}")        