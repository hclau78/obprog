from jarat import Jarat
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from foglalas import JegyFoglalas
from legitarsasag import LegiTarsasag
from abc import ABC, abstractmethod


def repulo_foglalas():
    legi_tarsasag = LegiTarsasag("Malév")

    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B001", "Magyarország", 10000))
    legi_tarsasag.jarat_hozzaadasa(NemzetkoziJarat("N001", "Franciaország", 20000))
    legi_tarsasag.jarat_hozzaadasa(NemzetkoziJarat("N002", "Fülöp-szigetek", 50000))

    legi_tarsasag.jegy_foglalasa("B001", "Malacka")
    legi_tarsasag.jegy_foglalasa("B001", "Füles")
    legi_tarsasag.jegy_foglalasa("N001", "Tigirs")
    legi_tarsasag.jegy_foglalasa("N001", "Zsebi baba")
    legi_tarsasag.jegy_foglalasa("N002", "Nyuszi")
    legi_tarsasag.jegy_foglalasa("N002", "Micimackó")

    while True:

        print("\n1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Járatok listázása")
        print("5. Kilépés")
        valasztas = input("\nVálassz egy lehetőséget: \n")

        if valasztas == "1":
            print("Jegy foglalása")
            jaratszam = input("\nAdd meg a járatszámot: ")
            utas_nev = input("Add meg az utas nevét: ")
            ar = legi_tarsasag.jegy_foglalasa(jaratszam, utas_nev)
            if ar:
                print(f"A foglalás jegyára: {ar} Ft")

        elif valasztas == "2":
            jaratszam = input("\nAdd meg a járatszámot: ")
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

