ext = {'py':'Python', 'c':'C', 'exe':'Executable File', 'gif':'Graphics Interchange Format'}

fileName = str(input("Input the Filename: "))
extFile = fileName.split('.')[1]

if extFile in ext:
    print(f'The extension of the file is: {ext[extFile]}')
else:
    print('Could not understand the format')