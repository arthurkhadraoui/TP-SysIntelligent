class Army:



    def __init__(self, chief, moralValue):
        self.chief = chief
        self.moralValue = moralValue

    def getChief(self):
        return self.chief

    def getMoralValue(self):
        return self.moralValue

    def setChief(self, chief):
        self.chief = chief

    def setMoralValue(self, moralValue):
        self.moralValue = moralValue

    def __repr__(self):
        return "Chef: "+ self.chief.getPrenom() + " " + self.chief.getNom() + " \nValeur morale totale: " + str(self.moralValue)

    def get_total_moral(self):
        totalMoral = self.moralValue * self.chief.getBoostMoral()
        return totalMoral


