# Czytanie zawartości pliku CSV do ramki danych
import pandas as pd
df = pd.read_csv('ex1.csv')
print(df)
print('-----------------------------')
print(df.dtypes)

#Skonwertuj dane w kolumnie message powyższej ramki danych na typ string. Wyświetl typy danych
#w tak zmodyfikowanej ramce.
df['message'] = df['message'].astype('string')
print(df.dtypes)

# Wyspecyfikuj typ danych w kolumnie message jako string w trakcie wczytywania powyższej ramki
# danych. Wyświetl typy danych w tak wczytanej ramce.
df = pd.read_csv('ex1.csv', dtype = {'message':'string'})
print(df.dtypes)