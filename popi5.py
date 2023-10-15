import time
import random

def gen (size):
    arr = []
    for i in range (size):
        arr.append(random.randint(0, 9))

    return arr

def find(haystack, needle):
    i = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return i
        i += 1
    return -1 

size = 1000000
iter = 100
arr = gen(size)
arr[0] = 10
arr[size // 2] = 11
arr[-1] = 12

print('-' * 30)
print('Метод index')

start = time.time() 
for i in range(iter):
    arr.index(10)
end = (time.time() - start) / iter
print(f'в начале: {end}')
 
start = time.time() 
for i in range(iter):
    arr.index(11)
end = (time.time() - start) / iter
print(f'в середине: {end}')

start = time.time() 
for i in range(iter):
    arr.index(12)
end = (time.time() - start) / iter
print(f'в конце: {end}')

print('-' * 30)
print('Наша функция')

start = time.time () 
for i in range(iter):
    find(arr, 10)
end = (time.time() - start) / iter
print(f'в начале: {end}')

start = time.time() 
for i in range(iter):
    find(arr, 11)
end = (time.time() - start) / iter
print(f'в середине: {end}')

start = time.time() 
for i in range(iter):
    find(arr, 12)
end = (time.time() - start) / iter
print(f'в конце: {end}')
