''' ## zip() 함수란?

- 여러 iterable의 요소를 묶어 튜플로 만듭니다.
- 가장 짧은 iterable의 길이에 맞춰집니다.
- 일회성 반복자(iterator)를 반환하므로, 여러 번 사용하려면 목록list으로 변환해야 합니다.
- `zip(*iterable)`을 사용하여 언패킹할 수 있습니다.
- 병렬 처리, 사전 생성, 행렬 조작 등 다양한 작업에 유용합니다.
# '''

# names = ["홍길동", "김철수", "이영희"]
# ages = [20, 25, 30]
# cities = ["서울", "부산", "인천"]


# combined = zip(names, ages)
# # print(list(combined))

# combined = zip(names, ages, cities)
# print(list(combined))

names = ["홍길동", "김철수", "이영희", "박지성"]
ages = [20, 25, 30]
combined = zip(names, ages)
# print(list(combined)) # "박지성"은 짝이 없어 결과에 포함되지 않음

combined_dict = dict(combined)
# print(combined_dict)

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

sum = [x + y for x, y in zip(list1, list2)]
# print(sum)

products = [x * y for x, y in zip(list1, list2)]
# print(products)

''' random module '''
import random

# rand_float = random.random()
# print(rand_float)

# rand_int = random.randint(1, 1000)
# print(rand_int)

fruits = ['사과', '바나나', '오렌지', '포도']
# chosen = random.choice(fruits)
# print(chosen)

random.shuffle(fruits)
# print(fruits)


''' datetime '''
from datetime import datetime

