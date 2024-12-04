#Ćwiczenie 5: Menedżer kontekstu - Zapisywanie danych do pliku
imie = input('Podaj swoje imie:')
wiek = input('Podaj swój wiek:')
miasto = input('Podaj swoje miasto:')
try:
    with open('uzytkownik.txt', 'w') as file:
        file.write(f'Imie: {imie} \n')
        file.write(f'Wiek: {wiek} \n')
        file.write(f'Miasto: {miasto} \n')

        print("Dane zostały zapisane w pliku 'uzytkownik.txt'")

except Exception as e:
    print(f'Wystąpił błąd podczas zapisu do pliku: {e}')