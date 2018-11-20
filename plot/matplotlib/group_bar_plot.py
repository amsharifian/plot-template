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
from random import randint
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_pdf import PdfPages

# Plot type
plt.style.use('ggplot')

matplotlib.pyplot.style.use('default')
# pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (30, 9)
mpl.rc('font', family='serif')
mpl.rcParams['xtick.major.pad']= '12'
mpl.rcParams['ytick.major.pad']= '8'

df = pd.read_csv('../../data/04-test.csv')

fig, ax = plt.subplots()
plt.xticks(rotation=90)
plt.tick_params(axis='both', which='major', labelsize=30)

# Set limits for X and Y axises
# plt.xlim(-0.5, 10.5)
plt.ylim(0, 50)


N = len(df['name'])
ind = np.arange(N)
width = 0.4

c = -1
for x in np.arange(N):
   if(x%2 == 0):
       c = c + 1
   ind[x] = c
   c = c + 1

# print(ind)

# bar.hatch -> puting patterns on the colors
opbars = ax.bar(ind, df['ColA'].values.tolist(), width, ecolor='k',
        color='white', edgecolor='k', hatch='//');

opbars = ax.bar(ind, df['ColB'].values.tolist(), width, ecolor='k',
        color='black', edgecolor='k');


ax.set_ylabel('Y Label',fontsize=32)
ax.set_xticks(ind);

# Adding extra name to the x labels
# rotation='degree' for rotating the text
ax.set_xticklabels(df['name'])
t = 10
ax.text(2, -1.5, '|', fontsize=20)
ax.text(2, -3.5, '|', fontsize=20)
ax.text(2, -5.5, '|', fontsize=20)
ax.text(2, -7.5, '|', fontsize=20)


ax.text(5, -1.5, '|', fontsize=20)
ax.text(5, -3.5, '|', fontsize=20)
ax.text(5, -5.5, '|', fontsize=20)
ax.text(5, -7.5, '|', fontsize=20)


ax.text(0.2, -7.5, 'This is test', fontsize=16)
ax.text(3.2, -7.5, 'This is test', fontsize=16)
ax.text(6.2, -7.5, 'This is test', fontsize=16)

# Set the background color
# ax.set_facecolor('white')

plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True, color='black')

plt.tick_params( axis='x', which='both', bottom='off', top='off')
plt.tick_params( axis='y', which='both', right='off' )

ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['left'].set_color('black')

# Adding legend and the position
# ax.legend((pbars[0], opbars[0], cbars[0], prec[0]), ('A', 'B', 'C', 'D'), bbox_to_anchor=(1, 0.92), fontsize=22)

fig.savefig('test.pdf',facecolor=fig.get_facecolor(), bbox_inches='tight')
