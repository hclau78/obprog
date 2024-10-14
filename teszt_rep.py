from abc import ABC, abstractmethod

# Járat absztrakt osztály
class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_info(self):
        pass


# BelföldiJarat osztály
class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_info(self):
        return f"Belföldi járat: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft"


# NemzetkoziJarat osztály
class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_info(self):
        return f"Nemzetközi járat: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft"


# JegyFoglalas osztály
class JegyFoglalas:
    def __init__(self, jarat, utas_nev):
        self.jarat = jarat
        self.utas_nev = utas_nev

    def foglalas_info(self):
        return f"{self.utas_nev} foglalt egy jegyet a(z) {self.jarat.jaratszam} számú járatra ({self.jarat.celallomas})"

    def jegyar(self):
        return self.jarat.jegyar


# LégiTársaság osztály
class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

    def jegy_foglalasa(self, jaratszam, utas_nev):
        jarat = self._keres_jarat(jaratszam)
        if jarat:
            foglalas = JegyFoglalas(jarat, utas_nev)
            self.foglalasok.append(foglalas)
            print(f"Sikeres foglalás: {foglalas.foglalas_info()}")
            return foglalas.jegyar()
        else:
            print("Nincs ilyen járat.")
            return None

    def foglalas_lemondasa(self, jaratszam, utas_nev):
        for foglalas in self.foglalasok:
            if foglalas.jarat.jaratszam == jaratszam and foglalas.utas_nev == utas_nev:
                self.foglalasok.remove(foglalas)
                print(f"{utas_nev} lemondta a(z) {jaratszam} számú járatra szóló foglalását.")
                return True
        print("Nincs ilyen foglalás.")
        return False

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincsenek aktuális foglalások.")
        else:
            for foglalas in self.foglalasok:
                print(foglalas.foglalas_info())

    def _keres_jarat(self, jaratszam):
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None


# Fő program
def felhasznaloi_interfesz():
    legi_tarsasag = LegiTarsasag("PéldaLégitársaság")

    # Járatok hozzáadása
    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B123", "Budapest", 15000))
    legi_tarsasag.jarat_hozzaadasa(NemzetkoziJarat("N456", "New York", 80000))

    while True:
        print("\n1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            jaratszam = input("Add meg a járatszámot: ")
            utas_nev = input("Add meg az utas nevét: ")
            ar = legi_tarsasag.jegy_foglalasa(jaratszam, utas_nev)
            if ar:
                print(f"A foglalás jegyára: {ar} Ft")

        elif valasztas == "2":
            jaratszam = input("Add meg a járatszámot: ")
            utas_nev = input("Add meg az utas nevét: ")
            legi_tarsasag.foglalas_lemondasa(jaratszam, utas_nev)

        elif valasztas == "3":
            legi_tarsasag.foglalasok_listazasa()

        elif valasztas == "4":
            break

        else:
            print("Érvénytelen választás!")


# Program indítása
if __name__ == "__main__":
    felhasznaloi_interfesz()
