a = [43, 54, 12, 84, 32, 6, 7, 8, 9, 10]
print(a[4])
print(a[-1])
print(a[1:5])
print(a[2:999])
print(a[:2])
print(a[2:])
print(a[:])
print(a[::2])
print(a[1::2])
print(a[3:7:3])
a[2:5] = 25, 33
print(a)
del a[2]
print(a[:])
print(a[::-2])
d = a[:]
print(d)

a = list(map(int, input().split()))
print(a[1])

a = list(map(int, input().split()))
print(a[2:5])

top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
top[-1] = 'Сверхъестественное'
top[2] = 'Настоящий детектив'
print(top)


a = list(map(int, input().split()))
print(a[-3:])

print([*map(int, input().split())][-3:])
list_obj = list(map(int, input().split()))
print(list_obj[len(list_obj) - 3:])

a = list(map(int, input().split()))
print(a[1::3])

print(list(map(int, input().split()))[1::3])

print(list(map(int, input().split()))[::-1])