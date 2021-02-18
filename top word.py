'''
https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
Write a function that, given a string of text
(possibly with punctuation and line-breaks),
returns an array of the top-3 most occurring words,
in descending order of the number of occurrences.
'''
from CodewarsTest import Test



def top_3_words(text):
    '''
    :param inn: text - string
    function: count 3 most frequently used words in a text
    :return:  - list with 3 str words []
    '''
    good_text = [] # разбиваем по словам...да, проще б было с регулярками, но тут без них
    k = ''
    for i in text.lower():

        if i in "abcdefghijklmnopqrstuvwxyz'":
            k+=i
        else:
            if "'" not in k:
                good_text.append(k)
                k=''
            else:
                for j in k:
                    if j in "abcdefghijklmnopqrstuvwxyz":
                            good_text.append(k)
                            k=''
                            break
                k=''

    good_text.append(k)
    word_set = set(good_text)        #формируем массив что бы потом сформировать словарик уникальных слов
    word_set.discard('')             #убираем мусор
    dict ={k: good_text.count(k) for k  in word_set}            #считаем количество слов и записываем словарик
    sort_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)          #сортируем словарик по value
    if len(sort_dict) == 1:
        return [sort_dict[0][0]]
    if len(sort_dict) == 2:
        return [sort_dict[0][0], sort_dict[1][0]]
    elif len(sort_dict) > 2:
        return [sort_dict[0][0], sort_dict[1][0], sort_dict[2][0]]

    return []

Test.assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
Test.assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
Test.assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
Test.assert_equals(top_3_words("  , e   .. "), ["e"])
Test.assert_equals(top_3_words("  ...  "), [])
Test.assert_equals(top_3_words("  '  "), [])
Test.assert_equals(top_3_words("  '''  "), [])
