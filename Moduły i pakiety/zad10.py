import analiza_tekstu

nazwa_pliku = input('Podaj nazwę pliku, z któego chcesz odczytać tekst:')

try:
    
    with open(nazwa_pliku, 'r') as plik:
        tekst = plik.read()

    print('\nWybierz operację:')
    print('1. Liczba słów: ')
    print('2. Liczba znaków: ')
    print('3. Liczba wystąpień danego słowa: ')
    print('4. Sprwdzenie, czy tekst jest palindromem ')
    wybor = input('Podaj numer operacji (1/2/3/4): ')

    if wybor == '1':
        liczba_slow = analiza_tekstu.licz_słowa(tekst)
        print(f'Liczba słów w tekście: {liczba_slow}')
    
    elif wybor == '2':
        liczba_znakow = analiza_tekstu.licz_znaki(tekst)
        print(f'Liczba znaków w tekście: {liczba_znakow}')
    
    elif wybor == '3':
        liczba_wystapien = analiza_tekstu.policz_wystapienia_slowa(tekst, slowo)
        print(f"Liczba wystapien slowa '{slowo}' w tekście: {liczba_wystapien}")
    
    elif wybor == '4':
        jest_palindromem = analiza_tekstu.czy_palindrom(tekst)
        if jest_palindromem:
            print('Podany tekst jest palindromem')
        else:
            print('Podany tekst nie jest palindromem')

    else:
        print('Nieprawidłowy wybór. Spróbuj ponownie')

except FileNotFoundError:
    print(f"Błąd: Plik '{nazwa_pliku}' nie został znaleziony.")

except Exception as e:
    print(f'Wystąpił błąd: {e}')




