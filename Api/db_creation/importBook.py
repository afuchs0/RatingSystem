import pandas as pd
from sqlalchemy import create_engine
import os

def addBooks():
    db_path = os.path.abspath('instance/library.db')

    # Load the CSV file
    books_def = pd.read_csv("../data/books_def.csv")

    # Keep only the relevant columns
    columns_to_import = [
        "bookId", "title", "series", "author", "rating", 
        "description", "language", "pages", "publishDate", 
        "awards", "coverImg", "price"
    ]
    books_to_import = books_def[columns_to_import]
    books_to_import = books_to_import.drop_duplicates(subset=["bookId"], keep="first")
    # Configure the database connection
    engine = create_engine(f'sqlite:///{db_path}')

    # Import data into the books tablea
    try:
        books_to_import.to_sql('books', engine, if_exists='append', index=False)
        print("Books have been successfully imported into the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
