result = range(1, 11)
print(result)
print(list(result))

for value in range(1, 6):
    print(value, 'iteration')

result1 = range(11)
print(list(result1))

for value in range(5):
    print(value)

result2 = list(range(1, 11, 1))
print(result2)

result2 = list(range(1, 11, 3))
print(result2)

result3 = list(range(5, -6, -1))
print(result3)

result4 = list(range(3, 31, 3))
print(result4)