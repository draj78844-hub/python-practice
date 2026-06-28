class complex:
    def __init__(self, real, img):
        self.real= real
        self.img= img

    def shownumber(self):
        print(self.real,"i +", self.img,"i")

    num1 = complex(4,7)
    num1.shownumber()   