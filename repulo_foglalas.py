class Jarat:
    def __init__(self, jaratszam, legitarsasag, celorszag, celvaros, indulasido, repulesido, jegyar):
        self.jaratszam = jaratszam
        self.celorszag = celorszag
        self.celvaros = celvaros
        self.indulas = indulasido
        self.repulesido = repulesido
        self.jegyar = jegyar

jarat1 = Jarat('1', 'Malev', 'Magyarorszag', 'Debrecen', '12:00', '1 óra', ' 12 500 Ft')
jarat2 = Jarat('2', 'FranceAir', 'Franciaorszag', 'Parizs', '21:00', '3 óra', '56 000 Ft')
jarat3 = Jarat('3', 'PhilipAir', 'Fulop-szigetek', 'Manila', '6:00', '15 óra', '128 900 Ft')

class Foglalas:
    def __init__(self, nev, jarat):
        self.nev = nev
        self.jarat = jarat

foglalas1 = Foglalas("Malacka", jarat1)
foglalas2 = Foglalas("Fules", jarat1)
foglalas3 = Foglalas('Tigris', jarat2)
foglalas4 = Foglalas('Zsebi baba', jarat2)
foglalas5 = Foglalas('Nyuszi', jarat2)
foglalas6 = Foglalas('Micimacko', jarat3)

class BelfoldiJarat:
    def __init__(self, celorszag, repulesido, jegyar):
        self.celorszag = celorszag
        self.repulesido = repulesido
        self.jegyar = jegyar

class NemzetkoziJarat:
    def __init__(self, celorszag, repulesido, jegyar):
        self.celorszag = celorszag
        self.repulesido = repulesido
        self.jegyar = jegyar

class LegiTarsasag:
    def __init__(self, legitarsasag):
        self.legitarsasag = legitarsasag

print(jarat1)

