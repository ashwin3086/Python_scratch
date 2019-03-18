from fuzzywuzzy import process

from fuzzywuzzy import fuzz
infile=open('names_to_find.txt','r')
name=infile.readline()
name_list=[]
while name:
    name_list.append(name.strip())
    name=infile.readline()

print (name_list)

infile2=open('master_names.txt','r')
name2=infile2.readline()
name_list2=[]
while name2:
    name_list2.append(name2.strip())
    name2=infile2.readline()

print (name_list2)
count=0
response = {}
for name in name_list:
    print ("Count is " + str(count))
    matches = filter(lambda x  : x[1] > 82, process.extract(name, name_list2, limit=98000))
    for match_name, score in matches:
        print(name + " <--> " + match_name + " <--->" + str(score ))
        response[match_name] = name
    count=count+1

