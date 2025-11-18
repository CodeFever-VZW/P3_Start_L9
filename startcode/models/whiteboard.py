"""
Whiteboard - Een speciaal object in het spel.
"""
import pygame
from models.karakter import Karakter
from config import TILE_SIZE, COLORS


class Whiteboard(Karakter):
    """
    Whiteboard klasse - speciaal object dat schoongemaakt kan worden.
    Erft van Karakter maar gedraagt zich anders (geen dialoog, andere tekening).
    """
    
    def __init__(self, x_tile: int, y_tile: int):
        """Initialiseer het whiteboard."""
        super().__init__("Whiteboard", 0, x_tile, y_tile, COLORS["rood"], "")
        self.is_schoon = False
    
    
    def beschrijf(self) -> str:
        """Beschrijving van het whiteboard."""
        if self.is_schoon:
            return "Schoon whiteboard"
        else:
            return "Vuil whiteboard"
    
    
    def interact(self) -> str:
        """Whiteboard reageert op basis van schoon/vuil status."""
        if self.is_schoon:
            return "Het whiteboard is weer schoon!"
        else:
            return "Een permanente tekening op het whiteboard... oei! (Typ T om te reinigen)"
    
    
    def verwerk_bericht(self, bericht: str, speler_inventory: list) -> str:
        """Probeer het whiteboard schoon te maken."""
        # TODO Oefening 4: Check "reinig" in bericht
        pass
    
    
    def schoon_maken(self):
        """Maak het whiteboard schoon (verander kleur)."""
        # TODO Oefening 4: Zet is_schoon op True en kleur op COLORS["groen"]
        pass
    
    
    def teken(self, scherm: pygame.Surface):
        """Teken het whiteboard - gecentreerd in de tile."""
        # Bereken pixel positie (centrum van tile)
        tile_x = self.x_tile * TILE_SIZE
        tile_y = self.y_tile * TILE_SIZE
        
        # Whiteboard grootte (iets kleiner dan tile voor mooie look)
        breedte = int(TILE_SIZE * 1.1)
        hoogte = int(TILE_SIZE * 0.8)
        
        # Centreer whiteboard in de tile
        x_px = tile_x + (TILE_SIZE - breedte) // 2
        y_px = tile_y
        
        rect = pygame.Rect(x_px, y_px, breedte, hoogte)
        
        # Teken witte achtergrond (het whiteboard zelf)
        pygame.draw.rect(scherm, COLORS["wit"], rect)
        
        # Teken rand (zwart frame)
        pygame.draw.rect(scherm, COLORS["zwart"], rect, 2)
        
        # Bereken centrum voor tekeningen
        cx = x_px + breedte // 2
        cy = y_px + hoogte // 2
        
        # Teken "tekening" relatief aan centrum
        if not self.is_schoon:
            # Krabbels (rode lijnen) - simpel gezichtje
            # Ogen
            pygame.draw.circle(scherm, self.kleur, (cx - 8, cy - 5), 3, 2)
            pygame.draw.circle(scherm, self.kleur, (cx + 8, cy - 5), 3, 2)
            # Mond (lachje)
            pygame.draw.arc(scherm, self.kleur, 
                          (cx - 10, cy - 5, 20, 15), 0, 3.14, 2)
        else:
            # Vinkje (groen) als schoon
            pygame.draw.line(scherm, self.kleur,
                           (cx - 8, cy), (cx - 2, cy + 8), 3)
            pygame.draw.line(scherm, self.kleur,
                           (cx - 2, cy + 8), (cx + 10, cy - 8), 3)

