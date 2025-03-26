is_raining = True
is_sunny = False
# print(type(is_raining))

a = True
b = False
# print(a and b)
# print(a or b)
# print(not a)

# print(5 > 3)

# false values
empty_string = ""
empty_list = []
empty_tuple = ()
empty_dict = {}
empty_set = set()
zero = 0
none_value = None

''' 모두 False로 출력됨 '''
# print(bool(empty_string))  # False
# print(bool(empty_list))    # False
# print(bool(empty_tuple))   # False
# print(bool(empty_dict))    # False
# print(bool(empty_set))     # False
# print(bool(zero))          # False
# print(bool(none_value))    # False


''' 모두 True로 해석됨 '''
# non_empty_string = "string"

''' bool with if statement '''
age = 25

# if age >= 18:
#     print("adult")
# else:
#     print("teenager")

my_list = []

# if my_list:
#     print("list is empty")
# else:
#     print("list is not empty")

has_ticket = True
has_id = False

if has_ticket and has_id:
    print("pass")
elif has_ticket and not has_id:
    print("show me ID")
else:
    print("buy ticket")

