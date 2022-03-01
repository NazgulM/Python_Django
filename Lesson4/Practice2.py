# Print out from 20 to 10
# i = 20
# while i >= 10:
#     print(i)
#     i -= 1

guess = input('Please enter a password')
password = 'qwerty'
count = 0
while guess != password:
    print('Wrong password')
    guess = input()
    if guess == password:
        print("You are right")

