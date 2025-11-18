# RPG School - Overerving in Python met Pygame

Een educatief Pygame-project dat **Object-Oriented Programming (OOP)** concepten demonstreert, met focus op **overerving**, **polymorfisme** en **method overriding**.

---

## 🚀 Installatie

```bash
pip install pygame
```

---

## 📚 Leerdoelen

Na het bestuderen en werken met dit project kun je:

1. **Overerving toepassen** - Subklassen maken die eigenschappen en methoden van een superklasse erven
2. **super() gebruiken** - De parent constructor en methoden aanroepen vanuit een subklasse
3. **Method overriding** - Methoden uit de superklasse overschrijven met subklasse-specifiek gedrag
4. **Polymorfisme begrijpen** - Meerdere objecttypen via een gemeenschappelijke interface gebruiken
5. **Type hints toepassen** - Code documenteren met type annotations voor betere leesbaarheid

---

## 🎯 Kernbegrippen

### 1. Overerving (Inheritance)

**Overerving** is een mechanisme waarbij een nieuwe klasse (subklasse/child) eigenschappen en methoden overneemt van een bestaande klasse (superklasse/parent).

**Voordelen:**
- 🔄 **Code hergebruik** - Geen duplicatie van gemeenschappelijke code
- 📦 **Hiërarchische structuur** - Organiseer gerelateerde klassen logisch
- 🛠️ **Uitbreidbaarheid** - Voeg specifieke functionaliteit toe zonder de basis te wijzigen

**In dit project:**
```python
class Karakter:           # Superklasse (parent)
    pass

class Leerkracht(Karakter):  # Subklasse (child) - erft van Karakter
    pass

class Leerling(Karakter):    # Subklasse (child) - erft van Karakter
    pass
```

### 2. super()

`super()` geeft toegang tot methoden van de parent klasse. Dit voorkomt code duplicatie.

**Gebruik:**
```python
class Leerkracht(Karakter):
    def __init__(self, naam, leeftijd, vak, x_tile, y_tile):
        super().__init__(naam, leeftijd, x_tile, y_tile, COLORS["blauw"])
        self.vak = vak  # Extra attribuut
```

### 3. Method Overriding

**Method overriding** betekent dat je een methode uit de parent klasse vervangt door een nieuwe implementatie in de child klasse.

**In dit project:**
- `Karakter.beschrijf()` → geeft basis info
- `Leerkracht.beschrijf()` → override met vak info
- `Leerling.beschrijf()` → override met klas info

### 4. Polymorfisme

**Polymorfisme** betekent "vele vormen". Een variabele van type `Karakter` kan een `Leerkracht` of `Leerling` object bevatten, en Python kiest automatisch de juiste methode.

**In dit project:**
```python
npcs: list[Karakter] = [
    Leerkracht("Dirk", 54, "Geschiedenis", 5, 5),
    Leerling("Amin", 15, "3A", 8, 12),
]

for npc in npcs:
    print(npc.beschrijf())  # Juiste versie wordt automatisch gekozen!
```

---

## 🏗️ Projectstructuur

```
RPG_2/
├── README.md                 # Dit bestand
├── config.py                 # Constanten (scherm, kleuren, tiles)
├── models/
│   ├── karakter.py          # Superklasse: Karakter
│   ├── leerkracht.py        # Subklasse: Leerkracht
│   └── leerling.py          # Subklasse: Leerling
├── tilemap.py               # Grid-based tilemap met collision en HUD
└── main.py                  # Hoofdprogramma met game loop
```

---

## 🎮 Hoe werkt het spel?

### Controls
- **Pijltjestoetsen** - Beweeg per tile (1 stap per toets)
- **E** - Interacteer met NPC die naast je staat (boven, onder, links, rechts)

### Gameplay
1. Je speelt als een geel vierkant in een school
2. Beweeg door de wereld (witte vloeren, grijze muren)
3. Ga naast NPCs staan (blauwe leerkrachten, groene leerlingen)
4. Druk op **E** om met ze te praten
5. Elke NPC heeft uniek gedrag via polymorfisme:
   - **Leerkracht** → geeft een les over hun vak
   - **Leerling** → gaat studeren (houdt studietijd bij)

---

## 📖 Stappenplan: Code Begrijpen

### Stap 1: Begin bij config.py

Open `config.py` en bekijk:
- `MAP_BREEDTE` en `MAP_HOOGTE` - bepalen de grootte van de spelwereld
- `TILE_SIZE` - bepaalt hoe groot elke tile is in pixels
- `SCREEN_WIDTH` en `SCREEN_HEIGHT` - worden **automatisch berekend** op basis van de map en HUD
- `COLORS` - alle kleuren die in het spel gebruikt worden

### Stap 2: Bestudeer de superklasse

