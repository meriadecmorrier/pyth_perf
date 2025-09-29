class Gateau:
    def __init__(self, nom, temps_cuisson, ingredients, etapes_recette, nom_createur):
        self.nom = nom
        self.temps_cuisson = temps_cuisson
        self.ingredients = ingredients
        self.etapes_recette = etapes_recette
        self.nom_createur = nom_createur

    def afficher_ingredients(self):
        print("Ingrédients:")
        for ing in self.ingredients:
            print(f"- {ing}")

    def afficher_recette(self):
        print("Recette:")
        for etp in self.etapes_recette:
            print(f"- {etp}")