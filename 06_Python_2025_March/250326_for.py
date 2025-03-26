name = "John Smith"
vowels = "aeiou"

# for i in range(len(name)):
#     char = name[i]
#     if char.lower() in vowels:
#         print(f"{i+1}: {char} character is vowel")
#     else:
#         print(f"")

msg = "HELLO"
encrypted = ""

for i in range(len(msg)):
    char = msg[i]
    new_char = chr(ord(char) + 1)

''' enumerate()는 반복 가능한 객체의 요소와 인덱스를 함께 제공하는 함수입니다. '''
tasks = ['a', 'b', 'c', 'd']

# for num, task in enumerate(tasks, 10):
#     print(f"task {num} : {task}")

scores = [1, 2, 3, 4, 5]

# for i, score in enumerate(scores):
#     if score < 3:
#         print(f"student {i+1} got {score} and needs to study")
#     elif score == 5:
#         print("perfect")
#     else:
#         print("hi")

'''리스트 컴프리헨션은 반복문을 사용해 리스트를 간단하게 만드는 방법입니다.'''
