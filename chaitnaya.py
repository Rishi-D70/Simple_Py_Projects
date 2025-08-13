class A:
    def show():
       print("all apples are fruits")
class B(A):
    def show():
        print("some fruits are apples")
class C(B):
    def show():
        print("but pineapples are better tho")

C.show()
C.show()
C.show()