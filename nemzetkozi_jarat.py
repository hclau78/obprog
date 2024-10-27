from jarat import Jarat


class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_info(self):
        return f"Nemzetközi járat: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft"
