import pandas as pd
import numpy as np

df = pd.read_csv('ex2.csv')
print(df)

df = pd.read_csv('ex2.csv', header=None)
print(df)

