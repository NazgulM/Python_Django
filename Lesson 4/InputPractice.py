from decimal import Decimal as D

# a,b,c = (int(input()) for i in range(3))
# first = a+b*c
# second = a*(b+c)
# third = a*b*c
# fourth = (a+b)*c
# fifth = a+b+c
# print(max(first, second, third, fourth, fifth))
#
# a, b, c = (int(input()) for _ in range(3))
# print(max(a*b*c, a+b+c, (a+b)*c, a*(b+c)))
#
# a = int(input())
# b = int(input())
# c = int(input())
# print(max((a+b+c), (a*b+c), (a+b*c), ((a+b)*c), (a*(b+c)), (a*b*c)))
#
# print((lambda a=int(input()), b=int(input()), c=int(input()):
#       max(a + b + c, a * (b + c), (a + b) * c, a * b * c))())
#
#
# a = float(input())
# print(round(a,2), round(a,3))

print(D('2.1') + D('4.5'))


(lambda x: print(round(x, 2), round(x, 3)))(float(input()))

