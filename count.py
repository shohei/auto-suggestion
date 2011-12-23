#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from eparser import Parser 
from collections import defaultdict
import glob


p = Parser()

files = glob.glob('./result/*')
print files

for i in xrange(len(files)):
#for f in files
    text = open('./result/'+str(i)+'.txt').readlines()
    #text = open(f).readlines()
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
    #print splts

    #set_splts=set(splts)#emit the doubling

    d = defaultdict(int)
    splts = [splt.lower() for splt in splts]
    for splt in splts:
        d[splt] += 1
        #print d.items()

    x= sorted(d.items(), key=lambda a:a[1],reverse=True)
    output=open('./output/'+str(i)+'output.txt','w')
    for k,v in x:
         #print '%s\t%s\t' % (str(k),v)
         #output.write('%s\t%s\t' % ("\t".join(k),v))
         output.write('%s\t%s\n' % (str(k),v))
    output.close()
    
