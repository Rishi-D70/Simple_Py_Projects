class get_numbers:
    def get_number_operation(self):
        self.n1 = int(input("Enter first num: "))
        self.n2 = int(input("Enter second num: "))
class calculations(get_numbers):
    def add(self):
            print(self.n1 + self.n2)
    def subs(self):
           print(self.n1 - self.n2)


cc = calculations()
cc.get_number_operation()
cc.add()



