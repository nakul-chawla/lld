from AirthmeticExpression import AirthmeticExpression


class Number(AirthmeticExpression):

    def __init__(self, num):
        self.num = num
    
    def evaluate(self):
        print(f"""The number is:{self.num}""")
        return self.num