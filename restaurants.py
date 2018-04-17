import csv
import random

class restaurantData():

    def __init__(self):
        
        self.city = []
        self.restaurantName = []
        self.outputRestaurants = []

        with open("r.csv") as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.restaurantName.append(row[20])
                self.city.append(row[2])



    def getRestaurant(self,cityName):
        for i in range(0, len(self.city)):
            if(self.city[i] == cityName): #enter what the user put for their location
                self.outputRestaurants.append(self.restaurantName[i])

        return self.outputRestaurants[random.randint(0,len(self.outputRestaurants)) - 1];
