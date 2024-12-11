from sqlalchemy import create_engine, Column, Integer, String, create_engine  # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker  # type: ignore

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
Base = declarative_base()


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


user = User(name="John", age=30)
user1 = User(name="fex", age=29)
session.add(user1)
session.commit()
users = session.query(User).all()

print(users)
