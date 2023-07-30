import os
import sys
import csv
import datetime

import numpy as np

#fin = open(sys.argv[1], "r")
#fout = open(sys.argv[2], "w")

hhmm = []
dy = []
mm = []
yy = [] #yy - 1900
speed = []
direction = []
u = []
v = []
temp = []
p = []
conductivity = [] #(if present, len = 12)
seq = []

k = 0
print("k = ",k)
with open(sys.argv[1]) as csvfile:
  sreader = csv.reader(csvfile,delimiter=',')
  print("sreader = ",sreader)
  print("k = ",k)
  for line in sreader:
    #debug print(line, flush=True)
    if (k != 0):    
      hhmm.append(int(line[0]))
      dy.append(int(line[1]))
      mm.append(int(line[2]))
      yy.append(int(line[3])+int(1900))
      speed.append(float(line[4]))
      direction.append(float(line[5]))
      u.append(float(line[6]))
      v.append(float(line[7]))
      temp.append(float(line[8]))
      p.append(float(line[9]))
      if ( int(float(line[10])) != k):
        conductivity.append(float(line[10])) 
      seq.append(int(line[-1]))

    k += 1
    #debug print(seq[k],k, flush=True)

#debug print("k = ",k)
#debug print(len(seq),k)
#debug print(hhmm[int(k/2)])

#A couple of simple graphics:
import matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(seq, speed)
ax.grid()
plt.savefig("speed.png")

fig, ax = plt.subplots()
ax.plot(seq, temp)
ax.grid()
plt.savefig("temp.png")

#Some simple time series analysis -- Autoregressive
import statsmodels as sm
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.ar_model import ar_select_order

#for k in range(1,60):
#  amodel = AutoReg(speed, lags=k).fit()
#  print('k = ',k,' ',amodel.params, flush=True)
#amodel = AutoReg(speed, lags = 32).fit()
#amodel = AutoReg(speed, lags = [1,2,4,12,16, 21, 26] ).fit()
#amodel = AutoReg(speed, lags = [1, 2, 21, 32, 33, 145, 146, 315]).fit()
#amodel = AutoReg(speed, lags = [1, 2]).fit()

amodel = ar_select_order(speed, maxlag=51)
print("len: ",len(amodel.ar_lags))
print(amodel.ar_lags)
amodel = AutoReg(speed, lags = amodel.ar_lags).fit()
print("summary:\n")
print(amodel.summary(alpha=0.01))

amodel = ar_select_order(temp, maxlag=51)
print("len: ",len(amodel.ar_lags))
print(amodel.ar_lags)
amodel = AutoReg(temp, lags = amodel.ar_lags).fit()
print("summary:\n")
print(amodel.summary(alpha=0.01))


amodel = AutoReg(temp, lags = [1,18,3,4,11,2,12,6,14,8]).fit()
print("summary2:\n")
print(amodel.summary(alpha=0.01))

