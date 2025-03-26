student = {'name': '김철수', 'grade': 3, 'score': 85}
# print(student['score'])

car = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020}
car['year'] = 2030
# print(car['year'])

car['price'] = 1000
# print(car)

student = {'name': '철수', 'age': 20, 'major': '컴퓨터 공학'}
# print(student.get('name'))
# print(student.get('namessss'))

employee = {
    'name': '김과장',
    'department': '개발팀',
    'details': {'salary': 5000000, 'position': '팀장'}
}

# print(employee['details']['position'])

grades = {'John': 'A', 'Mary': 'B', 'David': 'A'}
# for name, grade in grades.items():
#     print(f"{name}: {grade}")


colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
color_code = '#00FF00'
# for name, code in colors.items():
#     if code == color_code:
#         print(name)
#         break
# print("hihi")

my_dict = {'a': 1, 'b': 2}

try:
    print(my_dict['c'])
except KeyError:
    print("non exist Key")


my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("non exist index")

    