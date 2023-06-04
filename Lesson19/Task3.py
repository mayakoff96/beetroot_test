class MyIterable:
    class _MyIterator:

        def __init__(self, data):
            self.data = data
            self.index = 0

        def __next__(self):
            if self.index >= len(self.data):
                raise StopIteration
            result = self.data[self.index]
            self.index += 1
            return result

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterable._MyIterator(self.data)

    def __getitem__(self, index):
        return self.data[index]


my_iter = MyIterable(['item1', 'item2', 'item3', 'item4', 'item5'])

for value in my_iter:
    print(value)

print(my_iter[1])

iter1 = iter(my_iter)
iter2 = iter(my_iter)

print(next(iter1))
print(next(iter2))
print(next(iter2))