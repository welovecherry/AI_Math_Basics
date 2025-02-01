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


