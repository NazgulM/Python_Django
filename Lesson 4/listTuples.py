# list of integers
numbers = [1,2,3,4,-4]
print(numbers)

# mixed list
random_list = [2.5, 'Hello', -5, 2.5]
print(random_list)

# empty list
list1 = []
print(list1)
print(len(list1))

languages = ['Python', 'Java', 'Kotlin', 'C++']
print(languages)
print(languages[0])
print(languages[3])
print(languages[-1])
print(languages[-2])
print(languages[-4])

# slicing of the list
print(languages[0:3])
print(languages[1:3])
print(languages[::3])

#change items
languages[1] = 'Ruby'
print(languages)

languages[1:3] = ['Ruby', 'Dart']
print(languages)

print('Python' in languages)

for language in languages:
    print(language)

# append new item
languages.append('Rust')
print(languages)

languages.insert(1, 'Pascal')
print(languages)

languages1 = languages.copy()
print(languages1)

numbers1 = (21, -5, 6, 9)
print(numbers1)
print(numbers1[2])
print(numbers1[1:4])

for number in numbers1:
    print(number)




