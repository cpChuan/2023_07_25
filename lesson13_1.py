import student
#.py檔沒有display，只能用print
stu1 = student.Student("Ting", 100, 100, 100)
print((stu1.name, stu1.chinese, stu1.english, stu1.math))
print((stu1.total(), stu1.average))
print(stu1)

stu2 = student.get_student("Amy")
print((stu2.name, stu2.chinese, stu2.english, stu2.math))
print((stu2.total(), stu2.average))
print(stu2)