marks = [4, 5, 6, 7]
t_july = [20, 24, 30, 34, 43, 12, 23]
a = [True, 43, 'hello', 5.4, [4, 5, 6]]
print(type(a))
print(len(a))
a = ['hi'] + a
print(a)
b = [0] *5
print(b)
print(5.4 in a)
w = [43, 54, 65, 3, 4, 65, -43, 32]
print(max(w))
print(min(w))
print(sum(w))
print(sorted(w))
print(sorted(w, reverse=True))
print([100, 54] > [34, 543, 654, 43])
print(sum(marks)/len(marks))

s = list(map(int, input('Please enter the numbers: ').split()))
print(s)
print(min(s))

my_list = list(map(int, input().split()))
print(777 in my_list)

print(777 in list(map(int, input().split())))

list_numbers = list(map(int, input().split()))
print(sum(list_numbers))

print(sum(list(map(int, input().split()))))

mas = list(map(int, input().split()))
print(min(mas), max(mas))

print(*[f'{min(a)} {max(a)}' for a in [list(map(int, input().split()))]])


list_numbers = list(map(int, input().split()))
print(sum(list_numbers) / len(list_numbers))


numbers = [int(i) for i in input().split()]
print(sum(numbers) / len(numbers))

print((lambda li: sum(li)/len(li))([*map(int,input().split())]))