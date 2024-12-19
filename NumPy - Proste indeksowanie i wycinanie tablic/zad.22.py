# Modyfikacja fragmentu tablicy
import numpy as np 
tablica_2d = np.arange(1, 26).reshape(5, 5)
tablica_2d[1, :] = 99
tablica_2d[:, 2] = 99
print(tablica_2d)