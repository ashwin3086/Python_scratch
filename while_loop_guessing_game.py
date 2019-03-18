tries = 1
answer="delhi"
while tries<=3:
    print("what is the capital of india")
    response=raw_input()
    tries=tries+1
    if (response=="delhi"):
        print("Correct")
        break
    else:
        if ((tries-1) <> 3):
            print("Sorry.Try Again ..." + str(tries -1) + " over :(  ")
        else:
            print("Sorry.All " + str(tries -1) + " over :(  ")
        
        
       # print("Sorry try again") 