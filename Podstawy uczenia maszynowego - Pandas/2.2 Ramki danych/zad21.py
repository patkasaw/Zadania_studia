import numpy as np
import pandas as pd

df = (pd.DataFrame(np.random.rand(3,2), dtype = 'float32'))
print(df)
df.info()