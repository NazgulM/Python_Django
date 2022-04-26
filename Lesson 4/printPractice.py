print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')

# dividing 41//12 = 3
# divide 41%12 = 5 remainder

x = 78452
a = x // 10000
b = x // 1000 % 10
c = x // 100 % 10
d = x // 10 % 10
e = x % 10
print('\n', a, b, c, d, e)

print(int(input()) // 1000)

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

a = int(input())
sum_of_digits = sum(int(digit) for digit in str(a))
print(sum_of_digits)

print(sum(map(int, input())))

a = int(input())
print((a // 100) + (a // 10 % 10) + (a % 10))

a = int(input())
a1 = a // 100
a2 = a // 10 % 10
a3 = a % 10
print(a1 + a2 + a3)

a = list(map(int, list(input())))
print(sum(a))

n = int(input())
k100 = n // 100
n = n % 100
k20 = n // 20
n = n % 20
k10 = n // 10
n = n % 10
k5 = n // 5
n = n % 5
print(k100 + k20 + k10 + k5 + n)

min = int(input())
print(min % 24, min % 1440)

min = int(input())
min = min % 1440
print(min //60, min % 60)

n = int(input()) % (24*60)
print(*divmod(n, 60))

n = int(input())
print ((n+2)//2*2)

num = int(input())
print(num+2 -num % 2)

sec = int(input())

hh = (sec // 3600) % 24
sec = sec % 3600
minute = sec // 60
sec = sec %60
sec = sec %60
seconds = sec
print(hh,':', minute // 10, minute % 10,':',sec//10, sec%10, sep="")

