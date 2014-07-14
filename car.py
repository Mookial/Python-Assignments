class Car:
    #fuel_efficiency-> miles/gallon

    def __init__(self, miles, gallons, maxTank):
        self.maxTank = maxTank #Fuel Tank Full
        self.miles = miles
        self.gallons = gallons
        self.current_fuel = 0

    def addGas (self):
        "Fill the tank"
        self.current_fuel = self.maxTank
        print("Gas is now ", self.current_fuel)

    def getGas (self):
        return self.current_fuel 
    
    def drive (self, milesDriven):
        "Efficiency =  miles/gallon, so used = efficiency * milesDriven / X gallons"
        usedGas = (milesDriven * self.gallons)/self.miles
        if (usedGas <= self.current_fuel):
            if (self.current_fuel - usedGas >= 0):
                self.current_fuel -= usedGas
                print("Gas Left ", self.current_fuel)
        else:
            print ("Tank too low!")
