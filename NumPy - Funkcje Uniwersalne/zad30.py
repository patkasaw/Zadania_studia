#  np.max() kontra np.maximum()
import numpy as np
tab_1 = np.random.randint(1, 21, 10)
tab_2 = np.random.randint(1, 11, 10)
print(tab_1)
print(tab_2)
print('Max z tab_1', np.max(tab_1))
print('Max z tab_2', np.max(tab_2))
print('Wynik działania z funkcji maksimum:')
print(np.maximum(tab_1, tab_2))