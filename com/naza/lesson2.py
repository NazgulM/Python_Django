word = 'some word'# Probel toje imeet poryadkovyi nomer
print(word[2])
print('The length of word: ', len(word))

age = int(input('Enter age: '))
print(type(age))
number1 = 40
number2 = 65
totalAge = age + number1+number2
totalAge2 = totalAge
print(totalAge)
print(type(totalAge2))
totalAge = str(totalAge2)
print(type(totalAge2))

#word2 = input('Type second word: ')
#print(word2)
resultText = 'Info from lesson:\n' + word + '\n' + str(age)
print('Information from lesson:\n', word, '\n', age, '\n', )
print(resultText)

poem = """
    Hard to picture, but these Goliath trees
    are taller still than Robeson. Outside
    vast plate windows in this lecture hall,
    I imagine him running down autumn
"""
print(poem)
if 'Hard' in poem:
    print('Yes, it has')
else:
    print("No")
    if 'Yes' not in poem:
        print('No, it has not')
    else:
        print("Yes")