grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a = grades[0]
b = grades[1]
c = grades[2]
d = grades[3]
e = grades[4]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
students = dict.fromkeys(students)
students["Aaron"] = sum(a)/len(a)
students['Bilbo'] = sum(b)/len(b)
students['Johnny'] = sum(c)/len(c)
students['Khendrik'] = sum(d)/len(d)
students['Steve'] = sum(e)/len(e)
print(students)