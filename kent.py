'''
SberCraft задачка про Кентавров
'''



def total_time(lst, n):
    timer = 0
    while sum(lst)>0:
        c = 0
        timer += 1
        for i in range(len(lst)):
            if c+1 > n:
                break
            if lst[i] > 0:
                lst[i] -= 1
                c += 1
    return timer
print(total_time([3, 5, 10], 2))
