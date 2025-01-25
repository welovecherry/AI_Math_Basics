print("hihi")
print("first", "second", "third")

number = 42
text = "python"
print(number)
print(text)

name = "cherry"
age = 10

# f-string: modern style of print 중괄호 안에 직접 변수를 넣을 수 있다.
print(f"name: {name}, age: {age}")

# previous style of format()
print("name: {}, age: {}".format(name, age))

print(f"name: {name}, next year age: {age + 1}")
print(f"name: {name.upper()}")
print("\n")

# user_name = input("enter your name: ")
# print(f"hi, {user_name} !")

''' input()은 항상 문자열을 반환하므로 숫자로 변환해야한다. '''
# age_str = input("enter your age: ")
# age_num = int(age_str) #change string to integer
# print(f"you will be {age_num + 1} years old")

# x, y = input("enter 2 numbers ").split() # split()은 공백을 기준으로 입력 받음
# x = int(x)
# y = int(y)
# print(f"sum:  {x + y}")

# a = input()
# print(int(a))

# f = input()
# print(float(f))

# a = input()
# b = input()
# int(a)
# int(b)
# print(a)
# print(b)

# str1 = input()
# str2 = input()
# print(str2)
# print(str1)

# f = input()
# f = float(f)
# print(f)
# print(f)
# print(f)

# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a)
# print(b)

# a, b = input().split()
# print(b, a)

# a = input()
# print (a, a, a)

# a, b = input().split(":")
# print(a, b, sep=":")

# a, b, c = input().split(".")
# print(c, b, a, sep="-")

# a,b = input().split("-")
# print(a, b, sep='')

# str = input()
# print(str[0])
# print(str[1])
# print(str[2])
# print(str[3])
# print(str[4])

# a = input()
# print(a[0 : 2])
# print(a[2 : 4])
# print(a[4 : 6])

# h, m, s = input().split(":")
# print(m)

# str1, str2 = input().split()
# joined_str = str1 + str2
# print(joined_str)

# int1, int2 = input().split()
# int1 = int(int1)
# int2 = int(int2)
# sum = int1 + int2
# print(sum)

# float1 = input()
# float2 = input()
# float1 = float(float1)
# float2 = float(float2)
# print(float1 + float2)

# float1 = float(input())
# float2 = float(input())
# print(float1 + float2)
