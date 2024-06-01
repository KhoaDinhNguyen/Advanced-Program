def main():
    print("Hello World")
    print(1 + "A")

### List operation
print([1, 2, 3, 4, 5][2])
print(len([1, 2, 3, 4, 5]))
print([1, 2] + [3, 4, 5])
print(list(range(0, 10)))
array = [1, 2, 3]
del array[0]
print(array)
print([1, 2, 3][1 : 3])

### Recursion
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

print(fibo(3))
print(fibo(5))

### List Comprehensions
print([2 * x + 1 for x in list ( range (0, 10))])
print([(x, y) for x in [1, 2, 3] for y in [4, 5]])
print([(y, x) for x in [1, 2, 3] for y in list ( range (1, x + 1))])
print(all([x % 2 == 0 for x in [2, 4, 6, 8]]))
print(all([x % 2 == 0 for x in [2, 4, 6, 9]]))

def factors(n : int):
    return [x for x in range(1, n + 1) if n % x == 0]

print(factors(15))
print(factors(17))
def isPrime(n :int):
    return factors(n) == [1, n]

print(isPrime(15))  
print(isPrime(17))

# Higher-order function
def increaseBy1(x:int):
    return x + 1

def even(x : int):
    return x % 2 == 0

print(list(map(increaseBy1, [1, 2, 3, 4])))
print(list(map(even, [1, 2, 3, 4])))

print(list(filter(even, [1, 2, 3, 4])))

### Lambda expression
print((lambda x : x + 1)(5))
print(list(map(lambda x : x % 2 == 0, [1, 2, 3, 4])))

### Curried function
def sumThreeValue(a):
    return lambda x : lambda y : x + y + a
    
print(sumThreeValue(1)(2)(3))

### Merge sort
def merge(a1, a2, func):
    if len(a1) == 0:
        return a2
    elif len(a2) == 0:
        return a1
    if func(a1[0], a2[0]):
       return [a1[0]] + merge(a1[1:], a2, func)
    return [a2[0]] + merge(a1, a2[1:], func)

def split(a):
    return (a[0 : int(len(a) / 2)], a[int(len(a) / 2) : len(a)])

def mergeSort(a):
    if len(a) <= 1:
        return lambda func : a
    (a1, a2) = split(a)
    return lambda func : merge(mergeSort(a1)(func), mergeSort(a2)(func), func)


def desc(x, y):
    return x > y

def asec(x, y):
    return x < y

print(mergeSort([5, 4, 7, 1, 2, 3, 4])(lambda x, y : x < y)) 
print(mergeSort([5, 4, 7, 1, 2, 3, 4])(lambda x, y : x > y))