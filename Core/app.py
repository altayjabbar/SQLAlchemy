from sqlalchemy import create_engine, Column, Integer, String  # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker  # type: ignore
import random

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


# user1 = User(name="John", age=30)
# user2 = User(name="fex", age=29)
# user3 = User(name="defg", age=343)
# session.add_all([user1,user2,user3])  
# session.commit()


# users = session.query(User).filter(User.id > 1, User.id < 9).all()
# if users:
#     for user in users:
#         print(f"User found: ID={user.id}, Name={user.name}, Age={user.age}")
# else:
#     print("No user found.")


# x=session.query(User).filter(User.name  == 'fex').delete()
# session.commit()
# print(x)



# user_to_update = session.query(User).filter(User.id ==16).first()
# if user_to_update:
#     user_to_update.name = "Maykl"
#     user_to_update.age = 39

#     session.commit()
# else:
#     print("none")

# users = session.query(User).all()  

# if users:
#     for user in users:
#         print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
# else:
#     print("No users found.")

# y = session.query(User).filter(User.age== 343 ).delete()
# session.commit()

names= ['Alice','Darvin','James','Foden']
ages = [23,54,76,4,23,51,66,23,13,39]

# for x in range(20):
#     user = User(name=random.choice(names),age=random.choice(ages))
#     session.add(user)
# session.commit()


users = session.query(User).order_by(User.name).all()

for user in users:
    print(f'User age:{user.age},name:{user.name},id:{user.id}')
