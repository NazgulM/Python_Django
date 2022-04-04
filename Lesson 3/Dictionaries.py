person1 = {'name': 'Naza', 'age': 36}
print(person1)
print(person1['name'])
print(person1['age'])
print(person1.get('hobbies', ['dancing', 'fishing']))
person1['name'] = 'Dennis'
print(person1)
person1['hobbies'] = ['dancing', 'fishing']
print(person1)
person1.pop('name')
print(person1)
for key in person1:
    print(key)
    print(person1[key])
print()

person2 = {10: 'Naza', ('age'): 36}
print(person2)

synonyms = {"mountain": "peak", "forest": "jungle"}
print("1.", synonyms["mountain"])

synonyms["terrain"] = "land"
print("2.", synonyms)

synonyms.pop("forest")
print("3.", synonyms)

# Sets
print()
animals = {'dog', 'cat', 'tiger', 'elephant', 'dog'}
print(animals)
animals.add('monkey')
print(animals)
wild_animals = ['tiger', 'leopard', 'elephant']
animals.update(wild_animals)
print(animals)
animals.update(wild_animals, {'dolphins'})
print(animals)
animals.discard('cat')
print(animals)
animals.remove('monkey')
# animals.clear()
# print(animals)
print('tiger' in animals)
for animal in animals:
    print(animal)

print()
animals1 = set(['dog', 'cat', 'tiger', 'elephant', 'dog'])
print(animals1)
print()

domestic_animals = {'dog', 'cat', 'elephant'}
wild_animals1 = {'lion', 'tiger', 'elephant'}
animals = domestic_animals.union(wild_animals1)
print(animals)
animals = domestic_animals |wild_animals1
print(animals)
animals = wild_animals1.intersection(domestic_animals)
print(animals)
animals = wild_animals1 & domestic_animals
print(animals)

animals = {"dog", "cat", "tiger", "elephant", "dog"}
print("1.", animals)

animals.remove("cat")
animals.remove("dog")
print("2.", animals)

animals.add("snake")
print("3.", animals)

result = {1, 5, 10} & {100, 10, 3, 5}
print("4.", result)