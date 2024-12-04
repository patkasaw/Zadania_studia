#Ćwiczenie 8: Odczyt i analiza danych z pliku CSV
try:
    with open('dane.csv', 'r') as file:
        liczba_wierszy = 0
        liczba_kolumn = 0
    
    for line in file:
        liczba_wierszy += 1
        kolumny = line.strip().split(',')
        liczba_kolumn = len(kolumny)
    
    print(f'Liczba wierszy (rekordów) w pliku: {liczba_wierszy}')
    print(f'Liczba kolumn w rekordach: {liczba_kolumn}')

except FileNotFoundError:
    print("Błąd: Plik 'dane.csv' nie został znaleziony.")