
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(gen.__next__())  # 1
print(gen.__next__())  # 2
print(gen.__next__())  # 3
print(gen.__next__())  # StopIteration