import numpy as np
import pandas as pd

print(pd.DataFrame(np.random.rand(3,2), columns=['foo', 'bar'], index=['a', 'b', 'c']))