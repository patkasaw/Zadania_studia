import pandas as pd

states = pd.DataFrame(columns=['state', 'population'])
states['state'] = ['California', 'Texas', 'New York', 'Florida', 'Illinois']
states['population'] = [38332521, 26448193, 19651127, 19552860, 1288213]

print(states)

states['area'] = [423967, 170312, 149995, 141297, 695662]
states['density'] = states['population'] / states['area']
print(states)

states.set_index('state', inplace=True)
print(states)

states.reset_index(inplace=True)
print(states)

states1 = states.reset_index()
print(states1)