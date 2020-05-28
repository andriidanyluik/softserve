def solution(number):
    '''function search multiples numbers for 3 and 5'''
    a=[]
    for i in range(number):
        
        if i % 3 == 0 or i % 5 == 0:
            a.append(i)
    return sum(a)