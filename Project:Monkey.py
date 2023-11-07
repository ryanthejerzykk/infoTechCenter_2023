

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 2023 is loading
"""
import sys
# import libraries here
import time
import random
from time import sleep

time_to_sleep = 2

print("\nWelcome to the InfoTech Center 2023\n")
time.sleep(time_to_sleep)

# add code to have ellipsis add a dot ever.5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r print a carriage return first so, message is printed on top of the past line
    time.sleep(2.1)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOPERATING SYSTEM LOADING DONE - SCANNED - WELCOME ")



print("*****************************************************")
print("looking at gas levels\n")



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


print("\n****************************")
print("Weather Branch")
#import libraries
import random
from time import sleep
#Creat function that can chooses weather
def nymbus():
    weatherForcast = ["snow","blizzard","rain","foggy","windy","icy","sunny","cloudy"]
    weathercondition = random.choice(weatherForcast)
    return weathercondition

# Varibele to call the nymbus() when it is in or Vehicle Response System or VRS
weatherAlert = nymbus()
# VRS() will let the car respond to the weather
def VRS():
    if weatherAlert == "snow":
        print("NWS Has updated your alarm for 45min do to the forcast of ",weatherAlert)
        print("VRS Has been Engaged drive max of 30 MPH")
    elif weatherAlert == "blizzard":
        print("NWS Has updated your alarm for 2hours do to the forcast of ",weatherAlert)
        print("VRS Has been Engaged drive max of 20 MPH")
    elif weatherAlert == "rain":
        print("NWS Has updated your alarm for 20min do to the forcast of ",weatherAlert)
        print("VRS Has been Engaged drive max of 40 MPH")
    elif weatherAlert == "foggy":
        print("NWS Has updated your alarm for 30min do to the forcast of ",weatherAlert)
        print("VRS Has been Engaged drive max of 20 MPH")
    elif weatherAlert == "windy":
        print("NWS Has updated your alarm for 10min do to the forcast of ",weatherAlert)
        print("VRS Has been Engaged drive max of 50 MPH")
    elif weatherAlert == "icy":
        print("NWS Has updated your alarm for 1hour do to the forcast of ",weatherAlert)
        print("VRS Has been Engaged drive max of 20 MPH")
    elif weatherAlert == "sunny":
        print("NWS Has updated your alarm 10min do to the forcast of",weatherAlert)
        print("VRS Has been Engaged drive max of 65 MPH")
    else:
        print("NWS Has updated your alarm for 5min do to the forcast of",weatherAlert)
        print("VRS Has been Engaged drive max of 70 MPH")
VRS()

