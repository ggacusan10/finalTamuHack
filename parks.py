import csv
import random

class parkData():

    def __init__(self):

        self.city = []
        self.parkName = []
        self.state = []
        self.outputPark = []


        with open("park_visit.csv") as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.parkName.append(row[0])
                self.state.append(row[3])




#museumName, city, state = readMyFile('static/museums.csv')
    def getPark(self,stateName):

        for i in range(0, len(self.state)):
            if (self.state[i] == stateName):  # enter what the user put for their location
                self.outputPark.append(self.parkName[i])

        return self.outputPark[random.randint(0,len(self.outputPark)-1)]



