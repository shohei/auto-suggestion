#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, os.path

from BeautifulSoup import BeautifulSoup, NavigableString, Declaration, Comment

def getNavigableStrings(soup):
  if isinstance(soup, NavigableString):
    if type(soup) not in (Comment, Declaration) and soup.strip():
      yield soup
  elif soup.name not in ('script', 'style'):
    for c in soup.contents:
      for g in getNavigableStrings(c):
          yield g

path = '/Users/shohei/pytest/www.instructables.com/id/'
i = 0
for root, dirs, files in os.walk(path):
    for file in files:
        if file == "index.html":
            filename = os.path.join(root, file)
            print i
            
            article = open(filename, 'r')
            data = article.read()
            if not data:continue

            soup = BeautifulSoup(data)
            titleTag = soup.html.head.title
            atitle = titleTag.string #atitle shows the title of the article
            txts = soup.findAll(attrs={'class':'txt'})
       
            fout = open("./result/"+str(i)+'.txt','w')
            fout.write(filename+'\n')
            
            if not atitle:continue
            fout.write(atitle+"\n")
            for txt in txts:
                fout.write('\n'.join(getNavigableStrings(txt)))
                fout.write('\n\n')
            fout.close()
            i+=1
