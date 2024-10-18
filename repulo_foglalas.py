class Jarat:
    def __init__(self, jaratszam, celorszag, indulasido):
        self.jaratszam = jaratszam
        self.celorszag = celorszag
        self.indulasido = indulasido


    def __str__(self):
        return f'A foglalasok a rendszerben: A(z) {self.jaratszam} jaratszamu gep a(z) {self.legitarsasag} gepe, indul {self.indulasido}-kor.'

jarat1 = Jarat('1', 'Magyarorszag', '12:00')
jarat2 = Jarat('2', 'Franciaorszag', '21:00')
jarat3 = Jarat('3',  'Fulop-szigetek',  '6:00')

class Foglalas:
    def __init__(self, nev, jaratszam):
        self.nev = nev
        self.jaratszam = jaratszam

foglalas1 = Foglalas("Malacka", jarat1)
foglalas2 = Foglalas("Fules", jarat1)
foglalas3 = Foglalas('Tigris', jarat2)
foglalas4 = Foglalas('Zsebi baba', jarat2)
foglalas5 = Foglalas('Nyuszi', jarat2)
foglalas6 = Foglalas('Micimacko', jarat3)

class BelfoldiJarat:
    def __init__(self, jaratszam, celorszag, jegyar):
        self.jaratszam = jaratszam
        self.celorszag = celorszag
        self.jegyar = jegyar

class NemzetkoziJarat:
    def __init__(self, jaratszam, celorszag, jegyar):
        self.jaratszam = jaratszam
        self.celorszag = celorszag
        self.jegyar = jegyar

class LegiTarsasag:
    def __init__(self, legitarsasag, jaratszam):
        self.legitarsasag = legitarsasag
        self.jaratszam = jaratszam


