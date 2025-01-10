#Tworzenie indeksu na bazie listy
import pandas as pd
ind = pd.Index([2, 3, 5, 7, 11])
print(ind)
#pierwszy element indeksu
print(ind[1])
#co drugi jego element
print(ind[::2])

#Wypisz na ekranie rozmiar, kształt, liczbę wymiarów oraz typ danych indeksu ind z ćwiczenia 30
print(ind.size, ind.shape, ind.ndim, ind.dtype)

#Spróbuj pierwszemu elementowi indeksu ind z ćwiczenia 30 nadać wartość 0
ind[1] = 0
