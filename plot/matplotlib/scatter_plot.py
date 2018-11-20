# %matplotlib inline
import sys
sys.path.append('../../utils')
import utils as u
import math

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# Plot type
plt.style.use('ggplot')

#Seting plot fontsize and font family
# pd.set_option('display.mpl_style', 'default')
matplotlib.pyplot.style.use('default')
plt.rcParams['figure.figsize'] = (15, 9)
mpl.rc('font', family='serif')
mpl.rcParams['xtick.major.pad']= '12'
mpl.rcParams['ytick.major.pad']= '8'

#Loading data
df = pd.read_csv('../../data/05-test.csv')

fig, ax = plt.subplots()
plt.xticks(rotation=90)
plt.tick_params(axis='both', which='major', labelsize=30)
plt.xlim(-0.5, 10)

N = len(df['name'])
ind = np.arange(N)
# width = 0.8

majorLocator = MultipleLocator(0.2)
minorLocator = MultipleLocator(0.2)
# majorFormatter = FormatStrFormatter('%d')
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_minor_locator(minorLocator)
# ax.xaxis.set_major_formatter(majorFormatter)

# Instantiating the X bar
# cbars = ax.bar(ind+0.8, df['mul'].values.tolist(), \
#                width, ecolor='k', color=u.getcolor(3), edgecolor='k');
# cbars = ax.bar(ind+0.8, df['data'].values.tolist(), width)

ms = ['+', '*', 'o']

for n in np.arange(len(df['name'])):
    myscatter = ax.scatter(df['Area'][n], df['Power'][n], s=[350], marker=ms[n])

for n in np.arange(len(df['name'])):
    ax.text(df['Area'][n]-0.06, df['Power'][n]-0.07, df['name'][n], fontsize=16)

# Put limit on Y axis
plt.ylim(0, 1.1)
plt.xlim(0, 1.1)

# Set X label values
ax.set_ylabel('Y LABEL',fontsize=32)
# ax.set_xticks(ind+0.8);

# Put the labels from 'app' coulmn
# ax.set_xticklabels(u.rename(df['name']))
ax.set_facecolor('white')

plt.gca().xaxis.grid(True, color='gray')
plt.gca().yaxis.grid(True, color='gray')

plt.tick_params( axis='x', which='both', bottom='on', top='off', width=2, length=6)
plt.tick_params( axis='y', which='both', right='off' )

ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['left'].set_color('black')

# Saving the plot
fig.savefig('test.pdf',facecolor=fig.get_facecolor(), bbox_inches='tight')
