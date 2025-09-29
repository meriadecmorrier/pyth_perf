from gateau import Gateau
from comptebancaire import CompteBancaire

cheesecake = Gateau("cheesecake", 45, ["Speculoos", "Beurre", "Fromage blanc"], ["Ecraser les speculoos", "Faire fondre le beurre", "Mélanger le tout"], "Meriadec")

cheesecake.afficher_ingredients()
cheesecake.afficher_recette()



mon_compte = CompteBancaire("123456", "Meriadec", 50)
mon_compte.afficher()
mon_compte.versement(100)
mon_compte.retrait(200)
