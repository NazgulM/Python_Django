from datetime import datetime
from statistics import mean
# a = float(input('Please enter a: '))
# b = float(input('Please enter b: '))
# c = float(input('Please enter c: '))
#
# p = a+b+c
# print(p)

# a,b,c = map(int, input().split())
# p = a+b+c
# print(p)

# a = int(input('Please enter the number: '))
# print(a*a)
#
# age = int(input())
# print(age+1)
#
# a,b = map(int, input().split())
# total = a+b
# print(total)
# total = int(input())
# print(int(total/6),int(2*total/3),int(total/6))

a,b,c = map(int, input().split())
x = 3
y = 5
z = 12
print((a * x) + (b * y) + (c * z))

n,a,b  = map(int, input().split())
print(n*a*b*2)

a,b,c,d = map(int, input().split())
print((a+b+c+d)/4)

print(sum(map(int, input().split())) / 4)

print(mean(map(int, input().split())))

print(*[sum(s) / len(s) for s in [[int(i) for i in input().split()]]])

mark = list(map(int, input().split()))
print(sum(mark) / len(mark))

print((lambda d=list(map(int, input().split())): sum(d) / len(d))())

points = input().split()
points_lst = []

for point in points:
    point = int(point)
    points_lst.append(point)

result = sum(points_lst) / len(points_lst)

print(result)

h1, m1, s1, h2, m2, s2 = [int(input()) for _ in range(6)]
x = (h1*3600)+(m1*60)+s1
y = (h2*3600)+(m2*60)+s2
print(y-x)

h1, m1, s1, h2, m2, s2 = (int(input()) for _ in range(6))
print(3600 * (h2 - h1) + 60 * (m2 - m1) + (s2 - s1))

time1 = int(input()) * 3600 + int(input()) * 60 + int(input())
time2 = int(input()) * 3600 + int(input()) * 60 + int(input())
print(time2 - time1)

h1= int(input())*3600
m1= int(input())*60
s1= int(input())
h2= int(input())*3600
m2= int(input())*60
s2= int(input())
print((h2+m2+s2)-(h1+m1+s1))

a,b = (int(input()) for i in range(2))
print(abs(a)+abs(b))

print(sum(abs(int(input())) for _ in 'ab'))

print(abs(int(input())) + abs(int(input())))

one = datetime(year=9, month=9, day=9, hour=int(input()), minute=int(input()), second=int(input()))
two = datetime(year=9, month=9, day=9, hour=int(input()), minute=int(input()), second=int(input()))
delta = two - one
print(delta.seconds)

(lambda a, b: print(b - 1, a - 1))(*map(int, input().split()))

print(sum(int(input().lstrip('-')) for _ in range(2)))

print(eval('+'.join((map(str,(abs(int(input()))for i in range(2)))))))

a,b = map(float, input().split())
print(abs(a-b))

x1, x2 = map(float, input().split())
print(max(x1, x2) - min(x1, x2))

a,b = map(float,input().split())
if a < 0 and b >= 0:
    print(abs(a) +abs(b))
if a >= 0 and b < 0:
    print(abs(a) +abs(b))
if a < 0 and b < 0:
    print(abs(a-b))
if a >= 0 and b >= 0:
    if b > a:
        print(b-a)
    if a > b:
        print(a-b)


a, b, c, d, e = map(int, input().split())
print(max(a, b, c, d, e))

print(max(input().split(), key=int))

num = list(map(int, input().split()))
for i in num:
    if i<1 or i>100:
        print('Error!')
        break
    else:
        print(max(num))
        break


