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
from string import ascii_letters
from string import digits

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
        
        if exp[i-1] in digits:
            tempdig += exp[i-1]
        else:
            digit.append(tempdig)
            digit.append(exp[i-1])
            tempdig = ''

    digit.append(exp[-1])
    print(digit)
    return result

print(calculate('1222+1333'))
