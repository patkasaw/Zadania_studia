# Tworzenie serii danych o jawnym indeksie
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['c', 'b', 'f', 'd'])
print(data)

print(data['b'])

print(data['b':'d'])

data['c'] = 3.14
print(data)