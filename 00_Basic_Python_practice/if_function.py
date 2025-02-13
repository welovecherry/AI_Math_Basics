# def greet(name="Guest"):
#     return f"hello, {name}"

# print(greet())
# print(greet("abc"))

# def calculate(a,b):
#     return a+b, a-b, a*b, a/b

# result = calculate(10, 2)
# print(result)

''' ->: 리턴값의 타입을 지정
하지만 이는 단순한 힌트일 뿐이라서 타입을 강제하지 않는다.

'''
# def add(a: int, b: int) ->int:
#     return a + b

# #문자열을 넣어도 동작은 됨 (에러 없음)
# print(add("Hello ", "world"))

# def example (
#         age: int,
#         name: str,
#         is_student: bool,
# ) -> str:
#     return f"{name} is {age} years old " 

# print(example(1, "cherry", True,))

'''
튜플 특징: 
- 순서 있는 데이터 구조. 인덱스로 요소에 접근 가능.
- 불변이라서 한번 생성되면 내용을 변경할 수 없다. (추가, 삭제, 수정 불가)
- 정수, 문자열, 리스트, 다른 튜플도 저장 가능
'''
# my_tuple = (1, 2, 3)
# print(my_tuple)
# print(my_tuple[0])
# print(my_tuple[1])
# print(my_tuple[2])

# simple_tutple = 4, 5, 6
# print(simple_tutple)

# text = "Python Programming"

# print(text[:])

# text = "Hello, World!"
# print(text[-6:])
# print(text[::-1])


# num1, num2 = input().split()
# if (int(num1) == int(num2)):
#     print("True")
# else:
#     print("False")


# def check_input(value):
#     if value:
#         return "value is not empty" 
#     return "empty value"

# print(check_input(""))
# print(check_input("hello"))
# print(check_input("0"))
# print(check_input("-1"))

# num1 = int(input())
# if num1 == 0:
#     print("False")
# else:
#     print("True")

# a = True
# b = False
# print(f"not a: {not a}")
# print(f"a AND b: {a and b}")
# print(f"a or b: {a or b}")

# age = 20;
# has_id = True
# money = 100

# can_buy_alcohol = age >= 20 and has_id and money >= 1000
# print(f"can buy alcohol? {can_buy_alcohol}")

# def add(a: int, b: int) -> int:
#     return a + b

# result = add(5, 3)

# def say_hello(name: str) -> None:
#     print(f"hello, {name}")

# say_hello("kim")

# def add(a, b):
#     return a + b

# def add (a: int, b: int) -> int:
#     return a + b

# def user_info(name: str, age:int) -> str:
#     return f"{name} is {age} years old"

# result1 = user_info("cherry", 3)
# print(result1)

# result2 = user_info(name="charm", age=2)

# def greet(name: str, greetint: str = "hihi") -> str:
#     return f"{greetint}, {name}"
# print(greet("cherry"))
# print(greet("charm", "bye")) #update value

# # 1. math_tools.py
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def main():
#     print("수학 도구 테스트!")
#     print(f"5 + 3 = {add(5, 3)}")
#     print(f"5 - 3 = {subtract(5, 3)}")

# if __name__ == "__main__":
#     main()  # 이 파일을 직접 실행할 때만 테스트가 실행됨

# num = int(input())

# if bool(num) == False:
#     print("True")
# else:
#     print("False")

# num1, num2 = input().split()
# num1 = int(num1)
# num2 = int(num2)
# if bool(num1) == True:
#     if bool(num2) == True:
#         print("True")
# else:
#     print("False")

# a, b = input().split()
# if (bool(int(a)) and bool(int(b)) == True):
#     print ("True")
# else:
    # print("False")

# 삼항연산자
# num1, num2 = map(int, input().split())
# print("True" if num1 and num2 else "False")

# age = 20
# print("adult" if age >= 20 else "teen")

# a, b = 10, 20
# result = a if a > b else b

# text = ""
# msg = text if text else "empty"
# print(msg)


# num1, num2 = map(int, input.split())

# numbers = map(int, input().split())
# print(list(numbers))

# a, b, c = map(int, input().split())
# print(a, b, c)

'''2개의 정수값이 입력될 때,
그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
'''
# num1, num2 = map(int, input().split())

# if bool(num1) == False and bool(num2) == False:
#     print("True")
# else:
#     print("False")


# num = int(input())
# result = ~num
# print(result)

# a, b, c = map(int, input().split())

# if a < b and a < c:
#     min = a
# elif b < a and b < c:
#     min = b
# else:
#     min = c

# print(min)
# print(min(a, b, c))

# numbers = [a, b, c]
# # print(min(numbers))
# numbers.sort()
# print(numbers[0])

# min_num = a if a < b else b
# min_num = min_num if min_num < c else c
# print(min_num)

# a, b, c = map(int, input().split())

# if a % 2 == 0:
#     print(a)
# if b % 2 == 0:
#     print(b)
# if c % 2 == 0:
#     print(c)
# numbers = [a, b, c]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# numbers = [1, 2, 3, 4, 5]

