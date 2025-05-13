'''
Ecrire en Python la classe Rectangle que l'on caractérise par une longueur et une largeur.
Ecrire pour cette classe les méthodes suivantes :
perimetre qui renvoie le périmètre du rectangle
aire qui renvoie l'aire du rectangle
est_carre qui renvoie True si le rectangle est un carré et False sinon
Créez un rectangle et testez les 3 méthodes ci-dessus.
Créez un rectangle avec une longueur et largeur égale (donc un carré) et testez les 3 méthodes ci-dessus
'''

class Rectangle :

    def __init__(self , longueur , largeur ) :
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self) :
        return 2*self.longueur + 2*self.largeur
    def aire(self) :
        return self.longueur * self.largeur
    def est_carre(self) :
        if self.longueur == self.largeur :
            return True
        else :
            return False


Rectangle1 = Rectangle(10 , 10)
Rectangle2 = Rectangle(20 , 10)
print(Rectangle2.est_carre())
print(Rectangle1.aire())