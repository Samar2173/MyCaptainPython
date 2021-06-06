n = int(input('Enter the range fo Fibonnaci Sequence: '))

a = 0
b = 1
print(f'{a}, {b}, ', end = '')
for i in range(1, n-1):
    fib = a + b
    print(fib, end =', ')
    a = b
    b = fib