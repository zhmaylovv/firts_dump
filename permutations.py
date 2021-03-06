import itertools
from sys import argv
n = int(argv[1])
strin = ''
list_of_dig = [0 for i in range(n)]

for i in range(1,n+1):
    list_of_dig.append(i)
result = list(itertools.permutations(list_of_dig))

for i in result:
    for j in i:
        strin += str(j)
    print(strin)
    strin = ''

