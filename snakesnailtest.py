'''
Snail
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
Given an n x n array, return the array elements arranged from outermost elements
 to the middle element, traveling clockwise.
'''


def snail(snail_map):
    if len(snail_map[0]) == 0:
        return []

    n = len(snail_map)
    x = 0
    res = []

    for i in range(n//2): #zad
        for j in range(x, n-1-x):
            res.append(snail_map[x][j])
        for j in range(x, n-1-x):
            res.append(snail_map[j][n-1-x])
        for j in range(n-1-x, x, -1):
            res.append(snail_map[n-1-x][j])
        for j in range(n-1-x, x, -1):
            res.append(snail_map[j][x])
        x += 1
    if n %2 !=0:
        res.append(snail_map[n//2][n//2])

    return res

m = [  [1, 2, 3, 4, 5],
        [14, 15, 16, 17, 6],
        [13, 20, 19, 18, 7],
        [12, 11, 10, 9, 8]]
print(snail(m)) # не работает на не n*n массивах  )))
