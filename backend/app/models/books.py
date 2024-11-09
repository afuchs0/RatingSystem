from sqlalchemy import Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
     __tablename__ = 'books'
     id = Column(Integer, primary_key=True)
     bookId= Column(String(100), nullable= False)
     title = Column(String(100), nullable= False )
     serie = Column(String(100), nullable = False)
     desc = Column(String(100), nullable = False)
     lang = Column(String(100), nullable = False)
     ISBN = Column(String(100), nullable = False)
     pages = Column(String(100), nullable = False)
     nawards = Column(String(100), nullable = False)
     avg_vote = Column(String(100), nullable = False)
     price = Column(String(100), nullable = False)

     def to_dict(self):
          return{"id":self.id, 
            "title":self.title, 
            "serie":self.serie, 
            "desc":self.desc, 
            "lang":self.lang, 
            "ISBN":self.ISBN, 
            "naward":self.naward, 
            "avg_vote":self.avg_vote,
            "price":self.price, 
            "author":self.author,
            "genres":self.genres
            }
     

     def update(self, data):
        for key,value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)