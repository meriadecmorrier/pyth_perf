import json

# 1- Creation du dictionnaire
catalogue = {
  "produits": [
    {"id": 1, "nom": "Stylo", "prix": 1.8},
    {"id": 2, "nom": "Cahier", "prix": 2.5},
    {"id": 3, "nom": "Sac",   "prix": 19.9}
  ]
}

# 2a- sauvegarde dans fichier json
file = open("catalogue.json", "w")
json.dump(catalogue, file, indent=2)
file.close()

# 2b- lecture du fichier json
file = open("catalogue.json", "r")
data = json.load(file)
file.close()

# calcul du prix total des produits
prix_total = 0
for produit in data["produits"]:
    prix_total += produit["prix"]

# 2c- ajout de la clé "total" au dictionnaire
catalogue["total"] = prix_total

# 2d- affichage 
catalogue_total_str = json.dumps(catalogue, indent=2)
print("Affichage du catalogue total :")
print(catalogue_total_str)

# 2e- sauvegarde du catalogue total dans un fichier json aussi
with open("catalogue_total.json", "w") as file:
    json.dump(catalogue, file, indent=2)