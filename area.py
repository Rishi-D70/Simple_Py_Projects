class Rec:
    def __init__(self):
        self.lenght = 5
        self.width = 20


    def show_area(self):
        print(f"Area of rectangle is: ", self.lenght * self.width )

r = Rec()
r.show_area()
