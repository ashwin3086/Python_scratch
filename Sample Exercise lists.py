

 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
float_values=[]
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    
    
    colon_prefix= line.find(" ")
    float_value=line[colon_prefix:26].lstrip()
    float_values.append(float_value)
    
print "Done"

print float_values
float_values1=map(float,float_values)


tot=0.0

for i in float_values1:
    tot = tot + i
    avg=tot / float(len(float_values1))
    
#print sum 
print "Average spam confidence: " + str(avg)

#print reduce(lambda x , y: x + y,float_values1) / len (float_values)
#print avg
