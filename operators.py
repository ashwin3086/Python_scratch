'''
print ("test operators")
print(100 == 100)

print('a' == 'q')
print(100< 1)

#Adding a comment


hw=39
salary=39000
print((hw>20) and (salary<=60000))
'''

'''
#calculate GRoss pay 
hoursworked=45
rate=25
if (hoursworked>40):
    Grosspay=((40*rate) + ((hoursworked-40)*1.5))
else:
    Grosspay=((40*rate))
print("Grosspay is :" + str(Grosspay))
'''

# Guessing game
'''
answer="India"
print("IT is a game to guess the country. You have 3 tries")
print("which country's capital is Delhi?")
response  = raw_input()
if response == answer:
    print("You are correct")
else:
    print("You are wrong. 2nd chance ... ")
    response=raw_input()
    if response == answer:
        print("You are correct")
    else:
        print("Sorry. Last chance...")
        response=raw_input()
        if response == answer:
            print("You are correct")
        else:
            print("Sorry . No more chances. Answer is " + answer )
                
'''

#Recommended activity


message="The recommended activity is "
print("enter the temperature")
temp=int(raw_input())
if temp < 60:
    message = message + " swimming "
elif temp > 60:
    message = message + " golf"

print (message)
            


# test while loop with continue
            
            
    

