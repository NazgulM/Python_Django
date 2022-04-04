text = 'Hello there'
print(text)

text1 = '''Hello there
How are you doing?'''
print(text1)

text2 = "He said, \"What's there?\""
print(text2)

text3 = 'Python'
print(text3[0])
print(text3[3])
print(text3[-1])
print(text3[1:4])
print(text3[:4])
print(text3[2:])

text4 = 'Python'
text5 = 'Programming'
result = text4 + " " + text5

print(result)

text6 = 'Python'
new_text = text6 * 3
print(new_text)
print(len(text6))
for character in text6:
    print(character)

print("P" in text6)
print('th' in text6)

text7 = 'I like Python 3'
result = text7.lower()
print(result)

result2 = text7.upper()
print(result2)

result3 = text7.find('Python')
print(result3)

result4 = text7.replace('Python 3', 'Java')
print(result4)

quote = "Talk is cheap. Show me the code."

print("1.", quote[3])
print("2.", quote[-3])
print("3.", quote.replace("code", "program"))