Open `models/karakter.py` en bestudeer:
- De `__init__` methode - welke attributen heeft elk karakter?
- De `beschrijf()` methode - wat is de basis implementatie?
- De `interact()` methode - standaard gedrag
- De `teken()` en `beweeg()` methoden - hoe werken karakters?

### Stap 3: Bekijk de subklassen

Open `models/leerkracht.py`:
- Hoe wordt `super().__init__()` gebruikt?
- Welke extra attributen heeft een Leerkracht? (vak)
- Hoe overschrijft `beschrijf()` de parent versie?
- Wat doet `interact()` - let op dat de logica direct in de methode staat!

Open `models/leerling.py`:
- Vergelijk met Leerkracht - wat is hetzelfde, wat anders?
- Welke extra attributen heeft Leerling? (klas, studietijd)
- Hoe wordt `studietijd` bijgehouden in `interact()`?

### Stap 4: Zie polymorfisme in actie

Open `main.py` en zoek naar:
```python
# POLYMORFISME: lijst bevat verschillende subklassen van Karakter
self.npcs: list[Karakter] = [
    Leerkracht("Dirk", 54, "Geschiedenis", 5, 5),
    Leerling("Amin", 15, "3A", 8, 12),
]
```

**Let op:** De lijst heeft type `list[Karakter]`, maar bevat verschillende subklassen!

Zoek de `probeer_interactie()` methode:
```python
npc.interact()  # Welke versie wordt aangeroepen?
```

Python kiest **tijdens runtime** de juiste methode op basis van het werkelijke type!

### Stap 5: Experimenteer

Probeer het spel te draaien:
```bash
python main.py
```

Kijk wat er gebeurt als je interacteert met verschillende NPCs.

---

## 💡 Oefeningen

### Oefening 1: Voeg een nieuwe subklasse toe ⭐

**Doel:** Oefen overerving en method overriding

Maak een nieuwe file `models/directeur.py`:

1. Maak een `Directeur` klasse die erft van `Karakter`
2. Geef het een extra attribuut `jaren_ervaring`
3. Kies een unieke kleur (bijvoorbeeld "paars")
4. Override `beschrijf()` om directeur-info te tonen
5. Override `interact()` met een unieke actie (bijv. "geeft een toespraak")

**Bonus:** Voeg een Directeur NPC toe aan de game in `main.py`!

<details>
<summary>💡 Hint</summary>

```python
from models.karakter import Karakter
from config import COLORS

class Directeur(Karakter):
    def __init__(self, naam: str, leeftijd: int, jaren_ervaring: int, x_tile: int, y_tile: int):
        super().__init__(naam, leeftijd, x_tile, y_tile, COLORS["paars"])
        self.jaren_ervaring = jaren_ervaring
    
    def beschrijf(self) -> str:
        basis = super().beschrijf()
        return f"{basis} - Directeur ({self.jaren_ervaring} jaar ervaring)"
    
    def interact(self) -> str:
        return f"Geeft een inspirerende toespraak!"
```
</details>

---

### Oefening 2: Voeg attributen toe ⭐⭐

**Doel:** Begrijp state management in objecten

Voeg een `energie: int` attribuut toe aan alle karakters:

1. Voeg `energie` toe aan `Karakter.__init__()` (bijvoorbeeld startwaarde 100)
2. Laat `Leerkracht.interact()` energie verminderen (-10)
3. Laat `Leerling.interact()` energie verminderen (-5)
4. Update `beschrijf()` om energie te tonen
5. (Optioneel) Voorkom interactie als energie < 20

---

### Oefening 3: Implementeer een attributen systeem ⭐⭐⭐

**Doel:** Pas polymorfisme toe in een complexere situatie

Maak een inventaris systeem:

1. Voeg `inventaris: list[str]` toe aan `Karakter`
2. Maak een `geef_item(item: str)` methode in `Karakter`
3. Maak een `ontvang_item(item: str)` methode in `Karakter`
4. Laat Leerkrachten boeken geven, Leerlingen pennen ontvangen
5. Update de `interact()` methoden om items uit te wisselen

---

### Oefening 4: Maak het spel interessanter ⭐⭐⭐

**Doel:** Creatief denken en code uitbreiden

Ideeën:
- Voeg een quest systeem toe (praat met 3 verschillende NPCs)
- Maak een "moeidheid" systeem (energie daalt bij bewegen)
- Voeg meerdere levels/kamers toe (wijzig `tilemap._maak_map()`)
- Maak bewegende NPCs (random walk of patrol routes)
- Voeg een score systeem toe

---

## 📝 Mini-Quiz

Test je begrip!

### Vraag 1: Wat is overerving?
**A)** Het kopiëren van code van een klasse naar een andere  
**B)** Een mechanisme waarbij een klasse eigenschappen en methoden overneemt van een andere klasse  
**C)** Het aanroepen van een functie in een andere klasse  
**D)** Het maken van meerdere instanties van een klasse  

