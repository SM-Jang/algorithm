x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f'{i}번째 = {name}')
    
    
print('\n\n')
for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')
    
x_rev = reversed(x)

print('\n\n')
for i, name in enumerate(x_rev, 1):
    print(f'{i}번째 = {name}')