# Change list Items
fruits = ['Apple', 'Orange', 'Pears', 'Watermelon', 'Mango','Grapes', 'Orange']
print(fruits)

fruits[1] ='Guava'
print()
print(fruits)

print()
# replace 2 items
fruits[2:4] = ['Apple', 'Orange']
print(fruits)

fruits[1:2] = ['Kiwi', 'Mango']
print()
print(fruits)

# replace 2 items with single item
print()
fruits[1:3] = ['Pomegranate']
print(fruits)

print()
fruits.insert(1, 'Mango')
print(fruits)
print()


me = 'Nazgul'
you = 'is Best'

print(me,you)

me,you = you,me
print(me,you)

temp = me
me = you
you = temp
print(me,you)

print()
data = ['a', 'b', 'c', 'd','e','f','g', 'h']

index = 0
print(data[index], data[-index-1])
data[index], data[-index-1] = data[-index-1], data[index]
print(data[index],data[-index-1])
