'''
This calculator takes values that could be written in a browsers route path as a single string. It then returns the result as a number (or an error message).

Route paths use the '/' symbol so this can't be in our calculator. Instead we are using the '$' symbol as our divide operator.

You will be passed a string of any length containing numbers and operators:

'+' = add
'-' = subtract
'*' = multiply
'$' = divide
Your task is to break the string down and calculate the expression using this order of operations. (division => multiplication => subtraction => addition)

If you are given an invalid input (i.e. any character except .0123456789+-*$) you should return the error message:'400: Bad request'

'''
digits = '0123456789'

def calc(str):
   
    for j in range(len(str)):
        for i in range(len(str)):
            if str[i] =='*':
                str[i-1] = float(str[i-1]) * float(str[i+1])
                str.pop(i)
                str.pop(i)
                break
            elif str[i] =='$':
                str[i-1] = float(float(str[i-1]) / float(str[i+1]))
                str.pop(i)
                str.pop(i)
                break
    print(str)
    for j in range(len(str)):
        for i in range(len(str)):
            if str[i] =='+':
                str[i-1] = float(str[i-1]) + float(str[i+1])
                str.pop(i)
                str.pop(i)
                break

            elif str[i] =='-':
                str[i-1] = float(str[i-1]) - float(str[i+1])
                str.pop(i)
                str.pop(i)
                break


    return str


def calculate(exp):
    print(exp)
    try:
        return float(exp)
    except:
        pass

    result = 0
    tempdig = ''
    digit = []

    for symb in exp:
        if symb not in '.0123456789+-*$':
            return '400: Bad request'

    for i in range(1, len(exp)):
        if exp[i-1] in digits and exp[i] != ')' :
            tempdig += exp[i-1]
        else:
            if tempdig != '':
                digit.append(tempdig)
            digit.append(exp[i-1])
            tempdig = ''

    digit.append(tempdig + exp[-1])


    return float(calc(digit)[0])


#Правильный порядок и ( )
'''from string import ascii_letters
from string import digits

def calc(str):
    print(str)
    for j in range(len(str)):
        for i in range(len(str)):
            if str[i] =='*':
                str[i-1] = int(str[i-1]) * int(str[i+1])
                str.pop(i)
                str.pop(i)
                break
            elif str[i] =='$':
                str[i-1] = int(str[i-1]) / int(str[i+1])
                str.pop(i)
                str.pop(i)
                break
    for j in range(len(str)):
        for i in range(len(str)):
            if str[i] =='+':
                str[i-1] = int(str[i-1]) + int(str[i+1])
                str.pop(i)
                str.pop(i)
                break

            elif str[i] =='-':
                str[i-1] = int(str[i-1]) - int(str[i+1])
                str.pop(i)
                str.pop(i)
                break


    return str

def calculate(exp):
    try:
        return float(exp)
    except:
        pass

    result = 0
    tempdig = ''
    digit = []

    for symb in exp:
        if symb in ascii_letters:
            return '400: Bad request'

    for i in range(1, len(exp)):
        if exp[i-1] in digits and exp[i] != ')' :
            print(exp[i-1])
            tempdig += exp[i-1]
        else:
            if tempdig != '':
                digit.append(tempdig)
            digit.append(exp[i-1])
            print(tempdig)
            tempdig = ''

    digit.append(tempdig + exp[-1])
    while '(' in digit:

        for i in range(len(digit)):
            if digit[i] == '(':
                n = i
            if digit[i] == ')':
                k = i
        print(digit)
        print(digit[n+1:k])
        digit[n:k+1] = calc(digit[n+1:k])
        print(digit)

    print(digit)



    return calc(digit)


print(calculate('15+23-41$28$24$41*15*45$26'))
'''
