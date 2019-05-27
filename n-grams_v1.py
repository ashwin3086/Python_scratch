'''
input_list = ['all', 'this', 'happened', 'more', 'or', 'less']
def find_bigrams(i_list):
    return zip(input_list, input_list[1:])
output=list(find_bigrams(input_list))
print (output )
'''

'''

import os
print(os.getcwd())
infile=open('text.txt','r')
for line in infile:
    print (line.strip())
infile.close()
'''


import nltk
import os
import re
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TweetTokenizer
print('hello-1')

def find_bigrams(i_list,n):
    return zip(*[i_list[i:] for i in range(n)])




f=open('text.txt','r')
infile=f.read().replace('\'','').replace('.','').lower()

tokenizer=RegexpTokenizer('\w+|\$[\d\.]+|\S+')
tokens=tokenizer.tokenize(infile)
print(tokens)
output=list(find_bigrams(tokens,3))
print(output)
all_words = nltk.FreqDist(output)
print(all_words.most_common(10))
