#!/usr/bin/env python
# -*- coding: utf-8 -*-
#3-gram version

import re
from collections import defaultdict

#text = open('./result/1.txt').read()
text=open('obama.txt').read()
text = re.sub('\n',' ',text)
text = re.sub('&quot;',' ',text)

splts = text.split()
splts = [splt.lower() for splt in splts]
nsplts=[]

for i in xrange(len(splts)-2):
    nsplts+=[(splts[i],splts[i+1],splts[i+2])]
print nsplts

splts=nsplts

#set_splts=set(splts)#emit the doubling

d = defaultdict(int)
for splt in splts:
    d[splt] += 1
#print d.items()

x= sorted(d.items(), key=lambda a:a[1],reverse=True)
for k,v in x[:50]:
    print '%s\t%s\t' % (str(k),v)
    