# evens = []
# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)

# print(evens)

# odds = [num for num in numbers if num % 2 == 1]

''' 다양한 함수 예시 '''
''' 예제 2: 문자열을 대문자로 변환하여 반환하는 함수 '''

def to_uppercase(text):
    return text.upper()

res = to_uppercase("abcd")
# print(res)

''' 예제 4: 리스트의 요소를 출력하는 함수 '''
# def print_list(items):
#     for item in items:
#         print(item)

# print_list([1, 2, 3, 4])

''' return ''.join('0' if c < '5' else '1' for c in x) 비슷한 예제 '''
numbers = [1, 2, 3, 4, 5, 6]
res = ''.join('E' if num % 2 == 0 else 'O' for num in numbers)
# print(res)

''' 주어진 문자열 리스트에서 길이가 5 이하인 문자열은 'S', 그 이상은 'L'로 표시하는 예제입니다. '''
words = ["apple", "banana", "kiwi", "cherry"]
res = ''.join('S' if len(word) <= 5 else 'L' for word in words)
# print(res)

''' 예제 3: 알파벳 대소문자 구분하기
주어진 문자열에서 대문자는 'U', 소문자는 'L'로 표시하는 예제입니다.
'''

text = "Hello World"
res = ''.join('U' if ch.isupper() else 'L' for ch in text)
# print(res)

''' 내림을 표현하는 다양한 방법 
1. math.floor
2. 실수를 정수로 변환하기
3. // 연산자 사용: 나눗셈의 결과를 내림 처리 가능
'''
f = 12.123
# print(type(f)) # float

# print(int(f))

num = 12.23
# print(int(num//1))

''' numpy library '''
import numpy as np

numbers = np.array([3.4, 2.5, 1.2])
result = np.floor(numbers)
# print(result)

''' 올림: ceil() '''
import math

num1 = 1.23
res1 = math.ceil(num1)
# print(res1)

''' You get given the time in hours and you need to return the number of litres
 Nathan will drink, rounded to the smallest value.

'''

def litres(time):
    return int(time * 0.5 /1)

res = litres(11.8)
# print(res)

''' 
Write a function that takes an array of numbers and returns the sum of the numbers. 
The numbers can be negative or non-integer. 
If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.

'''

def sum_array(a):
    sum = 0
    for element in a:
        sum += element
    return sum

input = [1, 5.2, 4, 0, -1]
input1 = []
res = sum_array(input1)
# print(res)


'''
Timmy & Sarah think they are in love, but around where they live, 
they will only know once they pick a flower each. 
If one of the flowers has an even number of petals 
and the other has an odd number of petals it means they are in love.

Write a function 
that will take the number of petals of each flower 
and return true if they are in love and false if they aren't.

'''

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    elif flower1 % 2 == 1 and flower2 % 2 == 0:
        return True;
    else:
        return False

case1 = lovefunc(0, 0)
case2 = lovefunc(1, 0)
case3 = lovefunc(0, 1)
case4 = lovefunc(1, 1)

# print(case1)
# print(case2)
# print(case3)
# print(case4)


res_list = []
test_cases = [(0,0), (1,0), (0,1), (1,1)]
for case in test_cases:
    res = lovefunc(case[0], case[1])
    res_list.append(res)

# for res in res_list:
#     print(res)

def sum_even_odd(num1, num2):
    return True if num1 + num2 % 2 == 0 else False

res_list = []

test_cases = [(2, 3), (0, 0), (4, 5), (-2, 1)]
for case in test_cases:
    res = sum_even_odd(case[0], case[1])
    res_list.append(res)

# for res in res_list:
    # print(res)

''' 
Write a function to convert a name into initials. 
This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H # make upper

patrick feeney => P.F

'''

def abbrev_name(name):
    name_list = name.split(" ")
    res = name_list[0][0].upper() + '.' + name_list[1][0].upper()
    return res

res = abbrev_name("tam harris")
# print(res)

'''Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''

def maps(a):
    double_a = [element * 2 for element in a]
    return double_a

res = maps([1, 2, 3])
# print(res)

''' Summation
Write a program that finds the summation of every number from 1 to num. 
The number will always be a positive integer greater than 0. 
Your function only needs to return the result, 
what is shown between parentheses in the example below is how you reach that result 
and it's not part of it, see the sample tests.

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8) '''

def summation(num):
    sum = 0
    for element in range(1, int(num) + 1):
        sum += element
    return sum

# print(summation(2))

''' ["One", "Two", "Thre", "Four"] --> ["Four"] '''

def filter_even_length_words(words):
    even_list = []
    for word in words:
        if len(word) % 2 == 0:
            even_list.append(word)
    return even_list

res = filter_even_length_words(["One", "Two", "Thre", "Four"])
print(res)

# return [word for word in words if len(word) % 2 == 0]

''' multiplying a given number by eight if it is an even number and by nine otherwise.

'''

def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9

# print(simple_multiplication(2))
# print(simple_multiplication(3))

'''
You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.
'''

def other_angle(a, b):
    return 180 - (a + b)

print(other_angle(100, 10))