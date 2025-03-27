age = 15
# print("age" + str(age))

# print("name", "cherry")

''' print with end='''
# print('one', end=", ")
# print('two', end="?")

''' print with sep '''
# print("사과", "바나나", "오렌지")  # 사과 바나나 오렌지
# print("사과", "바나나", "오렌지", sep=', ')  # 사과 바나나 오렌지
# print("사과", "바나나", "오렌지", sep=' - ')  # 사과 바나나 오렌지

# print("사과", "바나나", "오렌지", sep='\n')  # 사과 바나나 오렌지

# pi = 3.14159265
# print(f"py is {pi:.2f}")

# price = 1000000
# print(f"price: {price:,} won")


# print(""" one
#       2
#     3
#       3
#       3""")


file = open("ex.txt", "a")
file = open("ex.txt", "w")
file.write("hihi\n")
file.write("ex of python")

''' write multiple lines '''
lines = ["first line\n", "second_line", "last line"]
file = open("lines.txt", "w")
file.writelines(lines)

file.close()

'''파일의 내용을 읽으려면 read(), readline(), 또는 readlines() 메서드를 사용합니다. '''
# file = open("ex.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("ex.txt", "r")
# line1 = file.readline()
# line2 = file.readline()
# print(line1, line2)
# file.close()

file = open("ex.txt", "r")
lines = file.readlines()

for line in lines:
    print(line)

file.close()

''' ## with 문을 사용한 파일 처리 (권장)
`with` 문을 사용하면 파일을 자동으로 닫아주므로 `close()`를 호출할 필요가 없습니다. 이 방식이 더 안전하고 권장됩니다.
'''

# with open("ex.txt", "r+") as file: 
#     file.write("hihi\n")
#     file.write("ex using with statement")
#     content = file.read()
#     print(content)


# try:
#     password = input("enter password")
# except ValueError as error:
#     print("error")
# else:
#     print("logged in")

# file = open("ex2.txt", "r")

# lines = file.readlines()
# for line in lines:
#     print(line.strip())
# file.close()


with open("ex3.txt", "w") as file:
    file.write("hi\n")
    file.write("123")
    # content = file.read()
    # print(content)
with open("ex3.txt", "r") as file:
    content = file.read()
    print(content)