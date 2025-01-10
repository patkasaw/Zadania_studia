# Indeksowanie ramek danych
import pandas as pd

states = pd.DataFrame(columns=['state', 'population'])

states['state'] = ['California', 'Texas', 'New York', 'Florida', 'Illinois']
states['population'] = [38332521, 26448193, 19651127, 19552860, 12882135]
states['area'] = [423967, 170312, 149995, 141297, 695662]
states['density'] = states['population'] / states['area']

states.set_index('state', inplace=True)

print(states)

# Dla ramki danych z ćwiczenia 25, zawierającej informacje o stanach USA, ich powierzchni oraz liczby
# ludności, wyświetl na ekranie informację o powierzchni stanu New York. Skorzystaj zarówno z indekA
# sów jawnych, jak i niejawnych (domyślnych)

print(states['area']['New York'])

print(states['area'][2])

# Z ramki danych states z ćwiczenia 25 wybierz kolumny, zawierające informacje o liczbie ludności
# i gęstości zaludnienia, wyświetlając je na ekranie.
print(states[['population', 'density']])

# Z ramki danych states z ćwiczenia 25 wybierz kolumny, zawierające informacje o stanach USA od
# Teksasu po Florydę.
print(states['Texas':'Florida'])

print(states[1:4])

#Użycie indeksatorów do ramki danych
print(states.loc['New York', 'area'])
print(states.iloc[2,1])

# Użycie indeksatorów do ramki danych (c.d.)
print(states.loc['Texas':'Florida', ['population', 'density']])

print(states.iloc[1:4, [0, 2]])

# Dodawanie nowego wiersza do ramki danych
states.loc['Alaska'] = {'population': 738430, 'area': 665384,
                        'density': 738430 / 665384}

print(states)
