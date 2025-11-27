from voertuig import Voertuig

class Fiets(Voertuig):
    def beweeg(self) -> str:
        return f"{self.naam} fietst aan {self.snelheid} km/u"