# print(f'Мое имя {input()}!')

a = input()
b = int(input())
print(f'Hello {a.upper()}. You are {b} years old.')

name, age =input(), input()
print(f'Hello {name.upper()}. You are {age} years old.')

print(f"Hello {input().upper()}. You are {input()} years old.")

a, b = input().upper(), int(input())
print(f'Hello {a}. You are {b} years old.')

name, year = input(), int(input())
print(f'{name}, вам исполнится 77 лет в {year+77}')

sec = int(input())
print(f'{sec} сек - это {sec//60} мин. {sec%60} сек.')

a,b = map(int, input().split())
print(f'Разрешение экрана: {a} x {b}.')
print(f'Общее количество пикселей = {a * b}.')

a,b  = int(input()), int(input())
print(f'{a} / {b} = {a/b}\n{a} // {b} = {a//b}\n{a} % {b} = {a%b}')

n1, n2 = input(), input()
for op in ['/', '//', '%']:
  print(f"{n1} {op} {n2} = {eval(n1 + op + n2)}")

a,b,c = int(input()), int(input()), int(input())
print(f'Vector A{a, b, c}')
print(f'Vector B{a+5, b+5, c+5}')

a = [int(input()) for y in range(3)]
b = ', '.join(str(y+5)for y in a)
a = ', '.join(str(i) for i in a)
print(f"Vector A({a})\nVector B({b})")
x, y, z = (int(input()) for _ in range(3))
print(f'Vector A({x}, {y}, {z})\nVector B({x+5}, {y+5}, {z+5})')

lst = [int(input()) for x in range(3)]
print(f"Vector A({lst[0]}, {lst[1]}, {lst[2]})\nVector B({lst[0]+5}, {lst[1]+5}, {lst[2]+5})")

a,b = float(input()), int(input())
print(f'Current dollar rate is {a}. You want buy {b} dollars\nYou must pay {a*b}')