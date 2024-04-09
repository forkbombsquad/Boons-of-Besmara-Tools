from enum import StrEnum


class PlunderType(StrEnum):
    COPPER = "Copper"
    SILVER = "Silver"
    GOLD = "GOLD"
    PLATINUM = "Platinum"

class Plunder:
    def __init__(self, plunderType: PlunderType):
        self.type = plunderType