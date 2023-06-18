from math import sqrt
a = int(input())
prime = True

for i in range(2, int(sqrt(a)) + 1):
    if a % i == 0:
        prime = False
        print('Число не является простым')
        break
    
if prime:
    print('Число является простым')
