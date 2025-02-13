'''
지수: 거듭제곱의 횟수를 나타내는 문자나 숫자.

루트: 어떤 수를 제곱해서 루트 안의 수가 나오게 하는것

'''

import math
print(math.sqrt(4)) # sqrt 함수는 항상 비음수의 제곱근만을 반환함. 결과는 항상 양수.

''' 인수분해 
- 복잡한 식을 공통 인수로 묶어서 곱으로 표현하는 과정.
- 인수분해의 반대 개념 = 전개 (expand)

'''

'''
symbols: 여러 변수 한번에 만들기
'''

# from sympy import expand, factor, Symbol, symbols

# x, y, z = symbols('x y z') # 변수 이름에 공백을 포함할 수 있다. 이 경우 문자열로 묶어야한다.
# x = 10
# y = 2
# z = 1
# print(x, y, z)

# expression1 = x + 2*y + z
# print(expression1)

# res = expression1.subs({x: 1, y:2})
# print(res)

''' expand(): 전개 '''
# from sympy import symbols, expand

# x, y = symbols('x y')
# polynomial = (x + y) ** 2

# expand_poly = expand(polynomial)
# print(expand_poly)


''' factor(): 다항식을 인수분해 해서 곱셈 형태 ()()로 변환'''
from sympy import symbols, factor

x = symbols('x')

poly = x**2 + 3*x + 2
factored_poly = factor(poly)
print(factored_poly)