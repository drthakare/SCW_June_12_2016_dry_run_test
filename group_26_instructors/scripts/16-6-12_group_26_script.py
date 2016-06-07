'''
Authors: ...

This is a completed script for the purpose of being a demo
'''
import matplotlib, numpy as np, matplotlib.pyplot as plt
import pandas as pd

dats = pd.read_csv('../raw_data/gapminder-FiveYearData.csv')

zim_dats = dats[dats['country']=='Zimbabwe']
alg_dats = dats[dats['country']=='Algeria']

fig = plt.figure(12, figsize=(6,2), dpi=150)
fig.clear()

#
# Zimbabwe life expectancy over time scatter
#
ax = fig.add_subplot(1,2,1)
ax.plot(zim_dats['year'],zim_dats['lifeExp'], 'ro')
ax.set_xlabel('Year')
ax.set_ylabel('Life Expectancy')

#
# Disease association versus publications
#
ax = fig.add_subplot(1,2,2)
ax.hist(list(alg_dats['pop']))
ax.set_xlabel('Population')
ax.set_ylabel('Frequency')

fig.tight_layout()

fig.text(0.01, 0.98, 'A', va='top', ha='left', fontsize=12)
fig.text(0.49, 0.98, 'B', va='top', ha='left', fontsize=12)

fig.show()




















