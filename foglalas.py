class Foglalas:
    def __init__(self, jarat, utas_nev):
        self.jarat = jarat
        self.utas_nev = utas_nev

    def foglalas_info(self):
        return f"{self._utas_nev} foglalt egy jegyet a(z) {self.jarat.jaratszam} számú járatra ({self.jarat.celallomas})"

    def jegyar(self):
        return self.jarat.jegyar