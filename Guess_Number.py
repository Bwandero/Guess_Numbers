import random
num = random.randint(0,100)
num1=-1

while num1 != num:
    num1 =int(input("Guess a number between 0 and 100 " ))
    if num1 > num:
        print ("Sorry  but %r is too high" %(num1))
    elif num1<num:
        print ("Sorry but  %r is too low"%(num1))
    elif num1==num:
        print ("YES! You've got it.The number was %r"%(num1))
    else:
        print ("invalid")

