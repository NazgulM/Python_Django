a = str(input().lower())
b = str(input().lower())
if a > b:
    print('1')
elif a < b:
    print('-1')
else:
    print('0')


a, b = input().lower(), input().lower()
print(int(a > b) - int(b > a))

a = input().lower()
b = input().lower()
print(-1 if a < b else 1 if b < a else 0)
