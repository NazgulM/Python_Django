# a = 47
# if a%5 ==0:
#     if a>9 and a<100:
#         print(1)
#         print(2)
#     else:
#         print(3)
#         print(4)
# else:
#     if a%2==0:
#         print(5)
#         print(6)
#     else:
#         print(7)
#         print(8)
# print('end')
#
#
# a = 12
# b = 20
# c = 30
#
# if a<b:
#     if a<c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b<c:
#         print(b)
#     else:
#         print(c)
#
# a,b = int(input()), int(input())
# if a < b:
#     print('<')
# elif a > b:
#     print('>')
# elif a == b:
#     print('=')
#
# A, B = int(input()), int(input())
# print('>'*(A>B) + '<'*(A<B) + '='*(A==B))
#
# A, B = int(input()), int(input())
# print(['=', '>', '<'][(A > B) - (A < B)])

# a,b,c = int(input()), int(input()), int(input())
# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > c:
#         print(b)
#     else:
#         print(c)
# a,b,c=int(input()),int(input()),int(input())
# if a>b and a>c:
#     print(a)
# else:
#     if b>c and b>a:
#         print(b)
#     else:
#         print(c)
#
#         ''' Сравнение трёх '''
#         print((lambda a=int(input()), b=int(input()), c=int(input()): ((a, c)[a < c], (b, c)[b < c])[a < b])())

# a = int(input())
# if a %2==0:
#     print(a//2)
# else:
#     if a == 1:
#         print(0)
#     else:
#         print(a)

# a = int(input())
# print(a if a%2!=0 and a>1 else int(a/2))


# a,b,c, = map(int, input().split())
#
# if a > b and a > c:
#     if b < c:
#         print(a-b)
#     if c < b:
#         print(a-c)
# elif b > a and b > c:
#     if a < c:
#         print(b-a)
#     if c < a:
#         print(b-c)
# elif c > a and c > b:
#     if a < b:
#         print(c-a)
#     if b<a:
#         print(c-b)

# a, b, c =sorted(map(int, input().split()))
# print(c-a)
#
# a, b, c = map(int, input().split())
# if a < b: a, b = b, a
# if a < c: a, c = c, a
# if b < c: b, c = c, b
#
# print(a - c)

a, b = input().lower(), input().lower()

