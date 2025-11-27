class Voertuig:
    def __init__(self, naam: str, snelheid: int):
        self.naam = naam
        self.snelheid = snelheid

    def beweeg(self) -> str:
        return f"{self.naam} beweegt aan {self.snelheid} km/u"