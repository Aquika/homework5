import math



i = 10000000
f1 = f2 = 1
fiblist = [f1, f2]
templist = []
num = 0
for i in range(f2, i):
    f1, f2 = f2, f1 + f2
    if f2 < 10000000:
        fiblist.append(f2)   
    else:
        break
print(fiblist)

for num in fiblist:
    if num % 2 == 0:
        templist.append(num)
print (templist)
b = [sum(templist)]
print(b)                  
print (fiblist[-1])
    


