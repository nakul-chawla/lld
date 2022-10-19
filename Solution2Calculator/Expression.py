from AirthmeticExpression import AirthmeticExpression

class Expression(AirthmeticExpression):

    def __init__(self, left_part:AirthmeticExpression, right_part:AirthmeticExpression, operator):
        self.left_a_expression = left_part
        self.right_a_expression = right_part
        self.operator = operator
        self.sol = None

    def evaluate(self):
        # print(f"""The number is:{self.num}""")
        
        if self.operator == "ADD":
            self.sol = self.left_a_expression.evaluate() + self.right_a_expression.evaluate()
        elif self.operator == "SUB":
            self.sol = self.left_a_expression.evaluate() - self.right_a_expression.evaluate()
        elif self.operator == "MUL":
            self.sol = self.left_a_expression.evaluate() * self.right_a_expression.evaluate()            
            
        print(self.sol)
        return self.sol