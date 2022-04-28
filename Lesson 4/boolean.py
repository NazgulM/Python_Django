print(int(input()) > 0) # positive number true

x = int(input())

print(bool(x + abs(x)))

n = int(input())
print(bool(n>0))

print(int(input()) % 2 == 0) # even numbers true

print(not int(input()) % 2)

print(bool(int(input())%2-1))

''' Кратно 6 '''
print(not int(input()) % 6)

n = int(input())
print(n%6==0)

print(not bool(int(input())%6))

"""Программа должна вывести True, 
если введенное значение не делится на 9, в противном случае - False."""

print(int(input()) % 9!=0)
print(bool(int(input()) % 9))

print(not not int(input()) % 9)

"""
Программа должна вывести True, если у введенного числа последняя цифра 2
"""
print(int(input())%10==2)

a = int(input())
print(a%10==2)

print(input()[-1] is "2")

print(not(int(input()) % 10 - 2))

"""
Программа должна вывести True, если оба числа делятся на 7, в противном случае - False.
"""

a,b = map(int, input().split())
print(a%7==0 and b%7 ==0)

"""
Необходимо вывести True, если данные стороны образуют правильный треугольник,
 в противном случае - False.
"""
a,b,c = map(int, input().split())
print(a==b==c)

print(len(set(input().split())) == 1)

print(*[a==b==c for a,b,c in [map(int,input().split())]])

"""
Программа должна вывести True, если введенное значение принадлежит интервалу от 5 
не включительно до 19 включительно , в противном случае - False.
"""

print(5 < int(input()) <= 19)

a = int(input())
print( 5 < a <= 19)

print(input() == 'awesome' or input() == 'awesome')

print('awesome' in {input(), input()})

a=str(input())
b=str(input())
print(a=='awesome' or b=='awesome')

print('awesome' in [input(),input()])

a, b, c = map(int, input().split())
print(a == b or a == c or b == c)

a,b,c=map(int,input().split())
print((min(a,b))==(min(b,c)))

print(len(set(input().split())) < 3)

''' Двузначное '''
print(int(input()) in range(10, 100))

a = int(input())
print(a // 100 == 0 and a // 10 != 0)

a = int(input())
print(10 <= a <= 99)

print(10<int(input())<=99)

a,b,c = map(int, input().split())
print((a**2+b**2==c**2) or (c**2+a**2==b**2) or (c**2+b**2==a**2))

f = sorted(map(int,input().split()))
print(f[0]**2 + f[1]**2 == f[2]**2)