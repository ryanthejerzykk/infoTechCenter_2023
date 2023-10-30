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
    milesToGasStation = round(random.uniform(1,25),1)
    print(milesToGasStation)


gasLevelAlert()