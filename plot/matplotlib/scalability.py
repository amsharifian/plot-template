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
df = pd.read_csv('../../data/cilk_for_test09_sweep4.csv')
#df.iloc[1:5,:] = df.iloc[1:5,:].applymap(lambda x: (300.0 / x)*50)
#df.iloc[1,1:5] = df.iloc[1,1:5].multiply(df.iloc[1,0])
#df.iloc[2,1:5] = df.iloc[2,1:5].multiply(df.iloc[2,0])
#df.iloc[3,1:5] = df.iloc[3,1:5].multiply(df.iloc[3,0])
#df.iloc[4,1:5] = df.iloc[4,1:5].multiply(df.iloc[4,0])
#df.iloc[5,1:5] = df.iloc[5,1:5].multiply(df.iloc[5,0])
#df.iloc[6,1:5] = df.iloc[6,1:5].multiply(df.iloc[6,0])
#df = df.iloc[1:5,:]

fig, ax = plt.subplots()
plt.xticks(np.arange(0,6,step=1.0),rotation=90)
plt.tick_params(axis='both', which='major', labelsize=30)
#plt.xlim(0, 51)

#N = len(df['Adders'])
#ind = np.arange(N)
# width = 0.8

#majorLocator = MultipleLocator(0.2)
#minorLocator = MultipleLocator(0.2)
# majorFormatter = FormatStrFormatter('%d')
#ax.xaxis.set_major_locator(majorLocator)
#ax.xaxis.set_minor_locator(minorLocator)
# ax.xaxis.set_major_formatter(majorFormatter)

# Instantiating the X bar
# cbars = ax.bar(ind+0.8, df['mul'].values.tolist(), \
#                width, ecolor='k', color=u.getcolor(3), edgecolor='k');
# cbars = ax.bar(ind+0.8, df['data'].values.tolist(), width)

ms = 10

#plt.plot('Tiles', 'a', data=df, linestyle=':', marker='<', markersize=ms,  color='black', linewidth=2, label='1 adder')
plt.plot('Tiles', 'b', data=df, linestyle='solid', marker='d', markersize=20, color='#332288', linewidth=4, label='10 adders')
plt.plot('Tiles', 'c', data=df, linestyle='solid', marker='^', markersize=20, color='#88CCEE', linewidth=4, label='20 adders')
plt.plot('Tiles', 'd', data=df, linestyle='solid', marker='*', markersize=20, color='#CC6677', linewidth=4, label='30 adders')
plt.plot('Tiles', 'e', data=df, linestyle='solid', marker='h', markersize=20, color='#882255', linewidth=4, label='40 adders')
plt.plot('Tiles', 'f', data=df, linestyle='solid', marker='o', markersize=20, color='#AA4499', linewidth=4, label='50 adders')
plt.plot('Tiles', 'g', data=df, linestyle='-.', marker='o', markersize=15, color='#117733', linewidth=4, label='Software')
plt.legend(loc='upper left', fontsize=24)

# ax.color_cycle    : 332288, 88CCEE, 44AA99, 117733, 999933, DDCC77, CC6677, 882255, AA4499

#for n in np.arange(len(df['Tiles'])):
#    myscatter = ax.scatter(df['Adders'][n], df['Cycles'][n], s=[350], marker=ms[n])

#for n in np.arange(len(df['Tiles'])):
#    ax.text(df['Area'][n]-0.06, df['Adders'][n]-0.07, df['Cycles'][n], fontsize=16)

# Put limit on Y axis
#plt.ylim(0, 22)
plt.xlim(0.7, 5.2)

# Set X label values
ax.set_ylabel('Performance (Million Adds/s)',fontsize=32)
ax.set_xlabel('Worker Tiles',fontsize=32)
# ax.set_xticks(ind+0.8);
#ax.set_yscale('log')
# Put the labels from 'app' coulmn
# ax.set_xticklabels(u.rename(df['name']))
#ax.set_facecolor('white')

plt.gca().xaxis.grid(True, color='gray')
plt.gca().yaxis.grid(True, color='gray')

plt.tick_params( axis='x', which='both', bottom='on', top='off', width=2, length=6)
plt.tick_params( axis='y', which='both', right='off' )

ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['left'].set_color('black')

# Saving the plot
fig.savefig('scalability.pdf',facecolor=fig.get_facecolor(), bbox_inches='tight')
