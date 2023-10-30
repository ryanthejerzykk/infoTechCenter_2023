print("*****************************************************")
print("gasoline branch\n")

# import the library here
import random
from time import sleep
# function that list gas levels and chooses one, and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty", " Low", "Quarter Tank", "Half tank", "Three Quarter Tank", "Full Tank"]
    currenGasLevel = random.choice (gasLevelList)
    return currenGasLevel


# function will read the gas level gauge and say a close gas station if empty
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarter = round(random.uniform(25.1,50),1)
    print("low =",milesToGasStationLow)
    print("Quarter=", milesToGasStationQuarter)


gasLevelAlert()