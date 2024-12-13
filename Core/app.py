from models import Course,Student,session

course1 = Course(name="Python Programming")
course2 = Course(name="Database Management")
student1 = Student(name="Ali")
student2 = Student(name="Vəli")

student1.courses = [course1, course2]
student2.courses = [course1]

course1.students = [student1, student2]
course2.students = [student1]

session.add(student1)
session.add(student2)
session.add(course1)
session.add(course2)
session.commit()

