a = 10
b = 25
compose = 1

for i in range(2, max(a, b)):
    if a % i == 0 and b % i == 0:
        compose = i
        break

if compose == 1:
    print('Числа взаимно просты')
    
else:
    print(compose)
