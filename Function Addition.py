'''
https://www.codewars.com/kata/5ebcfe1b8904f400208e3f0d
 often find that I end up needing to write a function to return multiple values,
 in this case I would often split it up into two different functions but then
 I have to spend time thinking of a new function name! Wouldn't it be great if
 I could use same name for a function again and again...

In this kata your task is to make a decorator, FuncAdd which will allow function
 names to be reused and when called all functions with that name will be called
 (in order) and the results returned as a tuple.

'''



class FuncAdd:
    func_list = {}

    def __init__(self, func):
        self.name = func.__name__
        if self.name not in FuncAdd.func_list.keys():
            FuncAdd.func_list[self.name] = []
        FuncAdd.func_list[self.name].append(func)

    def __call__(self, *args, **kwargs):
        if self.name not in FuncAdd.func_list.keys():
            raise NameError
        return tuple([func(*args, **kwargs) for func in FuncAdd.func_list[self.name]])

    @classmethod
    def delete(cls, func):
        if func.name in FuncAdd.func_list.keys():
            del cls.func_list[func.name]

    @classmethod
    def clear(cls):
        cls.func_list = {}
