from foglalas import JegyFoglalas



class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

    def jegy_foglalasa(self, jaratszam, utas_nev):
        jarat = self.keres_jarat(jaratszam)
        if jarat:
            foglalas = JegyFoglalas(jarat, utas_nev)
            self.foglalasok.append(foglalas)
            print(f"\nSikeres foglalás: {foglalas.foglalas_info()}")
            return foglalas.jegyar()
        else:
            print("\nNincs ilyen járat.")
            return None

    def foglalas_lemondasa(self, jaratszam, utas_nev):
        for foglalas in self.foglalasok:
            if foglalas.jarat.jaratszam == jaratszam and foglalas.utas_nev == utas_nev:
                self.foglalasok.remove(foglalas)
                print(f"\n{utas_nev} lemondta a(z) {jaratszam} számú járatra szóló foglalását.")
                return True
        print("\nNincs ilyen foglalás")
        return True

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("\nNincsenek aktuális foglalások.")
        else:
            for foglalas in self.foglalasok:
                print(foglalas.foglalas_info())

    def jaratok_listazasa(self):
        if not self.jaratok:
            print("\nNincsenek járatok.")
        else:
            for jarat in self.jaratok:
                print(jarat.jarat_info())

    def keres_jarat(self, jaratszam):
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None


