from jarat import Jarat


class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_info(self):
        return f"Belföldi járat: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft"
