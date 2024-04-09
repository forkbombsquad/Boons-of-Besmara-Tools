import math

import Constants
from Models.NPC import NPC
from Models.Plunder import Plunder
from Models.Ship import Ship
from Models.ShipInstance import ShipInstance
from Models.ShipModule import ShipModule
from Models.SiegeWeapon import SiegeWeapon
from random import randint


# TWEAKS
MIN_CREW_LEVEL = 2
MAX_CREW_LEVEL = 9
SHIP_MAX_LEVEL = 7
SHIP_MIN_LEVEL = 2

# You may need to adjust this value if it's infinite looping but 4 seems pretty good for now
MAX_NUM_SHIPS = 4




# Helper Funcs
def r(min_val: int, max_val: int) -> int:
    if max_val == min_val:
        return max_val
    return randint(min_val, max_val)

def filterOutShips(var, maxLevel):
    return var.level <= maxLevel

def generateShips(totalShipLevel) -> [ShipInstance]:
    currentShipLevel = 0
    sps = []
    while currentShipLevel < totalShipLevel:
        baseShips = list(filter(lambda var: filterOutShips(var, totalShipLevel - currentShipLevel), Constants.ShipBases))
        ship = baseShips[r(0, len(baseShips) - 1)]
        sps.append(ShipInstance(baseShip=ship, minCrewLevel=MIN_CREW_LEVEL, maxCrewLevel=MAX_CREW_LEVEL))
        currentShipLevel += ship.level
    return sps

# START GENERATION
totalShipLevel = r(SHIP_MIN_LEVEL, SHIP_MAX_LEVEL)

print(f"---------- GENERATOR SETTINGS ----------\n")
print(f"totalShipLevel={totalShipLevel}")
print(f"maxNumShips={MAX_NUM_SHIPS}")
print(f"minCrewLevel={MIN_CREW_LEVEL}")
print(f"maxCrewLevel={MAX_CREW_LEVEL}\n")

ships = []
attempts = 1
while len(ships) == 0 or len(ships) > MAX_NUM_SHIPS:
    print(f"Attempting to Generate Ships... Try #{attempts}")
    ships = generateShips(totalShipLevel)
    attempts += 1


print("================ SHIP ENCOUNTER ================\n")
print(f"{len(ships)} Ships")
for s in ships:
    print("\n")
    print(s.print())