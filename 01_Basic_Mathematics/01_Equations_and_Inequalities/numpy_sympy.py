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


''' sympy '''
