import csv
import random

class museumData():

    def __init__(self):

        self.city = []
        self.museumName = []
        self.state = []
        self.outputMuseum = []


        with open("museums.csv") as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.museumName.append(row[1])
                self.city.append(row[7])
                self.state.append(row[8])




#museumName, city, state = readMyFile('static/museums.csv')
    def getMuseum(self,cityName):

        for i in range(0, len(self.city)):
            if (self.city[i] == cityName):  # enter what the user put for their location
                self.outputMuseum.append(self.museumName[i])

        return self.outputMuseum[random.randint(0,len(self.outputMuseum)-1)]


mus = museumData()
test = mus.getMuseum("ANCHORAGE")
print(test)

