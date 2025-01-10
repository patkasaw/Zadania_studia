import pandas as pd

df = pd.read_csv('ex2.csv', names =[ 'a', 'b', 'c', 'd', 'message'], index_col='message')
print(df)