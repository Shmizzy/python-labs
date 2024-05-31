
def getName():
    name = input('what is your name?')
    print('hello, ' + name)

# getName()

def reverseString(): 
    string = 'a man, a plan, a canal, frenemies!'
    reverse = ''

    for c in range(0, len(string)):
        reverse += string[len(string) - (c+1)]

    print(reverse) 

# reverseString()

def swapEm():
    a = 10
    b = 30
    
    temp = b
    b = a
    a = temp
    print('a is now ->' + str(a) + ' b is now ->' + str(b))

# swapEm()

def multiplyArr(arr):
    if len(arr) == 0:
        print(1)
    
    total = arr[0]

    for i in range(0, len(arr)):
        total = total * arr[i]

    print(total)

# multiplyArr([1,2,3,4]) 

def fizzBuzz(num):
    if(num % 3 == 0):
        print('fizz')
    elif(num % 5 == 0):
        print('buzz')
    else:
        print('fizzbuzz')

def fibonacci(n):
    if n == 0:
      return 0
    elif n == 1 or n == 2:
        return 1    
    
    return fibonacci(n - 1) + fibonacci(n - 2)
    

# print(fibonacci(13))

def searchArray(arr, value):
    for num in arr:
        if value == num:
            return 'true'
    return 'false'

# print(searchArray([11,2,13,44], 4))

def hasDupes(arr):
    obj = {}
    for num in arr:
        if num in obj.keys():
            return 'true'
        else:
            obj[num] = 1
    return 'false'

# print(hasDupes([1,19,44,18,9,11,99]))
