grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
a = grades[0]
a = (sum(a)) / len(grades[0])
b = grades[1]
b = (sum(b)) / len(grades[1])
c = grades[2]
c = (sum(c)) / len(grades[2])
d = grades[3]
d = (sum(d)) / len(grades[3])
e = grades[4]
e = (sum(e)) / len(grades[4])
grades = [a, b, c, d, e]
GPA = dict()
GPA.update({students[0]: grades[0],
            students[1]: grades[1],
            students[2]: grades[2],
            students[3]: grades[3],
            students[4]: grades[4]})
print(GPA.items())
