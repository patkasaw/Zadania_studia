# np.ceil(), np.floor(), np.round()
import zad28
import numpy as np
diff = np.abs(zad28.tab_2 - zad28.tab_1)
print(diff)
print(np.ceil(diff))
print(np.floor(diff))
print(np.round(diff))