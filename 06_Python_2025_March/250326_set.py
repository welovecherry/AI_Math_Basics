'''fruits = set(['a', 'b', 'c'])
print(fruits)

colors = {'r', 'g', 'b'}
print(colors)

empty_set = set()
print(empty_set)

'''
letters = set('hello')
# print(letters) #remvoed dup value l

numbers = {1, 2, 2, 2, 3}
# print(numbers)

''' union '''
A = {1, 2, 3, 4, 5}
B = {2, 3, 4, 5, 6}

union_res = A | B
# print(union_res)

union_res2 = A.union(B)
# print(union_res2)

''' intersection '''
inter_res = A & B
# print(inter_res)

inter_res2 = A.intersection(B)
# print(inter_res2)


''' difference '''
diff_res = A - B
# print(diff_res)

diff_res2 = A.difference(B)
# print(diff_res2)


''' add(): add one value '''
fruits = {'a', 'b'}
fruits.add('c')
# print(fruits)

fruits.add('a') #no diff when dup value adds
# print(fruits)

''' update: add multiple values'''
colors = {'r', 'b'}
colors.update(['c', 'd'])
# print(colors)

more_colors = {'p', 'q'}
colors.update(more_colors)
# print(colors)


''' remove: delete specific value '''
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
# print(numbers)

# try:
    # numbers.remove(10)
# except KeyError:
    # print("no 10")

''' discard: even if the element doesnt exist, no error occuers'''
numbers.discard(100)
# print(numbers)

number_list = [1, 2, 2, 2, 3, 4, 5]
unique_numbers = list(set(number_list))
print(unique_numbers)

fruits = {'사과', '바나나', '오렌지'}
print('사과' in fruits)
print('사과aa' in fruits)