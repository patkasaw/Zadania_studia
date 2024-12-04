#Ćwiczenie 3: Czytanie pliku tekstowego linia po linii
try:
    file = open('dane.txt, 'r'')
    
    print('Zawartość pliku dane.txt:')
    line = file.readline()

    for line in file:
        print(line)
        
        file.close()

except FileNotFoundError:
    print('Błąd: plik nie został odnaleziony')
