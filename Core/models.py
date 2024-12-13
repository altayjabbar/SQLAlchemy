from sqlalchemy import create_engine, Column, Integer, String, ForeignKey  # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker, relationship  # type: ignore

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    id = Column(Integer, primary_key=True)

class Address(BaseModel):
    __tablename__ = "addresses"
    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id = Column(ForeignKey("users.id"))
    user = relationship('User',back_populates = 'addresses')
    def __repr__(self):
        return f"Address(id={self.id}, city = {self.city})"

class User(BaseModel):
    __tablename__ = 'users'
    name = Column(String)
    age = Column(Integer)
    addresses = relationship("Address", back_populates = 'user')   

    def __repr__(self):
        return f"Address(id={self.id}, city = {self.city})"


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
