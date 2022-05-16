print(input()[0])

print(input()[-1])

st_r = input()
while len(st_r) > 1:
    st_r = st_r[1:]
print(st_r)

s = str(input())
print(s[len(s)-1])

print(input()[0:4])

print(input()[-4:])

st1 = input()
print(st1[len(st1)-4:])

s = str(input())
print(s[::2])

n = input()
print(*[n[i] for i in range(0, len(n), 2)], sep='')

print(input()[1::2])

print(input()[::-3])

a = input()
print(a[-1] + a[:-1])
