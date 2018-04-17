'''
import csv

def readMyFile(filename):
    city = []
    restaurantName = []
    address = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            restaurantName.append(row[20])
            city.append(row[2])
            address.append(row[0])
            #state.append(row[8])

    return restaurantName, city


restaurantName, city, address = readMyFile('r.csv')

for i in range(0, len(city)):
    if(city[i] == "Brooklyn"): #enter what the user put for their location
        print(restaurantName[i])
'''

import csv
import random

class restaurantData():

    def __init__(self):
        #readMyFile(self, "r.csv")

        self.city = []
        self.restaurantName = []
        self.outputRestaurants = []

        with open("r.csv") as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.restaurantName.append(row[20])
                self.city.append(row[2])

    '''
    def readMyFile(self, filename):
        self.city = []
        self.restaurantName = []
        self.outputRestaurants = []

        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.restaurantName.append(row[20])
                self.city.append(row[2])

        return restaurantName, city
    '''

    def getRestaurant(self,cityName):
        for i in range(0, len(self.city)):
            if(self.city[i] == cityName): #enter what the user put for their location
                self.outputRestaurants.append(self.restaurantName[i])

        return self.outputRestaurants[random.randint(0,len(self.outputRestaurants)) - 1];


res = restaurantData()

test = res.getRestaurant("Brooklyn")

print test
