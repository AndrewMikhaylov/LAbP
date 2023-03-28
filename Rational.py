import math
from functools import singledispatchmethod

class Rational:
    @singledispatchmethod
    def __init__(self, numbers):
        raise ValueError(f"unsupported numbers format: {numbers}")

    @__init__.register(str)
    def _from_string(self, numbers_divided_by_slash : str):
       list = numbers_divided_by_slash.split("/")
       final_list = self.check_if_fully_divided(list[0],list[1])
       self.n = (int)(final_list[0])
       self.d = (int)(final_list[1])


    @__init__.register(int, int)
    def _from_two_numbers(self, n, d):
        list = self.check_if_fully_divided(n, d)
        self.n = list[0]
        self.d = list[1]

    def check_if_fully_divided(self, n, d):
        list=[]
        mutual=math.gcd(n, d)
        if mutual == 1:
            list.append(n)
            list.append(d)
        else:
            new_divider= d / mutual
            new_divided = n / mutual
            list.append(new_divided)
            list.append(new_divider)
        return list

    ##перегрузка операторів
    ##перегрузка додавання
    def __add__(self, other):
        if isinstance(other, Rational):
            result_n = self.n*other.d+other.n*self.d
            result_d = self.d*other.d
            return Rational(result_n,result_d)
        if isinstance(other, int):
            result_n = self.n+other*self.d
            result_d = self.d
            return Rational(result_n,result_d)

    def __radd__(self, other):
        if isinstance(other, Rational):
            result_n = self.n*other.d+other.n*self.d
            result_d = self.d*other.d
            return Rational(result_n,result_d)
        if isinstance(other, int):
            result_n = self.n+other*self.d
            result_d = self.d
            return Rational(result_n,result_d)
    #перегрузка віднімання
    def __sub__(self, other):
        if isinstance(other, Rational):
            result_n = self.n*other.d-other.n*self.d
            result_d = self.d*other.d
            return Rational(result_n,result_d)
        if isinstance(other, int):
            result_n = self.n-other*self.d
            result_d = self.d
            return Rational(result_n,result_d)

    def __rsub__(self, other):
        if isinstance(other, Rational):
            result_n = other.n*self.d - self.n*other.d
            result_d = self.d*other.d
            return Rational(result_n,result_d)
        if isinstance(other, int):
            result_n = other*self.d-self.n
            result_d = self.d
            return Rational(result_n,result_d)

    #перегрузка множення
    def __mul__(self, other):
        if isinstance(other, Rational):
            result_n = self.n*other.n
            result_d = self.d*other.d
            return Rational(result_n,result_d)
        if isinstance(other, int):
            result_n = self.n*other
            result_d = self.d
            return Rational(result_n,result_d)

    def __rmul__(self, other):
        if isinstance(other, Rational):
            result_n = self.n*other.n
            result_d = self.d*other.d
            return Rational(result_n,result_d)
        if isinstance(other, int):
            result_n = self.n*other
            result_d = self.d
            return Rational(result_n,result_d)

    #перегрузка круглих дужок
    def __call__(self):
        result = self.n/self.d
        return result

    #перегрузка квадратних дужок
    def __getitem__(self, item:str):
        if item=="n":
            return self.n
        elif item=="d":
            return self.d
        else:
            print("Wrong input")



