import csv

ParkName = []
State = []
Names = []
with open("C:/Users/Mannan/Documents/Database/park_visit.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    print(csvReader)

    for row in csvReader:
        ParkName.append(row[0])
        State.append(row[3])

#print(State)
#print(ParkName)
def find(s, a):
    b=False
    for i in range(0,len(a)):
        if(s==a[i]):
            b=True

    return b
for i in range(0,len(State)):
    if(State[i]=="KY" and find(ParkName[i],Names)==False):
        print(ParkName[i])
        Names.append(ParkName[i])
        #print(ParkName[row])
