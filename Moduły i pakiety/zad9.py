#Tworzenie modułu do operacji na ułamkach

def dodaj(a,b):
    nowy_licznik = a[0] * b[1] + b[0] * a[1]
    nowy_mianownik = a[1] * b[1]
    return(nowy_licznik, nowy_mianownik)

def odejmij(a,b):
    nowy_licznik = a[0] * b[1] - b[0] * a[1]
    nowy_mianownik = a[1] - b[1]
    return(nowy_licznik, nowy_mianownik)

def pomnoz(a,b):
    nowy_licznik = a[0] * b[0]
    nowy_mianownik = a[1] * b[1]
    return(nowy_licznik, nowy_mianownik)

def podziel(a,b):
    if b[0] == 0:
        raise ValueError('Nie mozna dzielic przez zero.)')
    nowy_licznik = a[0] / b[0]
    nowy_mianownik = a[1] / b[1]
    return(nowy_licznik, nowy_mianownik)


