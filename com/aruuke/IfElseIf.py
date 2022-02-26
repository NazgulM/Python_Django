# age = int(input('Please enter age'))
age2 = 35
# if age >=25 and age <= 40:
# print('You are good for this job')
# else:
# print('Unfortunately we can not accept you')

# if age2 >= 25 and age2 <= 40:
    # print('You are good')
# else:
    # print('Sorry')

if age2 >= 25 or age2 <= 40:
    print("OK")
else:
    print('Sorry')

name1 = 'Aslan'
name2 = 'Sergei'
name3 = 'Timur'
name4 = 'Altynai'

nametoCheck = 'Aslan'
if nametoCheck == name1 or nametoCheck == name2 or nametoCheck == name3 or \
        nametoCheck == name4:
    print('You are that person who can help us')
else:
    print("Sorry")

    # if else ElIf
address1 = 'Mira 1'
address2 = 'Turusbekova 7'

adrressDostavki = input("please enter address")

if adrressDostavki == address1:
    print('Got my order')
else:
    print('Wrong address')

    # complex construction
age = int(input('Enter your age for voting: '))

if age >= 17:
    print("You can vote")
if age == 18:
    print('In case of your first vote, you can get a gift')
else:
    print('you not allowed to vote')
