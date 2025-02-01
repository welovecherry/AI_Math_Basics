'''
NumPy: numerical python

- 넘파이에는 제곱근, 지수, 로그, 평균, 중앙값, 표준편차, 숫자 배열에 일괄적으로 값 더하기, 곱하기, 제곱 가능
- 넘파이의 장점: 계산 속도 빠름, 메모리 사용이 효율적이다.

- 넘파이가 빠른 이유: 씨언어로 작성되 있음. 데이터가 연속적으로 저장됨, 모든 요소가 같은 타입임
1: python_list = [1, 2, 3, 4, 5] # 각 요소가 메모리의 다른 위치에 저장됨
# 각 요소가 객체로 저장됨 (더 많은 메모리 사용)

2: numpy.array = np.array([1, 2, 3, 4, 5]) # 모든 요소가 메모리에 연속적으로 저장됨
#모든 요소가 같은 타입임
'''

import numpy as np # call numpy as np

''' list'''
# list1 = [1, 2, 3, 4, 5]
# # list1 + 2 # error
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1 + 2)
# print(arr1 * 3)
# print(arr1 ** 2)

# zeros = np.zeros(5)
# print(zeros)

# print(np.ones(3))

''' matrix '''
# matrix = np.array([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])
# print(matrix)

# print(f"shape: {matrix.shape}")
# print(f"size: {matrix.size}")

# print(matrix[0,0])
# print(matrix[2,2])

''' np with function'''
# scores = np.array([11, 22, 33, 44, 55, 66])

# print(f"average: {np.mean(scores)}")
# print(f"max: {np.max(scores)}")
# print(f"min : {np.min(scores)}")


''' 함수, 메서드 차이 '''
#- 함수: 독립적으로 실행
# numbers = np.array([4, 3, 1, 6, 4, 7])

# print(np.mean(numbers))
# print(np.max(numbers))
# print(np.sort(numbers))
# print(f"origial: {numbers}") # 위에서 sort를 했어도 원본 데이터 자체를 바꾸지는 않는다.

#- 매서드: 객체에 속한 동작으로 객체 자체를 변경시킨다
# numbers.sort()
# print(f"after sorting: {numbers}") # 원본 데이터를 변경시켰다


''' sympy : symbolic(기호)의 약자. 기호를 다루는 파이썬

1. 변수 만들기
2. 방정식 풀기
3. 미분 계산
4. 적분 계산
'''

''' 심파이 방법 1: 
전체 가져와서 별명 붙이기'''
# import sympy as sp
# x = sp.Symbol('x')

''' 심파이 방법 2:
필요한것만 가져오기'''
# from sympy import Symbol, solve
# x = Symbol('x')

'''
- Symbol: 수학에서 변수를 나타내는 기호 생성.
- solve: 방정식 풀어준다

방정식을 풀기 위해서 이항해서 방정식 = 0 꼴로 만들어줘야한다.
'''
# from sympy import Symbol, solve

# x = Symbol('x') # 변수 생성

# equation = x**2 - 4
# solution = solve(equation, x) # 방정식의 해 풀기
# print(solution)

''' 1 '''
# from sympy import Symbol, solve

# k = Symbol('k')
# equation = k - 2 - 4
# solution = solve(equation, k)
# print(solution)


''' 2 '''
from sympy import Symbol, solve

# k = Symbol('k')
# equation = 2*k - 10
# solution = solve(equation, k)
# print(solution)

k = Symbol('k')
equation = k/2 - 8
solution = solve(equation, k)
print(solution)

'''
- 항등식: 항상 좌변과 우변이 같은 식 (=가 반드시 있어야한다)
2x = x + x

- 방정식: 미지수가 특정한 값을 가질때만 참인 수식
2x + 4 = 0

- 항등식도 방정식도 아닌 식
2 + 4 = 6 (미지수 없음)
2x + 2 < 0 (= 없음)
'''

'''
연립 방정식
- 미지수가 여러개 포함된 방정식을 묶어 놓은 것

3x + y = 2
x - 2y = 3

- 미지수가 2개면 식도 적어도 2개 있어야 미지수를 구할 수 있다.
'''