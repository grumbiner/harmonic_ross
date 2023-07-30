import os
import sys
import csv

fin = open(sys.argv[1], "r")
fout = open(sys.argv[2], "w")
# Indices:
hhmm = 0
dy = 1
mm = 2
yy = 3
speed = 4
direction = 5
u = 6
v = 7
t = 8
p = 9
conductivity = 10 #(if present, len = 12)
#seq = [-1]

k = 0
for line in fin:
  if (k == 0):
    print(line, file=fout,end="")
  else:
    words = line.split()
    if (len(words) == 0):
      continue
    #debug: print(line,flush=True)
    #debug: print(k,len(line), len(words), flush=True )

    for l in range(0,len(words)-1):
      print(words[l].strip(),",",sep="",end="", file=fout)
    print(words[len(words)-1].strip(),sep="",file=fout)

  k += 1
  
#310 METERS AT CRACKLE, (PRISM).  FEB 83 - JAN 84.  TAPE 1499/8.
#1103  5  2 83  4.8 295  -4.4   2.0  -1.26  312.7     1        
