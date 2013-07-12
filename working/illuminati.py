#!/usr/bin/env python

import string
import csv
from collections import defaultdict

def partial_sums(iterable):
    total = 0
    for i in iterable:
        total += i
        yield total

x = [ord(c) for c in "The password is EARLTEAGREY.".encode('rot13')]
print x

t = list(partial_sums(partial_sums(x)))
print t

#Track  Time    Event           Channel Pitch   Velocity
#1	124	 Note_on_c	0	79	0

track = 1
event = 'Note_on_c'
channel = 11
velocity = 11


with open('/Users/josh/Dropbox/PRISM/CodeWars2013/illum.csv','wb') as f:
    w = csv.writer(f)
    for z,y in zip(x,t):
        w.writerow([track, y, event, channel, z, velocity])


combined = defaultdict(list)

with open('/Users/josh/Dropbox/PRISM/CodeWars2013/illum.csv','rb') as f:
    fr = csv.reader(f)
    for row in fr:
        combined[int(row[1])].append(row)
    
with open('/Users/josh/Dropbox/PRISM/finty.csv','rb') as g: 
    gr = csv.reader(g)
    for row in gr:
        combined[int(row[1])].append(row)

times = sorted(combined.keys())
    
with open('/Users/josh/Dropbox/PRISM/CodeWars2013/illuminati.csv','wb') as o:
    ow = csv.writer(o)
    for t in times:
        for row in combined[t]:
            ow.writerow(row)
            
# Prove that the encoding is reversible.
s = ''
with open('/Users/josh/Dropbox/PRISM/CodeWars2013/undo.csv','rb') as u:
    ur = csv.reader(u)
    for row in ur:
        if len(row) > 3 and int(row[3]) == 11:
            s += chr(int(row[4]))
print s.encode('rot_13')