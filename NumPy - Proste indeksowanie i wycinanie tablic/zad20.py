# Wycinanie tablicy wielowymiarowej
import numpy as np
tablica_3 = np.random.randint(0,10, size = (4, 4, 3))
druga_warstwa = tablica_3[:, :, 1]
print(tablica_3)
print(druga_warstwa)