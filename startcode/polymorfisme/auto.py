from voertuig import Voertuig

class Auto(Voertuig):
    def __init__(self, naam: str, snelheid: int, brandstof: int):
        super().__init__(naam, snelheid)
        self.brandstof = brandstof

    def beweeg(self) -> str:
        if self.brandstof <= 0:
            return f"{self.naam} staat stil (geen brandstof)"
        self.brandstof -= 1
        return f"{self.naam} rijdt aan {self.snelheid} km/u"