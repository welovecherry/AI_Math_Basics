
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

''' C++의 맵
- 키-쌍으로 구성된 연관 배열로, 2개의 요소(키-밸류)로 이루어짐
'''

# list1 = [1, 2, 3]
# list2 = [11, 22, 33]

# result = list(map(lambda x, y: x+y, list1, list2))
# print(result)

''' while '''
# number = 1
# while number <= 10:
#     number += 1
#     if number % 2 == 1:
#         continue
#     print(number)

# while True:
#     user_input = input("type 'exit' if you want to quit")
#     if user_input.lower() == 'exit':
#         print("finish the program")
#         break
#     else:
#         print(f"user input: {user_input}")

''' 문자열 유용한 함수 

strip(): 양쪽 끝의 공백 제거
replace(): 문자열 교체
split(): 문자열 나누기
join(): 리스트를 문자열로 연결
find(): 특정 문자열의 인덱스 찾기
count(): 특정 문자열의 개수 세기
upper(): 대문자로 변환
'''

''' strip() : 양쪽 끝의 공백 또는 지정된 문자 제거 '''
# text = "   hello  "
# cleaned_text = text.strip()
# print(cleaned_text)

''' replace() '''
# text1 = "i love apples"
# new_text = text1.replace("apples", "cherry")
# print(new_text)

''' split() '''
# text2 = "apple, banana, cheery"
# fruits = text2.split(", ")
# print(fruits)

''' join() : 지정한 문자열로 연결해 하나의 문자열로 만듦'''
# joined_text = "## ".join(fruits)
# print(joined_text)

''' find() : 찾은 문자열이 처음 나오는 위치의 인덱스 반환함'''
# text4 = "Hello, World"
# index = text4.find("World")
# print(index)


# def smash(words):
#     joined = ""
#     # for word in words:
#     joined = " ".join(words)
    
#     return joined

# words = ['hello', 'world', 'this', 'is', 'great']

# joined = smash(words)
# print(joined)

'''
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7 '''

# def basic_op(operator, value1, value2):
#     if operator == '+':
#         return value1 + value2
#     elif operator == '-':
#         return value1 - value2
#     elif operator == '*':
#         return value1 * value2
#     elif operator == '/':
#         return value1 / value2
    
# print(basic_op('+', 4, 7))

''' eval() 
- 파이썬 내장 함수, 문자열로 표현된 파이썬 표현식을 실행하고 결과를 반환함.
- 보안상 이유로 이발함수 주의해야하는 이유
    - 문자열을 그대로 실행하는데, rm -rf 같은 코드를 넣어도 실행함!
- 문자열의 입력이 항상 안전한지 판단이 어려울 수 있기 때문에 주의해야함
'''



# num = 5
# num = str(num)
# new_num = num.replace(num, "0")
# print(new_num)

# def fake_bin(x):
#     i = 0
#     while(x[i]):
#         print(i)
#         i += 1
    
# res = fake_bin("12345")
# print(res)

''' 문자열을 문자 하나씩 출력하는 다양한 방법'''
''' 1 '''
string = "abcde"
i = 0;

''' 2 '''
# while i < len(string):
#     print(string[i])
#     i += 1

''' 3 '''
# for char in string:
#     print(char)

''' 4: get idx and char at the same time '''
# for i, char in enumerate(string):
#     print(f"idx:{i}: {char}")

''' 5 '''
# output = [char for char in string]
# print("\n".join(output))

'''Given a string of digits, you should replace any digit below 5 with '0' 
and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string'''

# def fake_bin(x):
#     for ch in x:
#         int_ch = int(ch)
#         if int_ch < 5:
#             # print("less than 5")
#             ch.replace(ch, "0")
#     return x


# res = fake_bin("123678")
# print(res)

''' 아래 코드에서 ch.replace 안되는 이유
- 파이썬의 불변성: 파이썬에서 문자열은 불변이다.
- 그런데 새로운 변수에 저장하면 데이터 타입은 바꿀 수 있다.

- replace()는 새로운 문자열을 반환할 뿐, 원래 문자열을 변경하지 않음.


'''
# str = "123789"
# new_list= []

# for ch in str:
#     if int(ch) < 5:
#         new_ch = ch.replace(ch, "0")
#         new_list.append(new_ch)
#     else:
#         new_ch = ch.replace(ch, "1")
#         new_list.append(new_ch)

# res = "".join(new_list)

# print(res)


def fake_bin(x):
    new_list= []

    for ch in x:
        # print(ch)
        if int(ch) < 5:
            new_ch = ch.replace(ch, "0")
            new_list.append(new_ch)
        else:
            new_ch = ch.replace(ch, "1")
            new_list.append(new_ch)

    res = "".join(new_list)
    # print(res)
    return res

res = fake_bin("123789")
# print(f"res : {res}")



# print(res)


# str1 = "123"
# for ch in str1:
#     print(type(ch))
#     ch_to_int = int(ch)
#     print(type(ch_to_int))

# def fake_bin(x):
#     new_str = ""

#     for ch in x:
#         if int(ch) < 5:
#             new_str = new_str + "0"
#         else:
#             new_str = new_str + "1"
#     print(new_str)
#     return new_str

# res = fake_bin("123789")


'''
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
'''

# def fake_bin(x):
#     return ''.join('0' if c < 5 else '1' for c in x)

def fake_bin(x):
    return ''.join('0' if ch < '5' else '1' for ch in x)

res = fake_bin("123789")
# print(res)


''' 파이썬에서 문자열은 유니코드를 기준으로 비교됨. 
'3', '5'를 비교할 수 있다
작은따옴표 꼭 써야함
'''
ch = '3'
if ch < '5':
    print("wow")