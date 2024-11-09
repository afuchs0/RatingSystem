from sqlalchemy import Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(100), unique=True, nullable=False)
    age  = Column(String(100), unique=True, nullable=False)


    def to_dict(self):
        return{"id":self.id, "name":self.name, "surname": self.surname, "age":self.age}


    def update(self, data):
        for key,value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)
    
    def update(self, data):
        for key,value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)