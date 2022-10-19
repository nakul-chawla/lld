from Number import Number
from Expression import Expression

a = Number(2)
b = Number(3)
c = Number(2)

b_c = Expression(b,c,"MUL")

a_b_c = Expression(a,b_c,"ADD")
a_b_c.evaluate()
