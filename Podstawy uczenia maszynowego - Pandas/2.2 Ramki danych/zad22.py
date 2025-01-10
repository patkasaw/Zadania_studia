import pandas as pd
import numpy as np

dict = {'state': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
        'population' : np.array([38332521, 26448193, 19651127, 19552860, 1288213]),
        'area' : np.array([423967, 170312, 149995, 141297, 695662])}

states = pd.DataFrame(dict)
print(states)

