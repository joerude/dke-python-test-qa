class First:
    def __init__(self):
        self.i = None
        self.multiply(15)
        print(self.i)

    def multiply(self, i):
        self.i = 4 * i

    
class Second(First):
    def __init__(self):
        super().__init__()

    def multiply(self, i):
        self.i = 2 * i


obj = Second()
