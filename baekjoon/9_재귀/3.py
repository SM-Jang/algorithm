n=int(input())
def get_starList(n):
    if n==1: return ['*']
    else:
        starList2=[]
        starList1=get_starList(n//3)
        
        for star in starList1:
            starList2.append(star*3)
        for star in starList1:
            starList2.append(star+' '*(n//3)+star)
        for star in starList1:
            starList2.append(star*3)
            
        return starList2
    
for answer in get_starList(n):
    print(answer)