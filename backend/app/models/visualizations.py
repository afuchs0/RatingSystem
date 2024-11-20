from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Visualisation(Base):
    __tablename__ = 'visualisations'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    reading_date = Column(Date, nullable=True)  # Nouvelle colonne pour la date de lecture
    
    # Relations avec User et Book
    user = relationship("User", back_populates="visualisations")
    book = relationship("Book", back_populates="visualisations")  

    def to_dict(self):
        return{"id":self.id, "user_id":self.user_id, "book_id": self.book_id, "reading_date":self.reading_date}
    
    def update(self, data):
        for key,value in data.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)
