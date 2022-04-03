s = input()

diag = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for d in diag:
    if d in s:
        s = s.replace(d, '*')
        
        
print(len(s))