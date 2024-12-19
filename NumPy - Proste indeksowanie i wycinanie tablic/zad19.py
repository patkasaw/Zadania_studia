# Indeksowanie z użyciem zakresu
import numpy as np
tablica = np.arange(10, 101, 10)
co_drugi = tablica[1::2]
print('Oryginalna tablica:', tablica)
print('Co drugi element:', co_drugi)