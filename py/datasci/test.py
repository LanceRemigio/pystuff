import numpy as np
import pandas as pd
from numpy.random import randn


data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'], 
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)


byComp = df.groupby('Company').describe()
print(byComp)



