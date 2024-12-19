#Wycinanie fragmentu tablicy dwuwymiarowe
import numpy as np
tablica_2d = np.arange(1,17).reshape(4,4)
wycinek = tablica_2d[1:3, 2:4]
print(tablica_2d)
print(wycinek)