class Jarat:
    def __init__(self, jaratszam, legitarsasag, celorszag, indulasido, repulesido, jegyar):
        self.jaratszam = jaratszam
        self.legitarsasag = legitarsasag
        self.celorszag = celorszag
        self.indulasido = indulasido
        self.repulesido = repulesido
        self.jegyar = jegyar

    def __str__(self):
        return f'A foglalasok a rendszerben: A(z) {self.jaratszam} jaratszamu gep a(z) {self.legitarsasag} gepe, indul {self.indulasido}-kor.'

jarat1 = Jarat('1', 'Malev', 'Magyarorszag', '12:00', '1 óra', ' 12 500 Ft')
jarat2 = Jarat('2', 'FranceAir', 'Franciaorszag', '21:00', '3 óra', '56 000 Ft')
jarat3 = Jarat('3', 'PhilipAir', 'Fulop-szigetek',  '6:00', '15 óra', '128 900 Ft')

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
