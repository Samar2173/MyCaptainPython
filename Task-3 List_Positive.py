l = list(map(int, input('Enter Integers seperated by ",": ').split(',')))
res = []
for i in l:
    if i > 0:
        res.append(i)
print(f'Output: {res}')