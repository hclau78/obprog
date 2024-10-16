class Jarat:
    def __init__(self, jaratszam, celorszag, celvaros, indulasido, repulesido, jegyar):
        self.jaratszam = jaratszam
        self.celorszag = celorszag
        self.celvaros = celvaros
        self.indulas = indulasido
        self.repulesido = repulesido
        self.jegyar = jegyar

jarat1 = Jarat('HU1225',  'Magyarorszag', 'Debrecen', '12:35', '1 óra',  ' 12 500 Ft')
jarat2 = Jarat('FR5674',  'Franciaorszag','Parizs', '21:00', '3 óra', '56 000 Ft')
jarat3 = Jarat('MAN8412',  'Fulop-szihetek', 'Manila', '6:00', '15 óra', '128 900 Ft')

class Foglalas:
    def __init__(self, vezeteknev, keresztnev, jarat):
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        self.jarat = jarat

class BelfoldiJarat:
    def __init__(self, celorszag, repulesido, jegyar):
        self.celorszag = celorszag
        self.repulesido = repulesido
        self.jegyar = jegyar

class NemzetkoziJarat:
    def __init__(self, celorszag, jegyar):
        self.celorszag = celorszag
        self.jegyar = jegyar

class LegiTarsasag:
    def __init__(self, legitarsasag):
        self.legitarsasag = legitarsasag



