from sqlalchemy import ARRAY, Column,  Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
     __tablename__ = 'books'
     id = Column(Integer, primary_key=True)
     bookId= Column(String(100), nullable= False)
     title = Column(String(100), nullable= False )
     series = Column(String(100), nullable = False)
     author = Column(String(100))
     rating = Column(String(100))
     description= Column(String(100))
     language = Column(String(100), nullable = False)
     isbn = Column(String(100), nullable = False)
     genres = Column(ARRAY(String(100)), nullable=True)
     charaters = Column(ARRAY(String(100)), nullable=True)
     bookFormat = Column(String(100), nullable=True)
     edition = Column(String(100), nullable=True)
     pages = Column(String(100), nullable = False)
     publisher= Column(String(100),nullable=True )
     publishDate= Column(String(100), nullable=True)
     firtPublisherDate = Column(String(100), nullable=True)
     awards = Column(ARRAY(String(100)), nullable=True)
     numRating = Column(String(100), nullable=True)
     ratingsByStars=Column(ARRAY(String(100), nullable= True))
     likedPercent= Column(String(100), nullable=True)
     setting =Column(ARRAY(String(100), nullable=True))
     coverImg= Column(String(200),nullable=True)
     bbeScore = Column(String(100))
     bbeVote = Column(String(100), nullable=True)
     price = Column(String(100), nullable = False)
     
     
     def to_dict(self):
          return{"id":self.id,   
                "bookId": self.bookId, 
                "title":self.title, 
                "series":self.series, 
                "author":self.author,
                "rating": self.rating,
                "description":self.description,
                "language":self.language, 
                "isbn":self.isbn, 
                "genres":self.genres,
                "charaters": self.charaters, 
                "bookFormat":self.bookFormat,
                "edition": self.edition,
                "pages": self.pages, 
                "publisher": self.publisher,
                "publishDate":self.publishDate,
                "firtPublisherDate":self.firtPublisherDate,
                "awards": self.awards,
                "numRating":self.numRating,
                "ratingsByStars": self.ratingsByStars,
                "likedPercent": self.likedPercent,
                "setting": self.setting,
                "coverImg":self.coverImg, 
                "bbeScore": self.bbeScore,
                "bbVote": self.bbeVote,
                "price":self.price, 
                }
     

     def update(self, data):
        for key,value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)