import sys, pprint, re, operator
from functools import reduce

# Colorbrewer divergent
color_palette = ['#d7191c','#fdae61','#ffffbf', \
	 '#abdda4','#2b83ba', '#acacac']

# Tableau 10 palette (reordered)
# color_palette = [  \
# 	# Blue  
# 	'#4e79a7', \
# 	# Red
# 	# '#c15759', \
#         '#ab6267', \
# 	# Cyan
# 	# '#76b7b2', \
#         '#48a3ba', \
# 	# Green
# 	'#59a14f', \
# 	# Purple
# 	'#b07aa1', \
# 	# Orange
# 	'#f28e2b', \
# 	# Yellow
# 	'#edc948', \
# 	'#ff9da7', \
# 	'#9c755f', \
# 	'#bab0ac']

# Tableau 10 palette (original)
# color_palette = [  \
	# '#4e79a7', \
	# '#f28e2b', \
	# '#c15759', \
	# '#76b7b2', \
	# '#ff9da7', \
	# '#9c755f', \
	# '#59a14f', \
	# '#edc948', \
	# '#b07aa1', \
	# '#bab0ac']


def getcolor(idx):
    global color_palette
    return color_palette[idx] 

def getpalette():
    global color_palette
    return color_palette

def rename(names):
    regex = re.compile("^\d+\.")
    names = [regex.sub('', s) if s.strip() not in ('181.mcf', '429.mcf') else s for s in names ]
    names = [s[:9] for s in names] 
    return names 

def gm(iterable):
    return (reduce(operator.mul, iterable)) ** (1.0/len(iterable))

if __name__ == "__main__":
    rename([sys.argv[1]]*5)
