"""
Leerling - Subklasse van Karakter.
Demonstreert overerving en method overriding.
"""
from models.karakter import Karakter
from config import COLORS
import random


class Leerling(Karakter):
    """
    Leerling klasse - erft van Karakter.
    Dit is nog een SUBKLASSE: net als Leerkracht, maar met eigen uniek gedrag.
    """
    
    def __init__(self, naam: str, leeftijd: int, klas: str, x_tile: int, y_tile: int, dialoog: str):
        """
        Initialiseer een leerling.
        Ook hier gebruiken we super().__init__() voor code hergebruik.
        """
        # TODO Oefening 2a: Roep super().__init__() aan met COLORS["groen"] en sla klas op
        pass


    def beschrijf(self) -> str:
        """
        Overschreven beschrijving voor leerling.
        METHOD OVERRIDING: elke subklasse kan zijn eigen versie hebben.
        """
        # TODO Oefening 2b: Roep super().beschrijf() aan en voeg klasinformatie toe
        pass
    
    
    def verwerk_bericht(self, bericht: str, speler_inventory: list) -> str:
        """
        Verwerk bericht - speelt schaar-steen-papier als deze leerling een spel heeft.
        """
        # TODO Oefening 3: Implementeer schaar-steen-papier als self.spel == "schaar-steen-papier"
        pass

