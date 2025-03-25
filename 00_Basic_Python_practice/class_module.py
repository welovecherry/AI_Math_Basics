# class Myclass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
        # print(f"my name is {self.name}, i am {self.age} years old ")

# student1 = Myclass("cheery", 10)
# student1.introduce()




# class ShoppingCart:
#     items = []
    
#     def add_item(self, name, price):
#         self.name = name
#         self.price = price

#     def total_price(self):
#         self.total = sum()


# ''' list '''
# mixed = ["apple", 1 , True, 2.446]

# ''' list of lists (2D list)'''
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# ''' list of tuples '''
# coordinates = [(0, 0) , (1, 2), (3, 4)]

# shopping_cart = [
#     {"item": "Apple", "price": 123},
#     {"item": "banana", "price": 234}
# ]

# for item in shopping_cart:
    # print(f"item: {item['item']} price: {item['price']}")

# item = {"item": "Orange", "price": 20}
# print(f"Item name: {item['item']}")
# print(f"price: {item['price']}")


# shopping_cart = [
#     {"item": "Apple", "price": 1.50},
#     {"item": "Banana", "price": 0.75},
#     {"item": "Orange", "price": 2.00}
# ]

# for item in shopping_cart:
#     print(f"item: {item['item']}, price: {item['price']:.2f}")

# item = {"item": "watermelone", "price": 2.01}
# if item['price'] > 2.0:
#     print(f"the {item['item']} is a bit expensive")
# else:
#     print(f"the {item['item']} is affordable")

''' 런타임에 리얼 타임으로 값이 인설트 됨'''

# user = {"name": "cherry", "age": 12, "location": "korea"}
# print(f"{user['name']} is {user['age']} years old living in {user['location']}")

''' make a class '''

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score        

    def display_info(self):
        return(f"{self.name}'s score is {self.score}")

s1 = Student("a", 1)
s2 = Student("b", 11)
s3 = Student("c", 22)

# print(s1.display_info())

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, score):
        self.students.append({"name": name, "score":score})
    
    def show_student(self):
        for student in self.students:
            print(f'name: {student["name"]}: score: {student["score"]}')

    def average_score(self):
        sum = 0
        for s in self.students:
            sum += s['score']
        return sum / len(self.students)

m1 = StudentManager()
m1.add_student("a", 1)
m1.add_student("bbb", 2)
m1.add_student("ccc", 3)

m1.show_student()

sum = m1.average_score()
print(sum)

# shopping_cart = [
#     {"item": "Apple", "price": 1.50},
#     {"item": "Banana", "price": 0.75},
#     {"item": "Orange", "price": 2.00}
# ]

# sum = 0
# for item in shopping_cart:
#     sum += item["price"]

# sum = 0
# for item in shopping_cart:
#     sum += item['price']

# print(sum)

