with open('C:/Python27/input.txt') as f:
    for line in f:
        while line.count(',') < 2:
            another=f.readline()
            line = another + line
        print line
            
with open('C:/Python27/input.txt') as f:
    while True:
        line = f.readline()
        if not line: break
        while line.count(',') < 2:
            another=f.readline()
            print another
            line =  line + another
            print line
            
        print line
        
        