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

numbers = [1, 2, 3, 4, 5]

evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)

odds = [num for num in numbers if num % 2 == 1]