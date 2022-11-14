'''You have to enter a range[A,B] and sysytem will randomly pick any number
from your given range and check the status of the given number
the properties to be checked are:
1. is that number odd or even
2. is that number is positive or negative
3. is that number is prime or composite number'''

import random
a=(random.sample(range(1,10),1))
print("selected number is",a)

for i in a:
    if i%2==0:
        print("It is an even number")
    else:
        print("It is an odd number")

for i in a:
    if i>0:
        print("It is a positive number")
    else:
        print("It is a negative number")

for i in a:
    if i==1:
        print("It is neither prime nor composite")
    else:
        for divisor in range(2,(i//2)+1):
            if i%divisor == 0: 
                print("It is a composite number")
                break
        else:
            print("It is a prime number")
    
 
    
