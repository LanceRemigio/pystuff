import pandas as pd
import numpy as np
from plotly import __version__

import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
cf.go_offline()

df = pd.DataFrame(np.random.randn(100,4), columns = 'A B C D'.split())

df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32,43,50]})

df.iplot()

