from random import randint
a = [randint(1, 10) for i in range(10)]
b = 0
for i in a:
    b += i
print(a)
print(b)
