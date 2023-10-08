from verden import Verden

def hovedprogram():
    rad = int(input("Oppgi antall rader: "))
    kol = int(input("Oppgi antall kolonner: "))
    objekt = Verden(rad, kol)
    objekt.tegn()
    inp = input("q for å stoppe, eller tom linje til å fortsette: ")
    while inp != "q":
        if inp == "":
            objekt.oppdatering()
            objekt.tegn()
        inp = input("q for å stoppe, eller tom linje til å fortsette: ")

hovedprogram()
