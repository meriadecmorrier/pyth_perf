class Rectangle():
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        print(f"Rectangle créé avec longueur={longueur} et largeur={largeur}")

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def surface(self):
        return self.longueur * self.largeur
    

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur
        print(f"Parallélépipède créé  sur la base d'un rectangle de taille {longueur}x{largeur} avec hauteur={hauteur}")

    def volume(self):
        return self.longueur * self.largeur * self.hauteur
    
    def perimetre(self):
        return 4 * (self.longueur + self.largeur + self.hauteur)
    
    def surface(self):
        return 2 * (self.longueur * self.largeur + self.longueur * self.hauteur + self.largeur * self.hauteur)
    

# Exemples

print(f"Volume: {Parallelepipede(2,3,4).volume()}")
print(f"Surface: {Parallelepipede(2,3,4).surface()}")
