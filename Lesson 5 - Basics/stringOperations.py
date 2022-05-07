print('hello\nworld\n456')
d = 'hello'
e = 'world'
# Concatenation
print('abc' + 'dec')
print(d + ' ' + e)
print('abc' + str(3))
print(len('abc'))
a = 'Normal practice'
print('You entered', len(a), 'symbols')
b = '@#$4567'
print('4' in b)
print('54' in b)
print('AAA' == 'BBB')
print('a'>'A')
print('zxcv' <= 'asdf')

print('Я стану крутым программистом!\n'*3)

a = 'Я стану крутым программистом!'
print(a,a,a, sep = '\n')

print("""Я стану крутым программистом!
Я стану крутым программистом!
Я стану крутым программистом!""")

n='Я стану крутым программистом!'
print((n+'\n')*3)

print(*['Я стану крутым программистом!' for i in range(3)], sep='\n')

d='Я стану крутым программистом!\n'
print(d*3)

a = 'Я стану крутым программистом!'

for i in range(3):
    print(a)

print('Я стану крутым программистом!\nЯ стану крутым программистом!\nЯ стану крутым программистом!')

print("W"*777)

a = 'WWWWWWW'
print(a*111)

[print('W', end='') for _ in range(777)]

print('Лев Николаевич Толстой написал "Война и мир"')

print("Лев Николаевич Толстой написал \"Война и мир\"")

s = '«Лев Николаевич Толстой написал "Война и мир"»'
print(s[1:-1])

print(input().lstrip("<<").rstrip(">>"))
print(input().replace('«','').replace('»',''))



