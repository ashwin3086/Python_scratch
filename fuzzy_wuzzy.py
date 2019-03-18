from fuzzywuzzy import fuzz
import time

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

start_time = time.time()

for name_to_find in name_list:
    print ("Count is " + str(count))
    for name_master in name_list2:
        if fuzz.ratio(name_to_find,name_master) > 84:
            response[name_to_find] = [name_master , fuzz.token_sort_ratio(name_to_find,name_master)]
            break
    count=count+1

for key, [name,score] in response.items():
    print ("Name to find is ->" + key + " ---- Matching name is  -> " + name + " ---- Score is ->" + str(score))

end_time = time.time()

print ("Start Time is " + str(start_time))
print ("End Time is " + str(end_time))
print("--- %s seconds ---" % (end_time - start_time))
