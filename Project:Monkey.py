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
