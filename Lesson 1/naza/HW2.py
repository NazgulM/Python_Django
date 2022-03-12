# Task 1, input from user and output in reverse version
text = input('Please enter some text: ')
print(text[::-1])

# Task 2 - srez slov
text2 = 'I am studying course Python Django'
print(text2[21:])

#Task 3 - ubrat lishnie znaki s raznyh storon
text3 = '$$$Python@@@'
text4 = '%%%Programming'
text5 = 'City&&&'
text6 = '****Computer***'
print(text3.strip('$ @'))
print(text4.lstrip('%'))
print(text5.rstrip('&'))
print(text6.strip('*'))

# Task 4 input info from the user
number = input('Please enter your favorite number: ')
color = input("Your favorite color: ")
city = input('Favorite city: ')
eat = input('Your favorite meal: ')
# format method
print('\nNumber: {0}\nColor: {1}\nCity: {2}\nYour favorite meal: {3} '.format(number, color, city, eat))
# f row
print(f'\nFavorite number: {number}\nFavorite color: {color}\nFavorite city: {city}\nFavorite meal: {eat} ')