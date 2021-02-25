'''
https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
'''


from CodewarsTest import Test



def spiralize(size):
    spiral=[]
    for i in range(size):
        spiral.append([0 for i in range(size)])
    s = 0
    c = 0
    b = -1
    s1 = 1
    for i in range(size):
        spiral[0][i] = 1

    for i in range (size//2-1):
        for j in range(s, size-c):
            spiral[j][b] = 1
        for j in range(size-1-c,c,-1):
            spiral[b][j] = 1

        for j in range(size-s-1,s1,-1 ):
            spiral[j][s] = 1
        s +=2
        if s == size/2 and size % 2 == 0:
            break
        else:

            for j in range(c, size-s):
                spiral[s][j] = 1
        c +=2
        s1 += 2
        b -= 2

    return spiral

sp = spiralize(8)
for i in sp:
    print(i)

Test.assert_equals(spiralize(5), [[1,1,1,1,1],
                                  [0,0,0,0,1],
                                  [1,1,1,0,1],
                                  [1,0,0,0,1],
                                  [1,1,1,1,1]])
Test.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
                                  [0,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,0,1],
                                  [1,0,0,0,0,1,0,1],
                                  [1,0,1,0,0,1,0,1],
                                  [1,0,1,1,1,1,0,1],
                                  [1,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,1,1]])
