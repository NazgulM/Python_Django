# a = input()
# if len(a) > 6:
#     print(a[:3].upper() + a[3:-3].lower() + a[-3:].upper())
# else:
#     print(a.upper())
# (lambda i: print(i[:3].upper() + i[3:-3].lower() + i[-3:].upper()))(input())

a = [12, 43, 54, 65, 76, 3]
a.append('hello')
print(a)

a.clear()
print(a)

a = [12, 43, 54, 65, 76, 3, 'hello']
b = a.copy()
print(b)

print(a.count(12))
print(a.index(54))

print(b.index(12))
print(b.index(3, 3))
a.insert(2, 'Nazkou')
print(a)

b.pop()
print(b)
print(b.pop(3))
print(b.remove(12))
print(b)
b.reverse()
print(b)
b.sort(reverse=True)
print(b)

# mas = input().split()
# # Вот здесь разместите свой код
# mas.reverse()
# # Конец вашего кода
# print(*mas)
#
#
# a = list(map(int, input().split()))
# print(a.count(999))
#
# print(*reversed([i for i in input().split()]))

a = 'hello masha'
a.upper().split()
print(a)