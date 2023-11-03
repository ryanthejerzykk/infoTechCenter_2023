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
   