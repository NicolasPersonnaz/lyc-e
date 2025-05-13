class Contact :

    def __init__(self, nom = 'pierre', prenom = 'dufour', email = 'adressemail@truc.com', tel = -1) :


        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.tel = tel
    def get_mail(self) :
        return self.email
    def set_mail(self,email):
        self.email = email

    def get_nom(self) :

        return self.nom
    def set_nom(self,nom):
        self.nom = nom
    def get_prenom(self) :
        return self.prenom
    def set_prenom(self,prenom) :
        self.prenom = prenom
    def get_tel(self):
        return self.tel
    def set_tel(self, tel) :
        self.tel = tel
    def __str__(self) :
        return str(self.tel) + self.prenom + self.nom + self.mail


contact = Contact('justin', 'bridou', 'just1@bridou.com', 664837238)
contact.set_mail(" souris@email.com ")
contact.set_nom(" butters ")
contact.set_prenom("cartman")

print(contact.get_prenom())
