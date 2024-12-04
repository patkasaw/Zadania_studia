#Ćwiczenie 7: Zapisywanie danych do pliku CSV
imie = input('Podaj swoje imie:')
wiek = input('Podaj swoj wiek:')
miasto = input('Podaj swoje miasto:')

try:
    with open('dane.csv', 'w') as file:
        file.write(f'{imie}, {wiek}, {miasto}\n')
    
    print('Dane zostały dodane do pliku dane.csv')

except Exception as e:
    print(f'Wystąpił błąd podczas zapisu do pliku {e}')

