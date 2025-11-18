"""
Karakter - Superklasse voor alle personages in het spel.
Demonstreert basis voor overerving.
"""
import pygame
from config import TILE_SIZE, COLORS


class Karakter:
    """
    Basisklasse voor alle karakters (speler en NPCs).
    Dit is de SUPERKLASSE: gemeenschappelijke eigenschappen en methoden komen hier.
    """
    
    def __init__(self, naam: str, leeftijd: int, x_tile: int, y_tile: int, kleur: tuple[int, int, int], dialoog: str):
        """
        Initialiseer een karakter.
        
        Args:
            naam: Naam van het karakter
            leeftijd: Leeftijd van het karakter
            x_tile: X-positie in tiles (kolom)
            y_tile: Y-positie in tiles (rij)
            kleur: RGB kleur tuple
            dialoog: Dialoog voor dit karakter
        """
        self.naam = naam
        self.leeftijd = leeftijd
        self.x_tile = x_tile
        self.y_tile = y_tile
        self.kleur = kleur
        self.dialoog = dialoog
        self.inventory = []  # Simpel inventory systeem


    def beschrijf(self) -> str:
        """
        Geef een tekstuele beschrijving van dit karakter.
        Subklassen kunnen hun eigen beschrijving definiëren.
        """
        return f"{self.naam} ({self.leeftijd} jaar)"


    def interact(self) -> str:
        """
        Standaard interactie voor een karakter.
        Returnt de dialoog van dit karakter.
        """
        return self.dialoog

    
    def verwerk_bericht(self, bericht: str, speler_inventory: list) -> str:
        """
        Verwerk een getypt bericht en geef een reactie terug.
        Dit is de basis implementatie die gewoon echo't.
        Subklassen kunnen hun eigen reactie implementeren.
        
        Args:
            bericht: Het getypte bericht
            speler_inventory: De inventory van de speler
            
        Returns:
            De reactie van het karakter
        """
        return f"{self.naam} echo't: {bericht}"


    def teken(self, scherm: pygame.Surface):
        """
        Teken dit karakter op het scherm.
        """
        # Bereken pixel positie
        x_px = self.x_tile * TILE_SIZE
        y_px = self.y_tile * TILE_SIZE
        
        # Teken karakter als rechthoek
        rect = pygame.Rect(x_px, y_px, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(scherm, self.kleur, rect)
        pygame.draw.rect(scherm, COLORS["zwart"], rect, 2)  # Rand
        
        # Teken naam label
        font = pygame.font.Font(None, 14)
        tekst = font.render(self.naam[:5], True, COLORS["zwart"])
        tekst_rect = tekst.get_rect(center=(x_px + TILE_SIZE // 2, y_px + TILE_SIZE // 2))
        scherm.blit(tekst, tekst_rect)


    def beweeg(self, dx: int, dy: int):
        """
        Beweeg het karakter met delta tiles.
        
        Args:
            dx: Verandering in x-richting (tiles)
            dy: Verandering in y-richting (tiles)
        """
        self.x_tile += dx
        self.y_tile += dy

