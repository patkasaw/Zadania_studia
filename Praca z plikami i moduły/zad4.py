#Ćwiczenie 4: Menedżer kontekstu - Odczyt pliku tekstowego
try:

    with open('dane.txt, 'r'') as file:

        content = file.read()
        
        print('Zawartość pliku dane.txt:')
        print(content)

except FileNotFoundError:
    print('Błąd: plik nie został odnaleziony')

