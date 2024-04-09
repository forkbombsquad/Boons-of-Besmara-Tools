from Models.NPC import NPC, Book
from Models.SiegeWeapon import SiegeLocation, SiegeWeapon
from Models.Ship import ShipType, Ship
from Models.ShipModule import ShipModule, AreaOfEffect

PLAYER_LEVEL_OPTIONS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
PLAYER_COUNT_OPTIONS = [1, 2, 3, 4, 5, 6, 7, 8]


NPCs = [
    NPC(name="Palace Guard", book=Book.GM_GUIDE, page=206, level=4),
    NPC(name="Burglar", book=Book.GM_GUIDE, page=210, level=4),
    NPC(name="Zealot of Asmodeus", book=Book.GM_GUIDE, page=213, level=4),
    NPC(name="Guide", book=Book.GM_GUIDE, page=217, level=4),
    NPC(name="Bounty Hunter", book=Book.GM_GUIDE, page=227, level=4),
    NPC(name="False Priest", book=Book.GM_GUIDE, page=229, level=4),
    NPC(name="Beast Tamer", book=Book.GM_GUIDE, page=237, level=4),
    NPC(name="Mastermind", book=Book.GM_GUIDE, page=246, level=4)
]

BOMBARD = SiegeWeapon(name="Bombard", location=[SiegeLocation.BOW, SiegeLocation.STERN], damage="4d10", missMin=1, missMax=10,
            attackArea="360", minRange=3, maxRange=12, actions=7, cost=300),
BALLISTA = SiegeWeapon(name="Ballista", location=[SiegeLocation.BOW, SiegeLocation.STERN, SiegeLocation.BROADSIDE], damage="4d12",
            missMin=1, missMax=2, attackArea="45", minRange=0, maxRange=4, actions=6, cost=320),
CATAPULT = SiegeWeapon(name="Catapult", location=[SiegeLocation.BOW], damage="5d10", missMin=0, missMax=0, attackArea="Straight",
            minRange=5, maxRange=5, actions=7, cost=650),
MORTAR = SiegeWeapon(name="Mortar", location=[SiegeLocation.STERN], damage="5d10", missMin=1, missMax=4, attackArea="360",
            minRange=3, maxRange=10, actions=9, cost=720),
CANNON = SiegeWeapon(name="Cannon", location=[SiegeLocation.BROADSIDE], damage="6d12", missMin=1, missMax=5, attackArea="45",
            minRange=0, maxRange=6, actions=8, cost=900),
HEAVY_BALLISTA = SiegeWeapon(name="Heavy Ballista", location=[SiegeLocation.BOW, SiegeLocation.STERN], damage="7d12", missMin=1,
            missMax=2, attackArea="45", minRange=3, maxRange=7, actions=9, cost=900),
FIREDRAKE = SiegeWeapon(name="Firedrake", location=[SiegeLocation.BOW], damage="8d6 Fire", missMin=0, missMax=0,
            attackArea="Straight or exactly 45", minRange=0, maxRange=5, actions=9, cost=1000),
HEAVY_BOMBARD = SiegeWeapon(name="Heavy Bombard", location=[SiegeLocation.BOW, SiegeLocation.STERN], damage="7d10", missMin=1,
            missMax=4, attackArea="360", minRange=3, maxRange=10, actions=10, cost=1400),
TREBUCHET = SiegeWeapon(name="Trebuchet", location=[SiegeLocation.STERN], damage="8d10", missMin=0, missMax=0,
            attackArea="Straight (Forward or Backward)", minRange=5, maxRange=7, actions=9, cost=2000),
ALKENSTAR_CANNON = SiegeWeapon(name="Alkenstar Cannon", location=[SiegeLocation.BROADSIDE], damage="10d12", missMin=1, missMax=5,
            attackArea="45", minRange=0, maxRange=10, actions=14, cost=12000)

BOW_SIEGE_WEAPONS = [
    BOMBARD, BALLISTA, HEAVY_BALLISTA, FIREDRAKE, HEAVY_BOMBARD
]

STERN_SIEGE_WEAPONS = [
    BOMBARD, BALLISTA, MORTAR, HEAVY_BALLISTA, HEAVY_BOMBARD, TREBUCHET
]

BROADSIDE_SIEGE_WEAPONS = [
    BALLISTA, CANNON, ALKENSTAR_CANNON
]

