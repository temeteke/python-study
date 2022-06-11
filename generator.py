def my_generator():
    for i in range(10):
        print(f'Generating {i}')
        yield i

print(my_generator())

print('リストにする')
print(list(my_generator()))

print('一つずつ取り出す')
mg = my_generator()
print(next(mg))
print(next(mg))
print(next(mg))

print('forループで全て取り出す')
for i in my_generator():
    print(i)

print('スライスする')
print('stop=3')
from itertools import islice
for i in islice(my_generator(), 3):
    print(i)

print('start=1, stop=3')
from itertools import islice
for i in islice(my_generator(), 1, 3):
    print(i)

print('start=1, stop=5, step=2')
from itertools import islice
for i in islice(my_generator(), 1, 5, 2):
    print(i)
