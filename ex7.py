class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def set_longueur(self, longueur):
        self._longueur = longueur

    def get_largeur(self):
        return self._largeur

    def set_largeur(self, largeur):
        self._largeur = largeur

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    def get_hauteur(self):
        return self._hauteur

    def set_hauteur(self, hauteur):
        self._hauteur = hauteur

    def volume(self):
        return self._longueur * self._largeur * self._hauteur


rectangle = Rectangle(4, 5)
print("Longueur du rectangle :", rectangle.get_longueur())
print("Largeur du rectangle :", rectangle.get_largeur())
print("Périmètre du rectangle :", rectangle.perimetre())
print("Surface du rectangle :", rectangle.surface())

parallelepiped = Parallelepipede(4, 5, 6)
print("Longueur du parallélépipède :", parallelepiped.get_longueur())
print("Largeur du parallélépipède :", parallelepiped.get_largeur())
print("Hauteur du parallélépipède :", parallelepiped.get_hauteur())
print("Périmètre du parallélépipède :", parallelepiped.perimetre())
print("Surface du parallélépipède :", parallelepiped.surface())
print("Volume du parallélépipède :", parallelepiped.volume())