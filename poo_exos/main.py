from gateau import Gateau
from comptebancaire import CompteBancaire
from watertank import WaterTank

cheesecake = Gateau("cheesecake", 45, ["Speculoos", "Beurre", "Fromage blanc"], ["Ecraser les speculoos", "Faire fondre le beurre", "Mélanger le tout"], "Meriadec")

cheesecake.afficher_ingredients()
cheesecake.afficher_recette()


mon_compte = CompteBancaire("123456", "Meriadec", 50)
mon_compte.afficher()
mon_compte.versement(100)
mon_compte.retrait(200)

#########################
### Test classe WaterTank

tank = WaterTank(100, 500, 0)
tank.remplir(200)
tank.vider(50)

tank2 = WaterTank(100, 500, 300)

print(f"Volume total dans tous les réservoirs: {WaterTank.volume_total}")
print(f"Poids total du tank 1: {tank.poids_total}")