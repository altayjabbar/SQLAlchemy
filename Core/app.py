from models import University,Student,session

university1 = University(name="Bakı Dövlət Universiteti")
university2 = University(name="UNEC")

student1 = Student(name="Elnur", university=university1)
student2 = Student(name="Aygün", university=university2)


session.add(university1)
session.add(university2)

session.add_all([student1, student2])
session.commit()

