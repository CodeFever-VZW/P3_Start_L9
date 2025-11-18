"""
Leerkracht - Subklasse van Karakter.
Demonstreert overerving en method overriding.
"""
from models.karakter import Karakter
from config import COLORS


class Leerkracht(Karakter):
    """
    Leerkracht klasse - erft van Karakter.
    Dit is een SUBKLASSE: erft alles van Karakter, maar kan aanpassen en uitbreiden.
    """
    
    def __init__(self, naam: str, leeftijd: int, vak: str, x_tile: int, y_tile: int, dialoog: str):
        """
        Initialiseer een leerkracht.
        We gebruiken super().__init__() om de parent constructor aan te roepen.
        """
        super().__init__(naam, leeftijd, x_tile, y_tile, COLORS["blauw"], dialoog)
        self.vak = vak  # Extra attribuut specifiek voor Leerkracht
    
    
    def beschrijf(self) -> str:
        """
        Overschreven beschrijving voor leerkracht.
        METHOD OVERRIDING: we vervangen de parent methode en hergebruiken deze met super().
        """
        # TODO Oefening 1: Roep super().beschrijf() aan en voeg vakinformatie toe
        pass

