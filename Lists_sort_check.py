fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l_new=line.rstrip()
    ll_new=l_new.split()
  
    
    for word in range(len(ll_new)):
        #print ll_new[word]
        if ll_new[word] not in lst:
            lst.append(ll_new[word])
        ans=sorted(lst) 
        
print ans
        

