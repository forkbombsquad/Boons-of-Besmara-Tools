from random import randint
import Constants
from Models.Ship import Ship
from Models.ShipModule import ShipModule, AreaOfEffect
from Models.NPC import NPC
from Models.Plunder import PlunderType, Plunder
from Models.SiegeWeapon import SiegeWeapon

def r(min_val: int, max_val: int) -> int:
    if max_val == min_val:
        return max_val
    return randint(min_val, max_val)

class ShipInstance:
    def __init__(self, baseShip: Ship, maxCrewLevel: int, minCrewLevel: int):
        self.baseShip = baseShip

        # Set Base Numbers
        self.shipType = baseShip.shipType
        self.minSpeed = baseShip.minSpeed
        self.maxSpeed = baseShip.maxSpeed
        self.level = baseShip.level
        self.acceleration = baseShip.acceleration
        self.hp = baseShip.hp
        self.fireWeakness = baseShip.fireWeakness
        self.minCrew = baseShip.minCrew
        self.maxCrew = baseShip.maxCrew
        self.moduleCapacity = baseShip.moduleCapacity
        self.plunderCapacity = baseShip.plunderCapacity
        self.broadsideCapacity = baseShip.broadsideCapacity
        self.bowCapacity = baseShip.bowCapacity
        self.sternCapacity = baseShip.sternCapacity

        # Generate Stuff
        b = baseShip
        self.modules = generateModules(b.moduleCapacity)

        for mod in self.modules:
            match mod.areaOfEffect:
                case AreaOfEffect.HP:
                    self.hp += mod.value
                case AreaOfEffect.CREW:
                    self.minCrew += mod.value
                    self.maxCrew += mod.value
                case AreaOfEffect.PLUNDER:
                    self.plunderCapacity += mod.value
                case AreaOfEffect.NONE:
                    break
                case AreaOfEffect.SPEED:
                    break
                case AreaOfEffect.FIRE:
                    if self.fireWeakness == baseShip.fireWeakness:
                        self.fireWeakness = baseShip.fireWeakness / 2
                    else:
                        self.fireWeakness = 0
                case AreaOfEffect.BROADSIDE:
                    self.broadsideCapacity += mod.value
                case AreaOfEffect.BOW:
                    self.bowCapacity += mod.value
                case AreaOfEffect.STERN:
                    self.sternCapacity += mod.value
                case AreaOfEffect.ACCELERATION:
                    self.acceleration += mod.value

        self.crew = generateCrew(crewSize=r(self.minCrew, self.maxCrew), maxLevel=maxCrewLevel, minLevel=minCrewLevel)
        self.plunder = generatePlunder(r(0, self.plunderCapacity))
        self.broadsideWeapons = generateBroadsides(self.broadsideCapacity)
        self.bowWeapons = generateBow(self.bowCapacity)
        self.sternWeapons = generateStern(self.sternCapacity)


    def print(self) -> str:
        s = "  "
        return f"{self.shipType}\n" \
               f"{s}Speed {self.minSpeed}-{self.maxSpeed} ({self.acceleration}acc)\n" \
               f"{s}HP {self.hp}\n" \
               f"{s}Crew {self.getCrewCount()}\n" \
               f"{self.getCrewString(s + s)}" \
               f"{s}Siege Weapons (Actions {self.getCrewCount() * 3})\n" \
               f"{s}{s}Broadsides\n" \
               f"{self.getBroadsidesString(s + s + s, s)}" \
               f"{s}{s}Bow\n" \
               f"{self.getBowsString(s + s + s, s)}" \
               f"{s}{s}Stern\n" \
               f"{self.getSternsString(s + s + s, s)}" \
               f"{s}Plunder\n" \
               f"{self.getPlunderString(s + s)}"

    def getPlunderString(self, depth: str) -> str:
        plunderString = ""
        coppers = 0
        silvers = 0
        golds = 0
        plats = 0
        for p in self.plunder:
            match p.type:
                case PlunderType.COPPER:
                    coppers += 1
                case PlunderType.SILVER:
                    silvers += 1
                case PlunderType.GOLD:
                    golds += 1
                case PlunderType.PLATINUM:
                    plats += 1

        if coppers > 0 or silvers > 0 or golds > 0 or plats > 0:
            plunderString += f"{depth}"
            if coppers > 0:
                plunderString += f"{coppers}C  "
            if silvers > 0:
                plunderString += f"{silvers}S  "
            if golds > 0:
                plunderString += f"{golds}G  "
            if plats > 0:
                plunderString += f"{plats}P  "
            plunderString += "\n"
        else:
            plunderString += f"{depth}None\n"

        return plunderString

    def getCrewCount(self) -> int:
        count = 0
        for c, cnt in self.crew.items():
            count += cnt

        return count
    def getCrewString(self, depth: str) -> str:
        crewString = ""
        for c, num in self.crew.items():
            crewString += f"{depth}{num} {c.name} L{c.level} ({c.book} p{c.page})\n"
        return crewString

    def getBroadsidesString(self, depth: str, space: str) -> str:
        if len(self.broadsideWeapons) == 0:
            return f"{depth}None\n"
        broadsideString = ""
        weapons = {}
        for weapon in self.broadsideWeapons:
            if not weapon in weapons:
                weapons[weapon] = 1
            else:
                weapons[weapon] += 1

        for w, count in weapons.items():
            if isinstance(w, SiegeWeapon):
                weapon = w
            else:
                weapon = w[0]
            broadsideString += f"{depth}{count} {weapon.name}\n" \
                               f"{depth}{space}{weapon.attackArea}, {weapon.minRange}-{weapon.maxRange} hexes\n" \
                               f"{depth}{space}{weapon.damage} (miss {weapon.missMin}-{weapon.missMax})\n"

        return broadsideString

    def getBowsString(self, depth: str, space: str) -> str:
        if len(self.bowWeapons) == 0:
            return f"{depth}None\n"
        broadsideString = ""
        weapons = {}
        for weapon in self.bowWeapons:
            if not weapon in weapons:
                weapons[weapon] = 1
            else:
                weapons[weapon] += 1

        for w, count in weapons.items():
            if isinstance(w, SiegeWeapon):
                weapon = w
            else:
                weapon = w[0]
            broadsideString += f"{depth}{count} {weapon.name}\n" \
                               f"{depth}{space}{weapon.attackArea}, {weapon.minRange}-{weapon.maxRange} hexes\n" \
                               f"{depth}{space}{weapon.damage} (miss {weapon.missMin}-{weapon.missMax})\n"

        return broadsideString

    def getSternsString(self, depth: str, space: str) -> str:
        if len(self.sternWeapons) == 0:
            return f"{depth}None\n"
        broadsideString = ""
        weapons = {}
        for weapon in self.sternWeapons:
            if not weapon in weapons:
                weapons[weapon] = 1
            else:
                weapons[weapon] += 1

        for w, count in weapons.items():
            if isinstance(w, SiegeWeapon):
                weapon = w
            else:
                weapon = w[0]
            broadsideString += f"{depth}{count} {weapon.name}\n" \
                               f"{depth}{space}{weapon.attackArea}, {weapon.minRange}-{weapon.maxRange} hexes\n" \
                               f"{depth}{space}{weapon.damage} (miss {weapon.missMin}-{weapon.missMax})\n"

        return broadsideString

