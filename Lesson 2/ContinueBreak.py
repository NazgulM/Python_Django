# for item in range(1, 6):
#     # print(item)
#     # break
#     if item == 3:
#         break
#         print(item)
#     print('The end')

# while True:
#     number = float(input('Enter a number: '))
#     if number < 0:
#         break
#     print('You entered number: ', number)
# for i in range(5):
#     number = float(input('Enter a number: '))
#     if number < 0:
#         continue
#     print(number)

# Task
# Create a program so that all items of the list are printed except Swift and C++

languages = ['Python', 'Java', 'Swift', 'C', 'C++']

for i in languages:
    if i == 'Swift' or i == 'C++':
        continue
    print(i)