<details>
<summary>Antwoord</summary>

**B** - Overerving is een mechanisme waarbij een klasse (subklasse) eigenschappen en methoden overneemt van een andere klasse (superklasse).
</details>

---

### Vraag 2: Wat doet super().__init__()?
**A)** Het maakt een nieuwe instantie van de superklasse  
**B)** Het roept de constructor van de parent klasse aan  
**C)** Het overschrijft de parent constructor  
**D)** Het verwijdert de parent klasse  

<details>
<summary>Antwoord</summary>

**B** - `super().__init__()` roept de constructor (`__init__`) van de parent klasse aan, zodat de parent kan initialiseren wat nodig is.
</details>

---

### Vraag 3: Wat is method overriding?
**A)** Het aanroepen van een methode uit de parent klasse  
**B)** Het verwijderen van een methode  
**C)** Het vervangen van een parent methode met een nieuwe implementatie in de child klasse  
**D)** Het maken van een nieuwe methode  

<details>
<summary>Antwoord</summary>

**C** - Method overriding is het vervangen van een methode uit de parent klasse met een nieuwe (aangepaste) implementatie in de child klasse.
</details>

---

### Vraag 4: Wat is polymorfisme?
**A)** Het hebben van meerdere constructors  
**B)** Het maken van meerdere klassen  
**C)** Het vermogen om objecten van verschillende types via een gemeenschappelijke interface te gebruiken  
**D)** Het erven van meerdere klassen tegelijk  

<details>
<summary>Antwoord</summary>

**C** - Polymorfisme betekent dat je objecten van verschillende types (bijv. Leerkracht en Leerling) via een gemeenschappelijke interface (Karakter) kunt gebruiken, waarbij Python automatisch de juiste methode kiest.
</details>

---

### Vraag 5: Code Analyse

Bekijk deze code:
```python
personen: list[Karakter] = [
    Leerkracht("Anna", 40, "Engels", 3, 3),
    Leerling("Tom", 15, "2B", 5, 5),
]

for persoon in personen:
    print(persoon.beschrijf())
```

**Welke beschrijf() methode wordt aangeroepen voor het tweede element in de lijst?**

**A)** `Karakter.beschrijf()`  
**B)** `Leerkracht.beschrijf()`  
**C)** `Leerling.beschrijf()`  
**D)** Het geeft een error  

<details>
<summary>Antwoord</summary>

**C** - Het tweede element is een `Leerling` object, dus wordt `Leerling.beschrijf()` aangeroepen. Dit is polymorfisme: hoewel de variabele type `list[Karakter]` is, wordt de juiste methode gekozen op basis van het **werkelijke** type van het object tijdens runtime.
</details>

---

### Vraag 6: Type Hints

Wat betekent deze type hint?
```python
def vind_npc(self) -> Karakter | None:
```

**A)** De methode returned een Karakter of een None  
**B)** De methode returned een string  
**C)** De methode returned een boolean  
**D)** De methode returned een lijst  

<details>
<summary>Antwoord</summary>

**A** - De `|` operator (vanaf Python 3.10) betekent "of". Deze methode kan een `Karakter` object returnen, of `None` als er niets gevonden is. Dit heet een **Union type**.
</details>

---

### Vraag 7: Code Challenge

Als je dit zou schrijven:
```python
leerkracht = Leerkracht("Marie", 35, "Frans", 2, 2)
print(leerkracht.naam)
```

**Waar komt het `naam` attribuut vandaan?**

**A)** Het wordt gedefinieerd in `Leerkracht.__init__()`  
**B)** Het wordt geërfd van `Karakter` via `super().__init__()`  
**C)** Het is een built-in Python attribuut  
**D)** Het bestaat niet en geeft een error  

<details>
<summary>Antwoord</summary>

**B** - Het `naam` attribuut wordt geërfd van `Karakter`. Wanneer `Leerkracht.__init__()` `super().__init__(naam, ...)` aanroept, initialiseert de parent klasse `self.naam = naam`.
</details>

---

## 🎓 Conclusie

Dit project demonstreert de vier pijlers van OOP:
1. **Encapsulation** (inkapseling) - Data en methoden samen in klassen
2. **Inheritance** (overerving) - Hergebruik van code via parent-child relaties
3. **Polymorphism** (polymorfisme) - Eén interface, meerdere implementaties
4. **Abstraction** (abstractie) - Verbergen van complexiteit achter simpele interfaces

**Volgende stappen:**
- Experimenteer met de oefeningen
- Maak je eigen subklassen
- Voeg nieuwe features toe
- Deel je creaties!

---

## 📚 Extra Bronnen

- [Python Official Docs - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Real Python - OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

---

**Veel plezier met leren en programmeren! 🚀**

