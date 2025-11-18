"""
TileMap - Beheert de spelwereld als een grid van tiles.
"""
import pygame
from config import TILE_SIZE, COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, HUD_HEIGHT, MAP_HEIGHT


class TileMap:
    """
    Simpele grid-based tilemap voor het spel.
    
    # Dit is een helper klasse voor het beheren van de spelwereld en collision detection.
    # 0 = vloer (bewandelbaar)
    # 1 = muur (blokkeert beweging)
    """
    
    def __init__(self, breedte: int, hoogte: int):
        self.breedte = breedte
        self.hoogte = hoogte
        self.tiles = self._maak_kaart()

    
    def _maak_kaart(self) -> list[list[int]]:
        """
        Maak een kaart met klaslokaal en turnzaal.
        
        Returns:
            2D lijst met tile codes
        """
        # Maak lege kaart (allemaal vloer)
        tiles = [[0 for _ in range(self.breedte)] for _ in range(self.hoogte)]
        
        # Plaats muren aan de randen
        for x in range(self.breedte):
            tiles[0][x] = 1  # Bovenkant
            tiles[self.hoogte - 1][x] = 1  # Onderkant
        
        for y in range(self.hoogte):
            tiles[y][0] = 1  # Linkerkant
            tiles[y][self.breedte - 1] = 1  # Rechterkant
        
        # Klaslokaal muren (linksboven)
        for y in range(1, 7):
            tiles[y][6] = 1  # Rechtermuur klaslokaal
        for x in range(1, 7):
            tiles[6][x] = 1  # Ondermuur klaslokaal
        tiles[6][5] = 0  # Deur uit klaslokaal
        
        # Turnzaal muren (rechtsonder)  
        for y in range(11, self.hoogte - 1):
            tiles[y][16] = 1  # Linkermuur turnzaal
        for x in range(16, self.breedte - 1):
            tiles[11][x] = 1  # Bovenmuur turnzaal
        tiles[11][17] = 0  # Deur naar turnzaal
        
        return tiles
    
    def is_blokkade(self, x_tile: int, y_tile: int) -> bool:
        """
        Check of een tile een blokkade bevat (niet bewandelbaar).
        
        Args:
            x_tile: X-positie in tiles
            y_tile: Y-positie in tiles
        
        Returns:
            True als de tile geblokkeerd is, anders False
        """
        # Buiten de kaart = geblokkeerd
        if x_tile < 0 or x_tile >= self.breedte:
            return True
        if y_tile < 0 or y_tile >= self.hoogte:
            return True
        
        # Check of tile een muur is (code 1)
        return self.tiles[y_tile][x_tile] == 1
    

    def teken(self, scherm: pygame.Surface, bericht: str = "", is_typing: bool = False, input_text: str = "", inventory: list = None):
        """
        Teken de tilemap en HUD op het scherm.
        
        Args:
            scherm: Pygame scherm surface
            bericht: Bericht om in de HUD te tonen
            is_typing: Of de speler aan het typen is
            input_text: De huidige input tekst
            inventory: De inventory lijst van de speler
        """
        if inventory is None:
            inventory = []
        # Teken tiles
        for y in range(self.hoogte):
            for x in range(self.breedte):
                # Bereken pixel positie
                x_px = x * TILE_SIZE
                y_px = y * TILE_SIZE
                
                # Bepaal kleur op basis van tile type
                tile_code = self.tiles[y][x]
                if tile_code == 0:
                    kleur = COLORS["wit"]  # Vloer
                elif tile_code == 1:
                    kleur = COLORS["donkergrijs"]  # Muur
                else:
                    kleur = COLORS["grijs"]  # Onbekend
                
                # Teken tile
                rect = pygame.Rect(x_px, y_px, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(scherm, kleur, rect)
        
        # Teken HUD onderaan
        self._teken_hud(scherm, bericht, inventory)
        
        # Teken input veld als aan het typen
        if is_typing:
            self._teken_input_veld(scherm, input_text)
    

    def _teken_hud(self, scherm: pygame.Surface, bericht: str, inventory: list):
        """
        Teken de HUD (Heads-Up Display) onderaan het scherm.
        
        Args:
            scherm: Pygame scherm surface
            bericht: Het bericht dat getoond moet worden
            inventory: De inventory lijst van de speler
        """
        # Fonts
        font = pygame.font.Font(None, 24)
        klein_font = pygame.font.Font(None, 18)
        
        # HUD onderaan het scherm
        hud_y = SCREEN_HEIGHT - HUD_HEIGHT
        hud_rect = pygame.Rect(0, hud_y, SCREEN_WIDTH, HUD_HEIGHT)
        pygame.draw.rect(scherm, COLORS["zwart"], hud_rect)
        
        # Bericht tekst
        tekst = font.render(bericht, True, COLORS["wit"])
        scherm.blit(tekst, (10, hud_y + 15))
        
        # Inventory tekst
        if inventory:
            inv_tekst = klein_font.render(f"Inventory: {', '.join(inventory)}", True, COLORS["geel"])
        else:
            inv_tekst = klein_font.render("Inventory: leeg", True, COLORS["grijs"])
        scherm.blit(inv_tekst, (10, hud_y + 45))
        
        # Instructies rechts
        instructie = klein_font.render("Pijltjes: bewegen | E: praten | T: typen", True, COLORS["grijs"])
        scherm.blit(instructie, (SCREEN_WIDTH - 280, hud_y + 45))


    def _teken_input_veld(self, scherm: pygame.Surface, input_text: str):
        """
        Teken het tekst-input veld onderaan het scherm.
        
        Args:
            scherm: Pygame scherm surface
            input_text: De huidige input tekst
        """
        # Bereken positie onderaan het scherm (na de tilemap)
        y_positie = MAP_HEIGHT * TILE_SIZE
        
        # Achtergrond voor input veld
        input_rect = pygame.Rect(10, y_positie + 10, SCREEN_WIDTH - 20, 30)
        pygame.draw.rect(scherm, COLORS["lichtgrijs"], input_rect)
        pygame.draw.rect(scherm, COLORS["zwart"], input_rect, 2)
        
        # Teken de ingevoerde tekst met cursor
        font = pygame.font.Font(None, 24)
        tekst_surface = font.render(f"> {input_text}_", True, COLORS["zwart"])
        scherm.blit(tekst_surface, (input_rect.x + 5, input_rect.y + 5))
