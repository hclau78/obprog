class JegyFoglalas:
    def __init__(self, jarat, utas_nev):
        self._jarat = jarat
        self._utas_nev = utas_nev

    @property
    def jarat(self):
        return self._jarat

    @property
    def utas_nev(self):
        return self._utas_nev

    def foglalas_info(self):
        return f"{self.utas_nev} foglalt egy jegyet a(z) {self.jarat.jaratszam} számú járatra ({self.jarat.celallomas})"

    def jegyar(self):
        return self.jarat.jegyar