ROWBOAT_BASE = Ship(shipType=ShipType.ROWBOAT, minSpeed=1, maxSpeed=1, acceleration=1, hp=20, fireWeakness=10, minCrew=1, maxCrew=4, moduleCapacity=0, plunderCapacity=2, broadsideCapacity=0, bowCapacity=0, sternCapacity=0)
LONGBOAT_BASE = Ship(shipType=ShipType.LONGBOAT, minSpeed=1, maxSpeed=1, acceleration=1, hp=40, fireWeakness=10, minCrew=2, maxCrew=12, moduleCapacity=2, plunderCapacity=6, broadsideCapacity=0, bowCapacity=0, sternCapacity=0)
SLOOP_BASE = Ship(shipType=ShipType.SLOOP, minSpeed=2, maxSpeed=6, acceleration=4, hp=150, fireWeakness=15, minCrew=3, maxCrew=12, moduleCapacity=4, plunderCapacity=18, broadsideCapacity=2, bowCapacity=1, sternCapacity=0)
SCHOONER_BASE = Ship(shipType=ShipType.SCHOONER, minSpeed=2, maxSpeed=7, acceleration=3, hp=200, fireWeakness=10, minCrew=4, maxCrew=16, moduleCapacity=10, plunderCapacity=20, broadsideCapacity=6, bowCapacity=1, sternCapacity=2)
BRIGANTINE_BASE = Ship(shipType=ShipType.BRIGANTINE, minSpeed=2, maxSpeed=7, acceleration=2, hp=200, fireWeakness=10, minCrew=5, maxCrew=20, moduleCapacity=16, plunderCapacity=30, broadsideCapacity=8, bowCapacity=2, sternCapacity=2)
SQUARE_RIGGED_BASE = Ship(shipType=ShipType.SQUARE_RIGGED, minSpeed=2, maxSpeed=8, acceleration=1, hp=300, fireWeakness=20, minCrew=10, maxCrew=40, moduleCapacity=30, plunderCapacity=100, broadsideCapacity=12, bowCapacity=3, sternCapacity=4)
GALLEON_BASE = Ship(shipType=ShipType.GALLEON, minSpeed=1, maxSpeed=9, acceleration=1, hp=500, fireWeakness=20, minCrew=10, maxCrew=50, moduleCapacity=50, plunderCapacity=80, broadsideCapacity=16, bowCapacity=4, sternCapacity=6)
SHIP_OF_THE_LINE_BASE = Ship(shipType=ShipType.SHIP_OF_THE_LINE, minSpeed=0, maxSpeed=10, acceleration=1, hp=700, fireWeakness=20, minCrew=10, maxCrew=80, moduleCapacity=100, plunderCapacity=150, broadsideCapacity=20, bowCapacity=5, sternCapacity=6)
MAN_O_WAR_BASE = Ship(shipType=ShipType.MAN_O_WAR, minSpeed=0, maxSpeed=12, acceleration=1, hp=1000, fireWeakness=30, minCrew=20, maxCrew=150, moduleCapacity=150, plunderCapacity=300, broadsideCapacity=40, bowCapacity=7, sternCapacity=10)

ShipBases = [
   SLOOP_BASE, SCHOONER_BASE, BRIGANTINE_BASE, SQUARE_RIGGED_BASE, GALLEON_BASE, SHIP_OF_THE_LINE_BASE, MAN_O_WAR_BASE
]

ARMOR_PLATING = ShipModule(name="Armor Plating", areaOfEffect=AreaOfEffect.HP, size=1, cost=100, limit=0, id=1)
CREW_CABINS = ShipModule(name="Crew Cabins", areaOfEffect=AreaOfEffect.CREW, size=1, cost=100, limit=0, id=2)
PLUNDER_CHESTS = ShipModule(name="Plunder Chests", areaOfEffect=AreaOfEffect.PLUNDER, size=1, cost=100, limit=0, id=3)
MUNITION_CRATES = ShipModule(name="Munition Crates", areaOfEffect=AreaOfEffect.NONE, size=1, cost=100, limit=0, id=4)
BLACK_POWDER_BARRELS = ShipModule(name="Black Powder Barrels", areaOfEffect=AreaOfEffect.NONE, size=1, cost=100, limit=0, id=5)
FOOD_CRATES = ShipModule(name="Food Crates", areaOfEffect=AreaOfEffect.NONE, size=1, cost=50, limit=0, id=6)
WORKSHOP = ShipModule(name="Workshop", areaOfEffect=AreaOfEffect.NONE, size=2, cost=100, limit=0, id=7)
LIBRARY = ShipModule(name="Library", areaOfEffect=AreaOfEffect.NONE, size=2, cost=500, limit=0, id=9)
BACKUP_RUDDERS = ShipModule(name="Backup Rudders", areaOfEffect=AreaOfEffect.SPEED, size=5, cost=500, limit=1, id=10)
FIREPROOFING = ShipModule(name="Fireproofing", areaOfEffect=AreaOfEffect.FIRE, size=5, cost=5000, limit=2, id=11)
BROADSIDE_GUNPORT = ShipModule(name="Broadside Gunport", areaOfEffect=AreaOfEffect.BROADSIDE, size=5, cost=500, limit=0, id=12)
BOW_GUNPORT = ShipModule(name="Bow Gunport", areaOfEffect=AreaOfEffect.BOW, size=5, cost=2000, limit=0, id=13)
STERN_GUNPORT = ShipModule(name="Stern Gunport", areaOfEffect=AreaOfEffect.STERN, size=5, cost=1000, limit=0, id=14)
HYDRODYNAMIC_FINS = ShipModule(name="Hydrodynamic Fins", areaOfEffect=AreaOfEffect.ACCELERATION, size=10, cost=1000, limit=1, id=15)

Modules = [
    ARMOR_PLATING, CREW_CABINS, PLUNDER_CHESTS, MUNITION_CRATES, BLACK_POWDER_BARRELS, FOOD_CRATES, WORKSHOP, LIBRARY, BACKUP_RUDDERS, FIREPROOFING, BROADSIDE_GUNPORT, BOW_GUNPORT, STERN_GUNPORT, HYDRODYNAMIC_FINS
]