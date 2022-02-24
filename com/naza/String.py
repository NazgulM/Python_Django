# Slicing method==Srezy strok
# [start:stop:step]
# printing out without s
word = 'some word'
print(word[2])

word_No_s = word[1:]
print(word_No_s)

# printing word some
word_some = word[0:4]
print(word_some)
# printing word
print(word[5:9])
print(word[5:])
# print from the end
print(word[:-1])
print(word[:-2])
# print me and wo
print(word[2:-2])
# print reverse
print(word[::-1])

word2 = "HelloThere"
# elT
print(word2[1:7:2]) # elT
print(word2[1:9:3])

# search index in sentence
word3 = "I live in Bishkek"
print(word3.find('Bishkek'))
print(word3.find('live'))
# search with rfind
print(word3.rfind('in'))

# method replace
print(word3.replace('Bishkek', 'Moscow'))
word3 = word3.replace('Bishkek', 'Brussels')
print(word3)

word4 = 'I love Bishkek Bishkek and my parents live in Bishkek and I study in Bishkek'
print(word4.count('Bishkek'))
print(word4.count('I'))

# methods
text2 = 'my name is Naza'
print(text2.upper())
upperText = text2.upper()
print(upperText)

lowerCaseText = upperText.lower()
print(lowerCaseText)
capitalizedText = lowerCaseText.capitalize()
print(capitalizedText)

filename = 'myFile.pdf'
fileName2 = 'lessonFile.pdf'
fileName3 = 'myLesson.pdf'

if filename.endswith('.pdf'):
    print("Accept")
else:
    print("Please change your file")

if fileName3.startswith('lessonFile'):
        print("Accept")
else:
        print("Do not accept with this file name")


longWord = '       Some Text      '
print(longWord.lstrip())
print(longWord.rstrip())
print(longWord.strip())

someText = '%%%Do Something%%%'
print(someText.lstrip('%'))
print(someText.rstrip('%'))
print(someText.strip('%'))




