import numpy as np
import matplotlib.pyplot as plt
import math
from math import log
from matplotlib.ticker import NullFormatter


input_file = "./resultsCleaner.txt"

fileCleaned = open(input_file,"r")

listeOfFreqs = []

Lines = fileCleaned.readlines()
 
# Strips the newline character
#previousValue = 0
for line in Lines:
    linesSplitted = line.split(',')
    freq = linesSplitted[0]
    #if freq!=previousValue:
    listeOfFreqs.append(freq)
        #previousValue = freq
    
    
l = list(reversed(range(1,56652))) 
# print (math.log(l(2)))
llog = []
for i in l:
    x = math.log(int(i))
    llog.append(x) 


listeOfFreqsLog = []
for f in listeOfFreqs:
    x = math.log(int(f))
    listeOfFreqsLog.append(x)

ax = plt.axes()
plt.plot(llog,listeOfFreqsLog)
# plt.xscale("log")
# plt.yscale("log")
# setting ticks for y-axis
#ax.set_yticks([100,200,300,400,500,600,700,800,900,1000,1100])
plt.show()
