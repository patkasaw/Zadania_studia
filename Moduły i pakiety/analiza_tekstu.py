#Tworzenie modułu do analizy tekstu

def licz_słowa(tekst):
    return len(tekst.split())

def licz_znaki(tekst):
    return len(tekst)

def policz_wystapienia_slowa(tekst, slowo):
    return tekst.lower().split().count(slowo.lower())

def czy_palindrom(tekst):

    oczyszczony_tekst = ''.join(tekst.lower().split())
    return oczyszczony_tekst == oczyszczony_tekst[::-1]


