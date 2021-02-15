'''
Task:
Return an array or a tuple or a string depending on the language (see "Sample Tests") with

the smallest number you got
the index i of the digit d you took, i as small as possible
the index j (as small as possible) where you insert this digit d to have the smallest number.
Examples:
smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2,

testing(261235, [126235, 2, 0]);
testing(209917, [29917, 0, 1]);
testing(285365, [238565, 3, 1]);
testing(269045, [26945, 3, 0]);
testing(296837, [239687, 4, 1]);
testing(403287943124548279, [32487943124548279, 0, 3]);
'''


def smallest(n):

    print (n)
    lst = [int(i) for i in str(n)]
    c = 0
    if 0 in lst and lst[1] != 0:
        removeitem_index = ''.join([str(i) for i in lst]).rindex('0') + 1
        lst = lst[:removeitem_index-1] + lst[removeitem_index  :]

    elif lst[1] == 0:
        c = 2
        for i in lst[2:]:
            if lst[0] < i:
                lst.insert(c, lst[0])
                lst = lst[2:]
                removeitem_index = 1
                c -= 1
                break
            c +=1

    elif lst[0] > max(lst[1:]) and 0 not in lst and lst[1] > min(lst[2:]):
        lst.append(lst[0])
        lst = lst[1:]
        removeitem_index = 0
        c = len(lst) -1


    else:
        for i in lst:
            if i > min(lst[lst.index(i):]):
                removeitem_index = ''.join([str(i) for i in lst]).rindex(str(min(lst[lst.index(i):]))) + 1
                lst.insert(c, min(lst[lst.index(i):]))
                lst.pop(removeitem_index)
                break
            c += 1
    if c == 0 and removeitem_index == 2:
        removeitem_index, c = 1, 1
    return [int(''.join([str(i) for i in lst])), removeitem_index-1, c]
