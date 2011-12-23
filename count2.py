#!/usr/bin/env python
# -*- coding: utf-8 -*-
#2-gram version

import re
from eparser import Parser
from collections import defaultdict

p = Parser()

for i in xrange(200):

    text = open('./result/'+str(i)+'.txt').readlines()
    text = text[2:]
    text = "\n".join(text)
    text = re.sub('\n',' ',text)
    text = re.sub('&quot;',' ',text)
    text = re.sub('\.','',text)
    text = re.sub(',',' ',text)
    text = p.clean(text)

    #splts = text.split()
    splts = p.tokenise(text,stem=True)
    splts = p.removeStopwords(splts)
    splts = [splt.lower() for splt in splts]
    nsplts=[]
    for i in xrange(len(splts)-1):
        nsplts+=[(splts[i],splts[i+1])]
        #print nsplts
    splts=nsplts

    #set_splts=set(splts)#emit the doubling

    d = defaultdict(int)
    for splt in splts:
        d[splt] += 1
        #print d.items()

    x= sorted(d.items(), key=lambda a:a[1],reverse=True)
    output=open('./output/2-gram/'+str(i)+'output.txt','w')
    for k,v in x:
        #print '%s\t%s\t' % (str(k),v)
        output.write('%s\t%s\n' % ("\t".join(k),v))
    output.close()
