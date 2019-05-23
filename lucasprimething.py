import math
def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def Lucas(x):
    if (x == 1):
        return 1
    elif (x == 2):
        return 3
    else:
        return Lucas(x - 1) + Lucas(x - 2)
count = 0;
luc_list = []
for i in range(1, 50):
    luc_list.append(Lucas(i))
for j in range(len(luc_list)):
    if isPrime(luc_list[j]) == True:
        count = count + 1
prob = (count / len(luc_list))
print (count)
print (len(luc_list))
print (luc_list)
print (prob)
    





    
