import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['c', 'b', 'f', 'd'])
print(data)

#Nadaj serii danych z poprzedniego ćwiczenia nowy indeks ['a', 'b', 'c', 'd', 'e', 'f']. ZapaA
#miętaj kopię serii jako new_data i wyświetl jej zawartość.

new_data = data.reindex(index= ['a', 'b', 'c', 'd', 'e', 'f'])
print(new_data)