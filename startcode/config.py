"""
Configuratie voor de RPG. Bevat constanten voor scherm, tiles, FPS en kleuren.
"""

# Basis instellingen
FPS = 60

# Tile instellingen
TILE_SIZE = 40  # pixels per tile

# Map instellingen
MAP_WIDTH = 20  # aantal tiles breed
MAP_HEIGHT = 15   # aantal tiles hoog

# HUD instellingen
HUD_HEIGHT = 70  # pixels voor de HUD onderaan

# Scherm instellingen (automatisch berekend)
SCREEN_WIDTH = MAP_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAP_HEIGHT * TILE_SIZE + HUD_HEIGHT

# Kleuren (R, G, B)
COLORS = {
    "wit": (255, 255, 255),
    "zwart": (0, 0, 0),
    "grijs": (128, 128, 128),
    "donkergrijs": (64, 64, 64),
    "lichtgrijs": (192, 192, 192),
    "groen": (50, 200, 50),
    "blauw": (100, 150, 255),
    "rood": (255, 100, 100),
    "geel": (255, 255, 100),
}

