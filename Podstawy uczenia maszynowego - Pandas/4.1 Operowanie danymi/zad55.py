import pandas as pd

df = pd.read_csv('ex4.csv')
df.to_csv('ex4_out.csv')

df2 = pd.read_csv('ex4_out.csv')
print(df2)

df.to_csv('ex4_out.csv', index=False)
