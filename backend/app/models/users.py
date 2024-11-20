from sqlalchemy import ARRAY, Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    passWord= Column(String(100),nullable=False )
    generi_preferiti = Column(ARRAY(String))
    age  = Column(String(100), unique=True, nullable=False)
    visualisations = relationship("Visualisation", back_populates="user")



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
   
    def to_dict(self):
        return{"id":self.id, "email":self.email, "passWord": self.passWord, "generi_preferiti":self.generi_preferiti, "age":self.age}


    def update(self, data):
        for key,value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)
    
    