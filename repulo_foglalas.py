import jarat
import belfoldi_jarat
import nemzetkozi_jarat
import foglalas
import legitarsasag

class Foglalas:
    def __init__(self, jarat, utas_nev):
        self.jarat = jarat
        self.utas_nev = utas_nev


class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

