class Character:



    def __init__(self,nom,prenom,age,profession,boostMoral):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.boostMoral = boostMoral

    def getAge(self):
        return self.age

    def getPrenom(self):
        return self.Prenom

    def getNom(self):
        return self.nom

    def getProfession(self):
        return self.profession

    def getBoostMoral(self):
        return self.boostMoral

    def setNom(self,nom):
        self.nom = nom

    def setPrenom(self,prenom):
        self.prenom = prenom

    def setAge(self,age):
        self.age = age

    def setProfession(self,profession):
        self.profession = profession

    def setBoostMoral(self,boostMoral):
        self.boostMoral = boostMoral

    def __repr__(self):
        return "Prenom: "+self.prenom + " Nom: " + self.nom + "\nAge: " + str(self.age) + " Profession: " + self.profession + " Boost Moral: "+ str(self.boostMoral)
