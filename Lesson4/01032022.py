# score = int(input('Enter your score'))
# if score > 50:
#     print('You have passed your exam')
# if score < 50:
#     print('You have failed your exam')

# For cycle
poem = """
    Hard to picture, but these Goliath trees
    are taller still than Robeson. Outside
    vast plate windows in this lecture hall,
    I imagine him running down autumn
"""
# i = 1
#
# while i < 10:
#     print(f'Repeat a poem {i} time: \n{poem}')
#     i = i+1;

count  = 10

while count < 15:
    print(count)
    count += 1

i = 1



# while i <= 10:
#     print(i * 2)
#     i +=1

# range(1, 10) # 1 - 9
# range(10) # 0 - 9
# range(1,20,2) # [1:20:2]
 # print every second element

for count in range(1,11):
    print(f'Repeat a poem {i} time: \n{poem}')

for count2 in range(10, 15):
    print(count2, end=' ')

for count3 in range(1,11):
    print(count3, end= ' ')

print('\n')

for count4 in range(11):
    print(count4, end=' ')
print('\n')

for count5 in range(1,20,2):
    print(count5, end=' ')
print('\n')

for count6 in range(1,20,5):
    print(count6, end=' ')

counter = 1
while counter <= 15:
    num = counter * 3
    print(f'Куб числа {counter} равно {num}')
    counter +=1

n = int(input('\nEnter a number till which you want to know sum: '))
currentNum = 1
totalSum = 0
while currentNum <= n:
    totalSum = totalSum + currentNum
    currentNum +=1; # currentNum = currentNum + 1
    print(totalSum)

