def with_index(iterable, start=0):
    for element in iterable:
        yield start, element
        start += 1


for i, value in with_index(['item1', 'item2', 'item3', 'item4', 'item5', 'item6'], start=1):
    print(f'{i} - {value}')