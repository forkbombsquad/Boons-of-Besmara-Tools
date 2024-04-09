from enum import StrEnum


class SiegeLocation(StrEnum):
    BOW = "Bow"
    STERN = "Stern"
    BROADSIDE = "Broadside"


class SiegeWeapon:
    def __init__(self, name: str, location: [SiegeLocation], damage: str, missMin: int, missMax: int, attackArea: str, minRange: int, maxRange: int, actions: int, cost: int):
        self.name = name
        self.location = location
        self.damage = damage
        self.missMin = missMin
        self.missMax = missMax
        self.attackArea = attackArea
        self.minRange = minRange
        self.maxRange = maxRange
        self.actions = actions
        self.cost = cost


