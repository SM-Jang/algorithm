n = int(input())
    
    
def get_starList(n):
    # n이 1일때, 종료 조건
    if n==1: 
        return ['*']
    # n이 1이 아닐때,
    else:
        ans = []
        # 재귀 n=3,9,27,... 
        # if n=27일 때, 
        # starList = f(9)
        '''
        ['*********',
         '* ** ** *',
         '*********',
         '***   ***',
         '* *   * *',
         '***   ***',
         '*********',
         '* ** ** *',
         '*********']
        '''
        # starList = f(3) 
        '''
        ['***',
        '* *',
        '***']
        '''
        # starList = f(1) ['*']
        starList = get_starList(n//3)
        # n==3: starList = 
        # n==9: starList = 

        for star in starList:
            ans.append(star*3)
        for star in starList:
            ans.append(star + ' '*(n//3) + star)
        for star in starList:
            ans.append(star*3)
        return ans
        
for starLine in get_starList(n):
    print(starLine)