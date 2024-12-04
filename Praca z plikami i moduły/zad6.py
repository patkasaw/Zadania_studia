#Ćwiczenie 6: Czytanie i zapisywanie danych z pliku CSV
try:
    with open('dane.csv', 'r') as file:
        for line in file:
            kolumny = line.strip().split(',')
            print(kolumny)
except FileNotFoundError:
    print("Błąd: Plik 'dane.csv' nie został znaleziony.")