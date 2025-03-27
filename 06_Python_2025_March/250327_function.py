''' args '''
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# print(sum_all(1, 2, 3, 4))
# print(sum_all(100))
# print(sum_all(100, 200))
# print(sum_all())


''' kwargs
키워드 매개변수, kwargs
키워드 매개변수(keyword arguments)는 함수 호출 시 매개변수의 이름을 명시적으로 지정하는 방식입니다. 
**kwargs는 이름-값 쌍의 딕셔너리로 전달됩니다.'''

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_info(name = "cherry", age=20, grade='a')

'''. 함수의 리턴값, tuple
파이썬 함수는 여러 값을 동시에 반환할 수 있습니다. 이때 내부적으로 튜플(tuple)을 사용합니다. '''

def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b if b != 0 else "cannot div by 0"
    return add, sub, mul, div

result = calculate(10, 5)
# print(result)
# print(type(result))

add, sub, mul, div = calculate(10, 5)

''' 파이썬에서는 함수의 매개변수에 기본값을 설정할 수 있습니다. 이를 통해 인자를 전달하지 않았을 때 사용할 기본값을 지정할 수 있습니다.
'''

def greet(name, msg="hihi", times=1):
    for _ in range(times):
        print(f"{name} , {msg}")

# greet("cherry")
# greet("charm", "hellllpo")
# greet("third", "hhh", 3)

a = 1
def vartest(a):
    # print(a)
    a = a + 1
    # print(a)
    return a

vartest(a)
# print(a)
# print(vartest(a))

counter = 0

def increment():
    global counter # declare to use global variable
    counter += 1
    print(f"counter: {counter}")

# increment()
# increment()
# print(counter)

my_list = [1, 2, 3]

def add_list(item):
    my_list.append(item)

add_list(4)
# print(my_list)

def add(x, y):
    return x + y

# add_lambda = lambda x, y: x + y
# print(add(2, 3))
# print(add_lambda(3, 4))

# res = (lambda x, y: x * y)
# print(res(10, 2))
''' 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식 

>>> add = lambda a, b: a+b
>>> result = add(3, 4)
>>> print(result)
7
'''


''' map '''

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)

squared_list = list(squared)
# print(squared_list)

# num_str = ["1", "2", "3"]

# numbers = [1, 2, 3, 4, 5]
# res = []

# for num in numbers:
#     res.append(num * 2)

# def multiply_by_two(x):
#     return x * 2

# res2 = list(map(multiply_by_two, numbers))
# print(res2)

# str_numbers = ["1", "2", "3", "4", "5"]
# numbers = list(map(int, str_numbers))
# print(numbers)

# numbers = [-5, -4, -3, 0, 3, 4, 5]
# abs_values = list(map(abs, numbers))
# # print(abs_values)

# def c_to_f(celcius):
#     return (celcius * 9/5) + 32

# temperatures_c = [0, 10, 20, 30, 40]
# temp_f = list(map(c_to_f, temperatures_c))
# print(temp_f)

# def format_name(name):
#     return name.title()

# names = ["hong gildong", "kim chulsoo", "lee younghee"]
# formatted_names = list(map(format_name, names))

# print(formatted_names)

def add_numbers(x, y):
    return x + y

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

sums = list(map(add_numbers, list1, list2))
# print(sums)

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

scores = [ 10, 20 ,30, 100]
grades = list(map(calculate_grade, scores))
# print(grades)

def get_word_len(word):
    return len(word)

words = ["apple", "banana", "cherry", "date", "elderberry"]
word_length = map(get_word_len, words)
print(word_length)
print(list(word_length))