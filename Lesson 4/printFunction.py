print(1, 2, 3, sep=', ')
print(4, 5, sep='??')

print(1, 2, 3, sep=', ', end=' ')
print(4, 5, sep='??')

usd = 10
cents = 99
print(f'I have {usd} USD and {cents} cents')
print('I have %s USD and %s cents' % (usd, cents))

a,b,c = map(int,input().split())
print(a,b,c, sep=',')

print(*input().split(), sep=',')

print(input().replace(' ',','))

print(','.join(input().split()))

a=int(input())
print((a-1),a,(a+1),sep=' < ')

a = int(input())
print('%s < %s < %s'%(a-1, a, a+1))

n = int(input())
print(f'{n - 1} < {n} < {n + 1}')

n = int(input())
a = n -1
b = n +1
print("%s < %s < %s"%(a,n,b))

n = int(input())
print(f"{n-1}<{n}<{n+1}")

print(input(), input(), input(), sep='---')

print(*[input() for _ in range(3)], sep='---')

print('---'.join([input() for _ in range(3)]))

a = []
for _ in range(3):
    a.append(input())

print(*a, sep="---")

a = [input() for i in range(3)]
print(a[0],a[1],a[2],sep ="---")

words = [input() for i in range(3)]

print(*words, sep='---')

