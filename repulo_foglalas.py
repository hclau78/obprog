class Jarat:
    def __init__(self, jaratszam, cel, indulas, repulesido, jegyar):
        self.jaratszam = jaratszam
        self.cel = cel
        self.indulas = indulas
        self.repulesido = repulesido
        self.jegyar = jegyar

jarat1 = Jarat('HU1225', 'Debrecen', '12:35', '1 óra',  ' 12 500 Ft')
jarat2 = Jarat('FR5674', 'Parizs', '21:00', '3 óra', '56 000 Ft')
jarat3 = Jarat('MAN8412', 'Manila', '6:00', '15 óra', '128 900 Ft')

class Foglalas:
    def __init__(self, vezeteknev, keresztnev, jarat):
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        self.jarat = jarat

