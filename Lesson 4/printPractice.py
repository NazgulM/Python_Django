print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')

# dividing 41//12 = 3
# divide 41%12 = 5 remainder

x = 78452
a = x//10000
b = x//1000%10
c = x//100%10
d = x//10%10
e = x%10
print('\n',a,b,c,d,e)

print(int(input())//1000)

n, k = int(input()), int(input())
print(k // n)

print(*[j // i for i, j in [[int(input()), int(input())]]])

print(*[k // n for n, k in [[int(input()) for _ in range(2)]]])

money, keds = (int(input()) for i in range(2))
print(money // keds)

print(*[n // r for n, r in [[int(input()), int(input())]]])

print(int(input()) % 10)

print(input()[-1])

print(int(input()) // 100 % 10)

print(('000' + input())[-3])

print(int(input()) % 1000 // 100)