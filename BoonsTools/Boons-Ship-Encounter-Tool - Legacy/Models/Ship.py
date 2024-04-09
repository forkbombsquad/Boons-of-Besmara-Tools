from enum import StrEnum

class ShipType(StrEnum):
    ROWBOAT = "Rowboat"
    LONGBOAT = "Longboat"
    SLOOP = "Sloop"
    SCHOONER = "Schooner"
    BRIGANTINE = "Brigantine"
    SQUARE_RIGGED = "Square-Rigged"
    GALLEON = "Galleon"
    SHIP_OF_THE_LINE = "Ship of the Line"
    MAN_O_WAR = "Man-O'-War"


class Ship:
    def __init__(self, shipType: ShipType, minSpeed: int, maxSpeed: int, acceleration: int, hp: int, fireWeakness: int, minCrew: int, maxCrew: int, moduleCapacity: int, plunderCapacity: int, broadsideCapacity: int, bowCapacity: int, sternCapacity: int):
        self.shipType = shipType
        self.level = getShipLevel(shipType)
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
        self.acceleration = acceleration
        self.hp = hp
        self.fireWeakness = fireWeakness
        self.minCrew = minCrew
        self.maxCrew = maxCrew
        self.moduleCapacity = moduleCapacity
        self.plunderCapacity = plunderCapacity
        self.broadsideCapacity = broadsideCapacity
        self.bowCapacity = bowCapacity
        self.sternCapacity = sternCapacity


def getShipLevel(shipType: ShipType) -> int:
    match shipType:
        case ShipType.ROWBOAT:
            return 0
        case ShipType.LONGBOAT:
            return 0
        case ShipType.SLOOP:
            return 1
        case ShipType.SCHOONER:
            return 2
        case ShipType.BRIGANTINE:
            return 3
        case ShipType.SQUARE_RIGGED:
            return 7
        case ShipType.GALLEON:
            return 9
        case ShipType.SHIP_OF_THE_LINE:
            return 10
        case ShipType.MAN_O_WAR:
            return 13
