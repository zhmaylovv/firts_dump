# the end step 1

'''import statistics
h = []
d = {}
with open("dataset_3380_5.txt", 'r') as fil:
    for line in fil:
        str_line = line.strip().split()
        if str_line[0] in d.keys():
            d[str_line[0]].append(int(str_line[2]))
        else:
            d[str_line[0]] = [int(str_line[2])]
print(d)
for i in range (1,12):
    k = str(i)
    if k in d.keys():
        print(i, statistics.mean(d[k]))
    else:
        print(i, '-')
'''



'''a = []
print (h)
with open("dataset_3363_1.txt", 'w', encoding='utf_8_sig') as file:
    for i in range (len(h)):
        res1 = (str(round(statistics.mean(h[i]), 9)) + '\n')
        file.write((res1))

    for i in range (len(h[0])):
        for j in range (len(h)):
            a.append(h[j][i])

        print (a)
        res2 = (str(round((statistics.mean(a)), 9)) + ' ')
        file.write(res2)
        a = []
    file.write('\n')


'''



'''x = 0
y = 0
for i in range(int(input())):
    d, n = input().split()
    if d == 'север':
        x += int(n)
    elif d == 'юг':
        x -= int(n)
    elif d == 'запад':
        y -= int(n)
    elif d == 'восток':
        y += int(n)
print(y,x)
'''


'''st = set()
st2 = set()
for i in range (int(input())):
    st.add(input().lower())
for i in range(int(input())):
    for i in input().split():
        k = i.lower()
        if k not in st:
            if i not in st2:
                print(i)
                st2.add(i)
'''

'''Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

code1 = [i for i in (input())]
code2 = [i for i in (input())]
str1 = input()
str2 = input()
dico = {}
res = []
for i in range (len(code1)):
    dico[code1[i]] = code2[i]
for i in str1:
    res.append(dico[i])
print(*res, sep='')
res = []
for i in range (len(code2)):
    dico[code2[i]] = code1[i]
for i in str2:
    res.append(dico[i])
print(*res, sep='')

'''



'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output:

Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1

di = {}
s = []
for i in range (int(input())):
    s = [i for i in input().split(';')]
    if s[0] not in di.keys():
        di[s[0]] = {'game' : 0,
                        'win' : 0,
                        'draw' : 0,
                        'los' : 0,
                        'total': 0}
    if s[2] not in di.keys():
        di[s[2]] = {'game': 0,
                        'win': 0,
                        'draw': 0,
                        'los': 0,
                        'total': 0}
    if s[1] > s[3]:
        di[s[0]]['game'] += 1
        di[s[0]]['win'] += 1
        di[s[2]]['game'] += 1
        di[s[2]]['los'] += 1
    elif s[1] < s[3]:
        di[s[2]]['game'] += 1
        di[s[2]]['win'] += 1
        di[s[0]]['game'] += 1
        di[s[0]]['los'] += 1
    else:
        di[s[0]]['game'] += 1
        di[s[0]]['draw'] += 1
        di[s[2]]['game'] += 1
        di[s[2]]['draw'] += 1
for i in di.keys():
    di[i]['total'] = di[i]['win']*3 + di[i]['draw']
for i in di.keys():
    print(i+':'+str(di[i]['game']), di[i]['win'], di[i]['draw'], di[i]['los'], di[i]['total'])'''








'''
import requests
v = '699991.txt'
sq = 1
while sq != 0:
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+ v)

    v = r.text
    print(v)
    sq = r.text.find('W')

'''
#print(len(r.text.splitlines()))





'''import math

r = int(input())
print(math.pi*2*r)
'''






'''import statistics
h = []
with open("dataset_3363_4.txt", 'r') as fil:
    for line in fil:
        str_line = line.strip().split(";")
        h.append([int(i) for i in str_line[1:]])
a = []
print (h)
with open("dataset_3363_1.txt", 'w', encoding='utf_8_sig') as file:
    for i in range (len(h)):
        res1 = (str(round(statistics.mean(h[i]), 9)) + '\n')
        file.write((res1))

    for i in range (len(h[0])):
        for j in range (len(h)):
            a.append(h[j][i])

        print (a)
        res2 = (str(round((statistics.mean(a)), 9)) + ' ')
        file.write(res2)
        a = []
    file.write('\n')
'''


"""
#stepic IO task
with open("bib.txt", 'r') as fil:
    str_line = fil.read().replace('\n', ' ').lower().split()

print (type(str_line))
di = {}
for i in str_line:
    c = di.get(i.lower(), 0)
    di[i] = c + 1

max_key = max(di.values())
temp = 'яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя'
for i in di.keys():
    if di[i] == max_key:
        if i <= temp :
            temp = i
print(temp, max_key)"""


"""
#stepic IO task

with open("dataset_3363_2.txt", 'r') as fil:
    for line in fil:
        str_line = line.strip()
lst = []
temp = ''
n = 1
k = ''
with open("dataset_3363_1.txt", 'w') as file:
    for i in str_line:
        if i not in "0123456789":
            if temp != '':
                file.write (temp * n)
                k = ''
            temp = i

        else:
            k = k + i
            n = int(k)
    file.write(temp * n)
print("DONE")
"""

