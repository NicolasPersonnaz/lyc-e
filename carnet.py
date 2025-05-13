from contact import Contact
class Carnet :

    def __init__(self,id) :
        self.liste = []
        self.id = id

    def __str__(self) :
        chaine = ""
        for  i in self.liste :
            chaine += str(i)
        return chaine


    def __add__(self , objet2): # ajoute en fin de liste
        return self.liste.append(objet2)
    def __sub__(self , objet2): #retire en fin de liste
        return self.liste.remove(objet2)
    def __contains__(self, x) : # y a t il x dans la liste
        return x in self.liste
    def get_carnet(self) :
        return self.id
    def set_carnet(self , id) :
        self.id = id


