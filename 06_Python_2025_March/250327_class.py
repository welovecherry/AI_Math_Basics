class Student:
    school_name = "c_school"

    def __init__(self, name, grade, student_id):
        self.name = name
        self.grade = grade
        self.student_id = student_id
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_info(self):
        return self.name, self.grade, self.student_id
    
    def show_subject(self):
        if not self.subjects:
            return "no subject"
        return self.subjects
    
student1 = Student("cherry", 1, 123)
student1 = Student("cherry2", 12, 123333)

student1.add_subject("math")
print(student1.show_subject())

''' inheritance '''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"hi i am {self.name}"
    
class Employee(Person):
    def __init__(self, name, age, em_id, department):
        super().__init__(name, age)
        self.em_id = em_id
        self.department = department

    def introduce(self):
        basic_intro = super().introduce()
        return f"{basic_intro} i am {self.department} and my id is {self.em_id}"
    
person = Person("lee", 30)
em = Employee("cherry", 10, 123, "AI")

# print(person.introduce())
# print(em.introduce())

numbers = [1, 2, 3]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

names = ["Alice", "Bob"]
ages = [10, 20]

