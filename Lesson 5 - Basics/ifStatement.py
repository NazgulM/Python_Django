if 4 ==4:
    print(1)
    print(2)
    print(5)
if 4 < 2:
    print(10)

money = 100
ticket = 90
if money >= ticket:
    print('hureeee I go to cinema')

a = 40
b = 20
c = a
if b < a:
    c = b
print(c)

a = 45
b = 20

if b < a:
    a,b = b,a
print(a,b)

if 4 == 6 or 4 > 2 :
    print(1)
    print(2)
else:
    print(6)
print(7)

if 5:
    print(1)
else:
    print(2)

x = 40
y = 20

if x>y:
    print(x)
else:
    print(y)

q = 56
if q % 2 == 0:
    print('even number')
else:
    print('odd number')

salary = int(input())
if salary > 20000:
    print(salary*0.87)
else:
    print(salary)

zp = int(input())
if zp > 20000:
    print(zp - (zp / 100 *13))
else:
    print(zp)

a=int(input())
if a<20000:
    print(a)
else:
    print(a-(a*0.13))

word = input()
if word == 'Python':
    print('ДА')
else:
    print('НЕТ')

print("ДА" if input() == "Python" else "НЕТ")
print(('НЕТ', 'ДА')['Python' == input()])

a, b = int(input()), int(input())
print(a if a > b else b)

a, b = int(input()), int(input())
print((a, b)[a < b])

print(max([int(input()) for _ in range(2)]))

num = int(input())
if num == str(num[::-1]):
    print('YES')
else:
    print('NO')

n = input()
print("YES" if n == n[:: -1] else 'NO')

[print(('NO', 'YES')[s == s[::-1]]) for s in [input()]]

a, b, c = map(int, input().split())
print('NO' if a+b-c else 'YES')

a, b, c = map(int, input().split())
print('YES' if a + b == c else 'NO')

a, b, c = (int(i) for i in input().split())
print(('YES', 'NO')[a + b != c])

print(['NO', 'YES'][(lambda x, y, z: x + y == z)(*map(int,input().split()))])

s = input()
t = input()
if t == str(s[::-1]):
    print('YES')
else:
    print('NO')

print('YES' if input() == input()[::-1] else 'NO')

s, t = input(), input()
print('YES' if s == t[::-1] else 'NO')

s = ''.join(reversed(str(input())))
t = input()
if s == t:
    print("YES")
else:
    print("NO")

a, b, c = int(input()), int(input()), int(input())
if a+b>c and b+c>a and c+a>b:
    print('YES')
else:
    print('NO')

a, b, c = int(input()), int(input()), int(input())
d = [a, b, c]
d.sort()
if d[2] < (d[0] + d[1]):
    print('YES')
else:
    print('NO')

    A, B, C = sorted([int(input()) for _ in range(3)])
    print('YES' if A + B > C else 'NO')
a,b,c = sorted([int(input()) for _ in 'abc'])
print('YES' if a+b > c else 'NO')

n = input().rjust(6, '0')
a = n[:3]
b = n[3:]
a = [int(i) for i in a]
b = [int(i) for i in b]
if sum(a) == sum(b):
    print('YES')
else:
    print('NO')

a, b = input(), input()
a = (ord(a[0]) + int(a[1])) % 2 == 0
b = (ord(b[0]) + int(b[1])) % 2 == 0

if a == b:
    print('NO')
else:
    print('YES')

a, b = input(), input()
a = (ord(a[0]) + int(a[1])) % 2 == 0
b = (ord(b[0]) + int(b[1])) % 2 == 0

if a == b:
    print('NO')
else:
    print('YES')

print((a  *  (-1)**a  -  a  %  2)  //  2)