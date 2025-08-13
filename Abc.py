from abc import ABC

class cal(ABC):
    def calculate(self, n1, n2):
        pass

class add(cal):
    def calculate(self, n1,n2):
        print(n1+n2)
class sub(cal):
    def calculate(self, n1,n2):
        print(n1-n2)
class div(cal):
    def calculate(self, n1,n2):
        print(n1 / n2)
class mul(cal):
    def calculate(self, n1,n2):
        print(n1 * n2)
a = add()
s = sub()
d = div()
m = mul()

a.calculate(1, 2)
