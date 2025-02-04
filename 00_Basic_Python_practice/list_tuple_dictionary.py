# fruits = ["apple", "banana", "orange"]
# print(fruits[0])

# print("hi i'am cherry")
# print('hi i"am cherry')
# print('I\'m a student')

# mixed = [1, "cherry", True]
# mixed.append("append last")
# mixed.insert(1, "first")
# mixed.remove("cherry")
# print(mixed)

''' list '''
# numbers = [1, 22, 3, 14, 65, 9, 1]

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# numbers.reverse()
# print(numbers)

# print(numbers.count(1))
# print(numbers.index(22))

''' dictionary '''

# my_dic = {}

# student = {
#     'name': 'John',
#     'age': 20,
#     'major': 'CS'
# }
# print(student)
# name = student['name']
# age = student['age']
# print(f"name: {name}, age: {age}")

# student['age'] = 200
# print(student)

# student['grade'] = 'A'
# print(student)

# del student['major']
# print(student)

# ''' dictionary method '''
# keys = student.keys()
# print(keys)
# print(student.values())
# print(student.items())

# grades = {
#     'alice': 12,
#     'bob': 12,
#     'cherry': 12
# }

# grades['alice'] = 20  # update the value
# print(grades)

# for name, grade in grades.items():
#     print(f"{name}: {grade}")

# grades['charm'] = 100
# print(grades)

'''
[] 는 딕셔너리에서 값을 조회, 변경할 때 쓰임
'''

# student = {
#     'name' : 'a',
#     'age' : 20,
#     'major' : 'english'
# }

# name = student['name']
# age = student['age']

# # print(name + " " + str(age))
# student['age'] = 30
# print(student)

# del student['major']
# print(student)

''' for statement 
for 변수 in 반복 가능한 객체:
    반복할 코드
'''

''' for with list '''
# fruits = ['apple', 'banana','cherry']
# for fruit in fruits:
#     print(fruit)


# word = 'hello'
# for letter in word:
#     print(letter)

# for i in range(5):
#     print(i) #0 1 2 3 4 with new line

''' not in 
- 특정 값이 리스트, 튜플, 문자열 등 
반복 가능한 객체에 포함되지 않을 때 확인하는 연산자
- 특정 값이 없을 때 True 리턴함

반대는 in.
in은 특정 값이 존재할 때 True 반환함
'''

# numbers = [1, 2, 3, 4]

# if 3 in numbers:
#     print("there is 3")

# if 6 not in numbers:
#     print("there is not 6 in the list")

''' 리스트에서 중복된 값 제거하기'''
# numbers = [1, 2, 3, 4, 5, 6, 6, 6, 1]
# print (numbers)

# unique_numbers = []

# for number in numbers:
#     if number not in unique_numbers:
#         unique_numbers.append(number)

# print (numbers)
# print (unique_numbers)

# student = {'name': "Alice", 'age' : 40}

# if 'grade' not in student:
#     print('there is no grade')


''' list comprehension 
- 기존의 리스트를 기반으로 새로운 리스트 만들 때 유용
new_list = [expression for item in iterable if condition]
'''

# squared_numbers = [x ** 2 for x in range(10)]
# print(squared_numbers)

# if 추가할 수 있다.
# even_squared_numbers = [x ** 2 for x in range(10) if x % 2 == 0]
# print(even_squared_numbers)

# fruits = ["a", "b", "c"]
# uppercase_fruits = [fruit.upper() for fruit in fruits]
# print(uppercase_fruits)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# flattened = []
# for row in matrix:
#     for num in row:
#         flattened.append(num)
# print(flattened)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# sum = 0
# for row in matrix:
#     for num in row:
#         sum += num
# print(sum)

''' 튜플 
- 요소를 변경, 삭제하려고 하면 에러남.
- 튜플 안에는 [] 리스트 사용 가능함.

- 튜플이 리스트보다 메모리 사용량이 효율적인 이유
1. 불변성: 튜플은 한번 생성되면 변경 불가. 추가적인 메모리 관리가 불필요해서
2. 고정된 크기: 튜플은 고정된 크기를 가지므로
'''
# t1 = ()
# t2 = (1,)
# t3 = (1, 2, 3)
# t4 = 1, 2, 3
# t5 = ('a', 'b', ('ab', 'cd'))
# mixed_tuple = (1, 2, "abc", 'a', [1, 2, 3])

# print(t2[0])

# students = (
#     ("a", [1, 2, 3]),
#     ("b", [4, 5, 6]),
#     ("c", [10, 20, 30])
# )

''' 학생 별로 평균 성적 내기 '''
# sum = 0
# aver = []

# for name, scores in students:
#     # print(scores)
#     for score in scores:
#         # print(score)
#         sum += score
#         # print(f"sum: {sum}")
#     aver.append(sum / 3)
#     sum = 0
#     print(f"name: {name}, average: {aver[-1]}")
#     print("")

''' 튜플 언패킹 
- 튜플의 요소를 개별 변수에 쉽게 할당하는 방법.
- 가독성을 높이고 여러값을 동시에 반환 가능
'''

# person = {"alice", 30, "seoul"}

# name, age, city = person
# print( name, age, city)

'''
- 아래 코드는 전체적으로 리스트, 
- 리스트 안애 여러개의 튜플.
'''
# products = [
#     ("Apple", 1000),
#     ("Banana", 500),
#     ("Cherry", 1500)
# ]


# for product , price in products:
#     print(product, price)

coordinates = [
    (1, 2),
    (2, 3),
    (4, 5)
]

# for x, y in coordinates:
#     print(x, y)

# coordinates[0] = 3 # 0번째 인덱스는 튜플이 아니라 리스트라서 수정 가능함.
# print(coordinates[0])

# coordinates[0][0] = 9
# print(coordinates[0][0]) # 튜플의 요소 하나를 수정할 수 없어서 에러남