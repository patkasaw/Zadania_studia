# np.abs()
import numpy as np
import random
tab_1 = [i + random.random() for i in range(10)]
tab_2 = [i + random.random() for i in range(1,11)]

tab_1 = np.array(tab_1)
tab_2 = np.array(tab_2)
np.abs(tab_2 - tab_1)

# Można też wygenerować tablice tab_ i tab_2 w nieco inny sposób:
tab_1 = np.arange(10) + np.random.random(10)
tab_2 = np.arange(1, 11) + np.random.random(10)