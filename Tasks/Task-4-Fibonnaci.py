n = int(input('Enter the range fo Fibonnaci Sequence: '))

fib = 0
a = 0
b = 1
print(f'{a}, {b}, ', end = '')

for i in range(2, n):
    fib = a + b
    print(fib, end =', ')
    a = b
    b = fib
