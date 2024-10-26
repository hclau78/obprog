from jarat import Jarat
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from foglalas import Foglalas
from legitarsasag import LegiTarsasag
from abc import ABC, abstractmethod


def repulo_foglalas():
    legi_tarsasag = LegiTarsasag("Malév")

    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B001", "Magyarország", 10000))
    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B002", "Franciaország", 20000))
    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B003", "Fülöp-szigetek", 50000))

    while True:

        print("\n1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Járatok listázása")
        print("5. Kilépés")
        valasztas = input("\nVálassz egy lehetőséget: \n")

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
            print("\n")
            legi_tarsasag.foglalasok_listazasa()

        elif valasztas == "4":
            print("\n")
            legi_tarsasag.jaratok_listazasa()


        elif valasztas == "5":
            break

        else:
            print("Érvénytelen választás!")

        a = input("\nFolytatáshoz nyomd meg az Entert")

repulo_foglalas()

