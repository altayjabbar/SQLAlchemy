from sqlalchemy import create_engine, Column, Integer, String, ForeignKey  # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker, relationship  # type: ignore

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class University(Base):
    __tablename__ = 'universities'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship("Student", back_populates='university')  # 'Students' əvəzinə 'Student' yazılmalıdır


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    university_id = Column(Integer, ForeignKey('universities.id'))  # 'universites.id' düzəldildi

    university = relationship('University', back_populates='students')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


