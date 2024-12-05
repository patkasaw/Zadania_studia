import zad9

def wczytaj_ulamek(prompt):
    """Wczytuje ułamek od użytkownika w formacie licznik/mianownik."""
    while True:
        try:
            ulamek = input(prompt)
            licznik, mianownik = map(int, ulamek.split('/'))
            if mianownik == 0:
                print('Mianownik nie może być równy zero. Spróbuj ponownie.')
                continue
            return(licznik, mianownik)
        except ValueError:
            print("Niepoprawny format! Użyj formatu licznik/mianownik (np. 1/2)")
# Ciekawe wyświetlenie tytułu

version = 0.1
hello = f"Program do operacji na ułamkach w wersji {version}"
bars = '='*len(hello)

print(bars)
print(hello)
print(bars)
print('''Dostępne operacje:
1. Dodawanie
2. Odejmowanie
3. Mnożenie
4. Dzielenie''')

nie_wybrano = True
while nie_wybrano:
    try:
        wybor = int(input('\nWybierz operację (1-4):'))
        if wybor not in [1, 2, 3, 4]:
            print('Wybierz liczbę od 1 do 4!')
            continue
        nie_wybrano = False
    except ValueError:
        print('Wprowadź poprawną liczbę!')

print("Ułamki podajemy w formacie licznik/mianownik np: 2/3.")
a = wczytaj_ulamek("Podaj pierwszy ułamek: ")
b = wczytaj_ulamek("Podaj drugi ułamek: ")

operacje = {
 1: (zad9.dodaj, "+"),
 2: (zad9.odejmij, "-"),
 3: (zad9.pomnoz, "*"),
 4: (zad9.podziel, ":"),
}

print(print(f"\nWynik: {a[0]}/{a[1]} {operacje[wybor][1]} {b[0]}/{b[1]} = {operacje[wybor][0](a,b)[0]}/{operacje[wybor][0](a, b)[1]}"))

