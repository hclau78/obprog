from jarat import Jarat


class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    def jarat_info(self):
        return f"Belföldi járat: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft"
