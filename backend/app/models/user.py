from sqlalchemy import ARRAY, Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    surname = Column(String(100), unique=True, nullable=True)
    generi_preferiti = Column(ARRAY(String))
    age  = Column(String(100), unique=True, nullable=False)

    visualisations = relationship("Visualisation", back_populates="user")


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