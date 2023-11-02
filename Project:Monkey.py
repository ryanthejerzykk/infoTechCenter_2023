print("*****************************************************")
print("gasoline branch\n")

# import the library here
import random
from time import sleep
# function that list gas levels and chooses one, and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty", " Low", "Quarter Tank", "Half tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice (gasLevelList)
    return currentGasLevel


# Function with list of gasStations
def listofgasStation():
    gasStation = ["shell","Speedway","Exon","Costco","Maraton","BP","Circle K","Wesco"]
    gasStationsNear =random.choice(gasStation)
    return gasStationsNear


# function will read the gas level gauge and say a close gas station if empty
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    milesToGasStationQuarter = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("****YOU ARE EMPTY****")
        sleep(2.1)
        print("CALLING TRIPLE A")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is low, looking for closest gas station")
        sleep(1.1111111111111111111111111)
        print("Closest gas station is", listofgasStation(),"which is",milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is has a quarter of a tank left, looking for closest gas station")
        sleep(1.1111111111111111111111111)
        print("Closest gas station is", listofgasStation(),"which is",milesToGasStationQuarter, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("your gas tank has a half tank checking for closest gas station.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("your gas has three quartes full")
    else:
        print("Your gas tank is full- Good Job")
gasLevelAlert()