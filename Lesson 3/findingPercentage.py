n = int(input('Please enter the number of students: '))
student_marks = {}
for _ in range(n):
    name, *line = input('Please enter the name and marks: ').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
result = list(student_marks[query_name])
per = sum(result) / len(result)
print("%.2f" % per)