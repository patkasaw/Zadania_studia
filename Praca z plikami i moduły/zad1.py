#2.1. Operacje na plikach
#Ćwiczenie 1: Odczytywanie pliku tekstowego
try:
    file = open('dane.txt', 'r')
    content = file.read()

    print('Zawartosć pliku dane.txt:')
    print(content)

    file.close()
    
except FileNotFoundError:
    print('Błąd: plik nie został znaleziony')
