from models.books import Book
from random import randint
import pandas as pd

def csv_to_books():

    data = pd.read_csv("books.csv")
    
    books = []
    # Loop over the dataframe rows and create Book objects
    for _, row in data.iterrows():
        if row['price'] == '':
            row['price'] = randint(1,20)
        book = Book(
            id=row['bookId'],
            title=row['title'],
            serie=row['series'],
            author=row['author'],
            desc=row['description'],
            lang=row['language'],
            ISBN=row['isbn'],
            genres=row['genres'],
            npag=row['pages'],
            nawards=row['awards'],
            avg_vote=row['likedPercent'],
            price=row['price']
        )
        books.append(book)
    
    return books


# Convert the CSV to a list of Book objects
books_list = csv_to_books()