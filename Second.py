def fizzbuzz(intList):
    temp = []
    for n in intList:
        if n % 3 == 0 and n % 5 == 0:
            temp.append('Fizzbuzz')
        elif n % 3 == 0:
            temp.append('Fizz')
        elif n % 5 == 0:
            temp.append('Buzz')
        else:
            temp.append(n)
    return temp


print (fizzbuzz(range(1,20)))