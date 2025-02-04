
''' for with enumerate()
반복 가능한 객체의 인덱스와 값을 동시에 제공 '''

# fruits = ["apple", "banana", "cherry"]

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# for i in range(2, 4):
#     for j in range(1, 4):
#         print(f"{i} * {j} = {i * j}")

''' range() function 
1. range(stop): 0 ~ 스탑 직전까지의 숫자 생성.

2. for i in range(start, stop, step)

- 레인지는 모든 숫자를 메모리에 저장하지 않고 필요할때마다 생성함.
따라서 메모리 효율이 좋다.
'''

# for i in range(2, 5):
#     print(i)

# for i in range(10, 1, -1):
#     print(i)

# total = 0;
# for i in range(0, 11):
#     total += i

# print(f"sum: {total}")


# fruits = ['apple', 'banana', 'cherry', 'date']

# for index, fruit in enumerate(fruits):
#     print(f"{index} : {fruit}")


# total = 0
# scores = [85, 90, 78, 92, 88]

# for index, score in enumerate(scores):
#     total += score
#     print(f"Student {index}: {score}")
# print(f"Total score: {total}")

# '''1'''
# for even in range(2, 21, 2):
#     print(even)

# '''2'''
# for i in range(2, 6):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}")

# '''3'''
# total = 0
# for i in range(3, 101, 3):
#     total += i
# print(total)




''' 문자열 리스트에서 특정 문자 찾기 '''
# words = ['aa', 'bb', 'cc', 'dd']

# for word in words:
#     if 'aa' in word:
#         print("found aa")

''' 리스트에서 중복 제거하고 출력하기 '''
# numbers = [1, 1, 2, 2, 3, 3, 3,]
# unique_numbers = []

# for number in numbers:
#     if number not in unique_numbers:
#         unique_numbers.append(number)

# print(f"unique numbers: {unique_numbers}")

''' 에러나는 이유
i + 1은 반복가능한 객체가 아니다! range()써라!!
range(i + 1)
'''
# for i in range(5):
#     for j in i + 1:
#         print("*", end='')
#     print()

# print()

# pibo = [1, 1]
# print((pibo[0] + pibo[1]))
# pibo.append(pibo[0] + pibo[1])
# print(pibo) # 1

# input_value = int(input())

# for i in range(input_value):
#     if (i >= 2):
#         pibo.append(pibo[i - 2] + pibo[i - 1])
#         # print(pibo[i])
# print(pibo)

# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [1]
#     elif n == 2:
#         return [1, 1]
#     else:
#         fib = fibonacci(n - 1)
#         fib.append(fib[-1] + fib[-2])
#         return fib

# print(fibonacci(5))

''' return nth fibonacci number '''

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(3))

# n = int(input())
# fibo_list = []

# for fibo in range(1, n):
#     # print(fibo)
#     fibo_list.append(fibonacci(fibo))

# print(fibo_list)

''' search max and min value in list '''
# empty_list = []

# empty_list = int(input()).split() # error
# empty_list = int(input().split()) # error

# print(empty_list)

''' 여러 입력을 일괄적으로 정수로 변형하려면 map()사용하기
맵함수: 반복 가능한 객ㅊ의 각 요소에 적용해서 새로운 반복 가능한 객체를 생성함'''

# input_list = list(map(int, input().split()))

# len = 0
# for i in input_list:
#     len += 1
# # print(len)

# # print(empty_list)
# min = input_list[0]
# max = input_list[0]
# # print(min)
# for n in range(len):
#     # print(input_list[n])
#     if input_list[n] < min:
#         min = input_list[n]
#     else:
#         max = input_list[n]

# print(f"min: {min}")
# print(f"max: {max}")

''' min(), max() '''
# input_list = list(map(int, input().split()))

# min_value = min(input_list)
# max_value = max(input_list)
# print(f"min: {min_value}, max: {max_value}")

''' sort 사용하기 '''
# input_list = list(map(int, input().split()))
# input_list.sort()
# print(f"min: {input_list[0]}, max: {input_list[-1]}")

''' 파이썬의 맵()함수
- 반복 가능한 객체의 각 요소에, 주어진 함수를 적용해서
새로운 반복 가능한 객체를 생성함. 

- 여러 인자를 받을 수 있다.
'''

list1 = [1, 2, 3]
list2 = [11, 22, 33]

result = list(map(lambda x, y: x+y, list1, list2))
print(result)