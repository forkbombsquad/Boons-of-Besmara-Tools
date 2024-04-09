from enum import Enum


class AreaOfEffect(Enum):
    HP = 1
    CREW = 2
    PLUNDER = 3
    NONE = 4
    SPEED = 5
    FIRE = 6
    BROADSIDE = 7
    BOW = 8
    STERN = 9
    ACCELERATION = 10

class ShipModule:
    def __init__(self, name: str, areaOfEffect: AreaOfEffect, size: int, cost: int, limit: int, id: int):
        self.name = name
        self.areaOfEffect = areaOfEffect
        self.value = getModuleValue(areaOfEffect)
        self.size = size
        self.cost = cost
        self.limit = limit
        self.id = id



def getModuleValue(aoo: AreaOfEffect) -> int:
    match aoo:
        case AreaOfEffect.HP:
            return 10
        case AreaOfEffect.CREW:
            return 2
        case AreaOfEffect.PLUNDER:
            return 2
        case AreaOfEffect.NONE:
            return 0
        case AreaOfEffect.SPEED:
            return 0
        case AreaOfEffect.FIRE:
            return 0
        case AreaOfEffect.BROADSIDE:
            return 1
        case AreaOfEffect.BOW:
            return 1
        case AreaOfEffect.STERN:
            return 1
        case AreaOfEffect.ACCELERATION:
            return 1