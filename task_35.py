def fib(num):
    a = 1
    b = 1
    print(a)
    print(b)
    
    for i in range(num-2):
        print(a + b)
        a, b = b, a + b


number = int(input())
fib(number)