#Ćwiczenie 2: Zapisywanie danych do pliku tekstowego
imie = input('Podaj swoje imie:')
wiek = input('Podaj swój wiek:')
miasto = input('Podaj swoje miasto:')

try:
    file = open('uzytkownik.txt', 'w')

    file.write(f'Imie: {imie} \n')
    file.write(f'Wiek: {wiek} \n')
    file.write(f'Miasto: {miasto} \n')

    file.close()

    print("Dane zostały zapisane w pliku 'uzytkownik.txt'")

except Exception as e:
    print(f'Wystąpił błąd podczas zapisu do pliku: {e}')