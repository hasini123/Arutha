#import re
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
#from nltk import sent_tokenize,word_tokenize,pos_tag,RegexpParser,CFG
#from nltk.corpus import  brown
#from nltk.corpus #import treebank
#import nltk.corpus.treebank


w = input("Input the sinhala sentence: ") # For Python 3: use input() instead
x = w.split(" ")
#print (x[2])
for item in x:
    with open(r"C:\WinPython-64bit-3.4.3.7\wordsnew.txt", 'r',encoding='utf8') as f:
        found = False
        for line in f:
            k = line.split()
            if item in k: # Key line: check if `w` is in the line.
                s = k[1]
                #print(s,end=" ")
                text = word_tokenize(s)
                j = pos_tag(text)
                print(j,end=" ")
                
                
            
                
                
