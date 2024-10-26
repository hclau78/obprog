from jarat import Jarat
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from foglalas import Foglalas
from legitarsasag import LegiTarsasag
from abc import ABC, abstractmethod


def repulo_foglalas():
    legi_tarsasag = LegiTarsasag("Malév")

    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B001", "Magyarország", 10000))

    while True:

        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Járatok listázása")
        print("5. Kilépés")
        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            print("Jegy foglalása")
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
            legi_tarsasag.jaratok_listazasa()

        elif valasztas == "5":
            break

        else:
            print("Érvénytelen választás!")

repulo_foglalas()

