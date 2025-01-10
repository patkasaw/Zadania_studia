import pandas as pd

area_dict = {'California': 423967,
 'Texas': 695662,
 'New York': 141297,
 'Florida': 170312,
 'Illinois': 149995}

area = pd.Series(area_dict)
print(area)
