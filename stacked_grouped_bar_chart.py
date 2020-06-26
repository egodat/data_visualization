# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
 
# y-axis in bold
rc('font', weight='bold')

# set width of bar
barWidth = 0.25
 
# set height of bar
barsb1 = [12, 6]
barsb2 = [28, 16]
barsb3 = [29, 24]

barst1 = [12, 28]
barst2 = [28, 7]
barst3 = [25, 3]


# Set position of bar on X axis
r1 = np.arange(len(barsb1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot
plt.bar(r1, barsb1, color='darkblue', width=barWidth, edgecolor='white', label='var1a')
plt.bar(r2, barsb2, color='darkred', width=barWidth, edgecolor='white', label='var2a')
plt.bar(r3, barsb3, color='darkgreen', width=barWidth, edgecolor='white', label='var3a')

plt.bar(r1, barst1, bottom=barsb1,color='blue', width=barWidth, edgecolor='white', label='var1b')
plt.bar(r2, barst2, bottom=barsb2, color='red', width=barWidth, edgecolor='white', label='var2b')
plt.bar(r3, barst3, bottom=barsb3, color='green', width=barWidth, edgecolor='white', label='var3b')
 
# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B'])
 
# Create legend & Show graphic
plt.legend()
plt.show()
