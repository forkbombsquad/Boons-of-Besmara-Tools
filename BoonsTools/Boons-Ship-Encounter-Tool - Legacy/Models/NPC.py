from enum import StrEnum


class Book(StrEnum):
    BESTIARY_1 = "Bestiary 1"
    BESTIARY_2 = "Bestiary 2"
    BESTIARY_3 = "Bestiary 3"
    GM_GUIDE = "GM Guide"


class NPC:
    def __init__(self, name: str, book: Book, page: int, level: int):
        self.name = name
        self.book = book
        self.page = page
        self.level = level
