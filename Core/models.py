from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table  # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker, relationship  # type: ignore

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


student_courses = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    
    courses = relationship(
        "Course", secondary=student_courses, back_populates="students"
    )


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Many-to-Many əlaqəsi - Hər kursun bir neçə tələbəsi ola bilər
    students = relationship(
        "Student", secondary=student_courses, back_populates="courses"
    )


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