def generateBroadsides(capacity: int) -> [SiegeWeapon]:
    if capacity == 0:
        return []
    siegeWeapons = []
    total = r(1, capacity)
    count = 0
    while count < total:
        siegeWeapons.append(Constants.BROADSIDE_SIEGE_WEAPONS[r(0, len(Constants.BROADSIDE_SIEGE_WEAPONS) - 1)])
        count += 1
    return siegeWeapons

def generateBow(capacity: int) -> [SiegeWeapon]:
    if capacity == 0:
        return []
    siegeWeapons = []
    total = r(1, capacity)
    count = 0
    while count < total:
        siegeWeapons.append(Constants.BOW_SIEGE_WEAPONS[r(0, len(Constants.BOW_SIEGE_WEAPONS) - 1)])
        count += 1
    return siegeWeapons

def generateStern(capacity: int) -> [SiegeWeapon]:
    if capacity == 0:
        return []
    siegeWeapons = []
    total = r(1, capacity)
    count = 0
    while count < total:
        siegeWeapons.append(Constants.STERN_SIEGE_WEAPONS[r(0, len(Constants.STERN_SIEGE_WEAPONS) - 1)])
        count += 1
    return siegeWeapons
def generateCrew(crewSize: int, maxLevel: int, minLevel: int):
    npcs = list(filter(lambda var: filterOutNpcLevels(var, minLevel, maxLevel), Constants.NPCs))
    chosenNpcs = {}
    currentCount = 0
    while currentCount < crewSize:
        npc = npcs[r(0, len(npcs) - 1)]
        if not npc in chosenNpcs:
            chosenNpcs[npc] = 1
        else:
            chosenNpcs[npc] += 1
        currentCount += 1
    return chosenNpcs

def generatePlunder(plunderAmount: int) -> [Plunder]:
    currentPlunder = 0
    plunder = []

    # Copper
    copperCount = r(0, plunderAmount)
    currentPlunder += copperCount
    counter = 0
    while counter < copperCount:
        plunder.append(Plunder(PlunderType.COPPER))
        counter += 1

    #Silver
    silverCount = r(0, plunderAmount - currentPlunder)
    currentPlunder += silverCount
    counter = 0
    while counter < silverCount:
        plunder.append(Plunder(PlunderType.SILVER))
        counter += 1

    #Gold
    goldCount = r(0, plunderAmount - currentPlunder)
    currentPlunder += goldCount
    counter = 0
    while counter < goldCount:
        plunder.append(Plunder(PlunderType.GOLD))
        counter += 1

    #Platinum
    platCount = r(0, plunderAmount - currentPlunder)
    currentPlunder += platCount
    counter = 0
    while counter < platCount:
        plunder.append(Plunder(PlunderType.PLATINUM))
        counter += 1

    return plunder

def generateModules(maxModules: int) -> [ShipModule]:
    modulesToUse = r(0, maxModules)
    currentUsed = 0
    currentMods = []
    while currentUsed < modulesToUse:
        remain = modulesToUse - currentUsed
        availMods = list(filter(lambda var: filterAvailMod(var, remain), Constants.Modules))
        availMods = filterModsAtMax(currentMods, availMods)
        mod = availMods[r(0, len(availMods) - 1)]
        currentMods.append(mod)
        currentUsed += mod.size

    return currentMods

def filterAvailMod(var, m):
    return var.size <= m

def filterModsAtMax(currentMods: [ShipModule], availMods: [ShipModule]) -> [ShipModule]:
    idsToRemove = []
    modCounts = {}
    for mod in currentMods:
        if mod in modCounts:
            modCounts[mod.id] += 1
        else:
            modCounts[mod.id] = 1

    for mod in availMods:
        if mod.id in modCounts:
            if mod.limit > 0:
                if modCounts[mod.id] >= mod.limit:
                    idsToRemove.append(mod.id)

    return list(filter(lambda var: filterOutIdsToRemove(var, idsToRemove), availMods))

def filterOutIdsToRemove(var, idsToRemove: [int]):
    for id in idsToRemove:
        if id == var.id:
            return False
    return True

def filterOutNpcLevels(var: NPC, minLevel, maxLevel):
    return minLevel <= var.level <= maxLevel