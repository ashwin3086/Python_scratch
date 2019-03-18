# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:
    text=line.rstrip().upper()
    print text 
