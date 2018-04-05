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
plt.style.use('ggplot')

#Seting plot fontsize and font family
# pd.set_option('display.mpl_style', 'default')
matplotlib.pyplot.style.use('default')
plt.rcParams['figure.figsize'] = (15, 9)
mpl.rc('font', family='serif')
mpl.rcParams['xtick.major.pad']= '12'
mpl.rcParams['ytick.major.pad']= '8'

#Loading data
df = pd.read_csv('../data/tile_ins.csv')


fig, axes = plt.subplots(2,2)

name = ['1 (Tile) -> 1 (Ins)','1 (Tile) -> 50 (Ins)','10 (Tile) -> 1 (Ins)','10 (Tile) -> 50 (Ins)']

for i, ax in enumerate(axes.flatten()):
    # ax.pie(df[name[i]], labels=df['labels'].values.tolist(), autopct='%1.0f%%', shadow=True, startangle=90)
    ax.pie(df[name[i]], autopct='%1.0f%%', shadow=True, startangle=90)
    ax.set_title(name[i], y= -0.1)
    ax.axis('equal')

plt.legend(loc='upper left')

# plt.xticks(rotation=90)
# plt.tick_params(axis='both', which='major', labelsize=30)
# plt.xlim(-0.5, 10)

# N = len(df['app'])
# ind = np.arange(N)
# width = 0.8


# Instantiating the X bar
# cbars = ax.bar(ind+0.8, df['mul'].values.tolist(), \
#                width, ecolor='k', color=u.getcolor(3), edgecolor='k');
# cbars = ax.bar(ind+0.8, df['data'].values.tolist(), width)
# cbars = ax.pie(ind, df['data'].values.tolist(), width)

# Put limit on Y axis
# plt.ylim(0, 60)

# Writing text on top of the bars
# c = 0
# ll = df['data'].values.tolist()
# for t in df['data']:
#     if(int(t) > 50):
#         ax.text(c+0.65, 62+0.2, str(int(t)), fontsize=18, rotation=0)
#     else:
#         ax.text(c+0.65, ll[c]+0.2, str(int(t)), fontsize=18, rotation=0)
#     c += 1

# Set X label values
# ax.set_ylabel('Y LABEL',fontsize=32)
# ax.set_xticks(ind+0.8);

# Put the labels from 'app' coulmn
# ax.set_xticklabels(u.rename(df['app']))
# ax.set_facecolor('white')

# plt.gca().xaxis.grid(False)
# plt.gca().yaxis.grid(True, color='black')

# plt.tick_params( axis='x', which='both', bottom='off', top='off')
# plt.tick_params( axis='y', which='both', right='off' )

# ax.spines['bottom'].set_color('black')
# ax.spines['top'].set_color('black')
# ax.spines['right'].set_color('black')
# ax.spines['left'].set_color('black')

# Saving the plot
plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=None)


fig.savefig('test.pdf',
            facecolor=fig.get_facecolor(), bbox_inches='tight')
