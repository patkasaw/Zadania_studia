# Indeksowanie z warunkiem logicznym
import numpy as np
tablica = np.arange(1, 21)
parzyste = tablica[tablica % 2 == 0]
print(tablica)
print(parzyste)