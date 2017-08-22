# %matplotlib inline
import sys
sys.path.append('../utils')
import utils as u
import math

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# Plot type
matplotlib.style.use('ggplot')

# Loading input DataFrame
# index_col option mention the column name
#
# Example of generating random data
#   df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])

input_data = pd.read_csv('../data/01-test.csv', index_col='name')
input_data.plot.bar()
# input_data.plot.bar(stacked=True)




# df.plot.bar(stacked=True);

plt.show()
