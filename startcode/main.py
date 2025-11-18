"""
Main - Hoofdprogramma voor het RPG School spel.
"""
import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLORS, MAP_WIDTH, MAP_HEIGHT
from models.karakter import Karakter
from models.leerkracht import Leerkracht
from models.leerling import Leerling
from models.whiteboard import Whiteboard
from tilemap import TileMap


class Game:
    
    def __init__(self):
        """Initialiseer het spel."""
        pygame.init()
        
        # Scherm setup
        self.scherm = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("RPG School")
        self.klok = pygame.time.Clock()
        
        # Game state
        self.game_bezig = True
        self.bericht = "OH NEE! Iemand tekende met permanente marker op het whiteboard!"
        
        # Text input state
        self.is_typing = False
        self.input_text = ""
        self.typing_target = None  # NPC waarnaar we typen
        
        # Maak tilemap
        self.tilemap = TileMap(MAP_WIDTH, MAP_HEIGHT)
        
        # POLYMORFISME: lijst bevat Karakter objecten (ook Leerkracht & Leerling)
        # Verhaal NPCs met custom dialoog
        
        # Whiteboard object (speciaal - heeft eigen class)
        whiteboard = Whiteboard(2, 1)
        
        self.npcs = [
            # Whiteboard in klaslokaal
            whiteboard,
            
            # OEFENING 1: Uncomment Dirk nadat je Leerkracht.beschrijf() hebt gemaakt
            # Leerkracht("Dirk", 54, "Geschiedenis", 4, 1, 
            #           "Iemand heeft het whiteboard verpest! Kun jij het schoonmaken?"),
            
            # OEFENING 2: Uncomment deze Leerlingen nadat je Leerling class hebt gemaakt
            # Leerling("Warre", 15, "3A", 4, 5,
            #         "Psst! Ik hoorde dat je permanente marker eraf krijgt met deo."),
            
            # Leerling("Sara", 16, "4B", 10, 9,
            #         "Er ligt volgens mij deo in de kleedkamer van de turnzaal!"),
            
            # Leerling("Siebe", 16, "3B", 17, 10,
            #         "Wil je de turnzaal in? Win van mij met schaar-steen-papier! (Typ T)"),
        ]
        
        # Speler start in klaslokaal
        self.speler = Karakter("Jij", 17, 3, 3, COLORS["geel"], "Dat ben jij!")


    def verwerk_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_bezig = False
            
            elif event.type == pygame.KEYDOWN:
                # Als we in typing mode zijn, verwerk tekst input
                if self.is_typing:
                    self.verwerk_typing_input(event)
                else:
                    # Normale game input
                    # Beweging: één stap per toets
                    # dx = verandering in x-richting, dy = verandering in y-richting
                    dx, dy = 0, 0       
                    
                    if event.key == pygame.K_LEFT:
                        dx = -1
                    elif event.key == pygame.K_RIGHT:
                        dx = 1
                    elif event.key == pygame.K_UP:
                        dy = -1
                    elif event.key == pygame.K_DOWN:
                        dy = 1
                    
                    # Beweeg speler als er een verandering is
                    if dx != 0 or dy != 0:
                        self.beweeg_speler(dx, dy)
                    
                    # Interactie met E-toets
                    elif event.key == pygame.K_e:
                        self.probeer_interactie()
                    
                    # Typing mode activeren met T-toets
                    elif event.key == pygame.K_t:
                        self.probeer_typen()


    def probeer_typen(self):
        """Start typing mode met aangrenzende NPC."""
        npc = self.vind_aangrenzende_npc()
        if npc:
            self.typing_target = npc
            self.is_typing = True
            self.input_text = ""


    def verwerk_typing_input(self, event):
        """Verwerk typing input."""
        if event.key == pygame.K_RETURN:
            # POLYMORFISME: elk karakter reageert op eigen manier
            self.bericht = self.typing_target.verwerk_bericht(self.input_text, self.speler.inventory)
            
            self.is_typing = False
            self.typing_target = None
        elif event.key == pygame.K_BACKSPACE:
            self.input_text = self.input_text[:-1]
        elif event.unicode:
            self.input_text += event.unicode


    def beweeg_speler(self, dx: int, dy: int):
        """
        Beweeg de speler als het mogelijk is (geen collision).
        
        Args:
            dx: Verandering in x-richting (tiles)
            dy: Verandering in y-richting (tiles)
        """
        nieuwe_x = self.speler.x_tile + dx
        nieuwe_y = self.speler.y_tile + dy
        
        # Check collision
        if self.tilemap.is_blokkade(nieuwe_x, nieuwe_y):
            self.bericht = "Je kunt niet door muren heen lopen!"
        elif self.is_npc_op_positie(nieuwe_x, nieuwe_y):
            self.bericht = "Je kunt niet door mensen heen lopen!"
        else:
            self.speler.beweeg(dx, dy)


    def is_npc_op_positie(self, x_tile: int, y_tile: int) -> bool:
        """
        Check of er een NPC of object op een bepaalde positie staat; geeft True als dat het geval is.
        """
        for npc in self.npcs:
            if npc.x_tile == x_tile and npc.y_tile == y_tile:
                return True
        return False


    def vind_aangrenzende_npc(self) -> Karakter | None:
        """
        Vind een NPC die naast de speler staat (boven, onder, links, rechts).
        
        Returns:
            Het NPC object, of None als er geen naast staat
        """
        # Check alle vier richtingen
        richtingen = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Boven, Onder, Links, Rechts
        
        for dx, dy in richtingen:
            check_x = self.speler.x_tile + dx
            check_y = self.speler.y_tile + dy
            
            # Check of er een NPC op die positie staat
            for npc in self.npcs:
                if npc.x_tile == check_x and npc.y_tile == check_y:
                    return npc
        
        return None


    def probeer_interactie(self):
        """
        Probeer te interacteren met een aangrenzende NPC.
        
        # POLYMORFISME: Roep interact() aan op een Karakter object, kies juiste versie:
        # Bv. als het een Leerkracht is -> Leerkracht.interact()
        """
        npc = self.vind_aangrenzende_npc()
        
        if npc:
            beschrijving = npc.beschrijf()
            interactie = npc.interact()
            self.bericht = f"{beschrijving}: {interactie}"
        else:
            self.bericht = "Er is niemand om mee te praten. Ga naast iemand staan!"


    def teken(self):
        self.scherm.fill(COLORS["wit"])
        
        self.tilemap.teken(self.scherm, self.bericht, self.is_typing, self.input_text, self.speler.inventory)
        
        # POLYMORFISME: alle NPCs worden op dezelfde manier getekend
        for npc in self.npcs:
            npc.teken(self.scherm)
        
        self.speler.teken(self.scherm)
        
        pygame.display.flip()


    def run(self):
        while self.game_bezig:       # Game loop
            self.verwerk_input()      # 1. Verwerk input
            self.teken()              # 2. Teken alles
            self.klok.tick(FPS)       # 3. Klok tick
        
        pygame.quit()
        sys.exit()


game = Game()
game.run()
