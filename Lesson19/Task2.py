def in_range(start, end=None, step=1):
    if end is None:
        start, end = 0, start
    if step == 0:
        raise ValueError('Step must not be 0!')
    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step


for i in in_range(5):
    print(i, end=' ')

print('\n')

for i in in_range(2, 10, 2):
    print(i, end=' ')

print('\n')

for i in in_range(10, 2, -2):
    print(i, end=' ')

print('\n')

try:
    for i in in_range(10, 2, 0):
        print(i, end=' ')
except ValueError as e:
    print(e)



