#Tworzenie tablicy z określonym typem danych
import numpy as np
tablica = np.arange(1, 11).astype(np.float64)
print(tablica)
tablica = np.arange(1, 11, dtype=np.float64)
print(tablica)