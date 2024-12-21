#  Funkcje trygonometryczne
import numpy as np
katy = np.pi  / np.arange(6, 0, -1)
sinus = np.sin(katy)
cosinus = np.cos(katy)
tangens = np.tan(katy)
print(np.square(sinus) + np.square(cosinus))
print(sinus > cosinus)