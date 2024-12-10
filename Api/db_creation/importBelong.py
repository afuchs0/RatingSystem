import pandas as pd
from sqlalchemy import create_engine
import ast
def add_belongs():
    genres = pd.read_csv("../data/genres.csv")
    columns_to_import = [
        "id","name"
    ]
    genres_to_import = genres[columns_to_import]
    genres_to_import = genres_to_import.drop_duplicates(subset=["name"], keep="first")
    books_def = pd.read_csv("../data/books_def.csv")
    columns_to_import = [
        "bookId","new_genres"
    ]
    books_to_import = books_def[columns_to_import]
    books_to_import = books_to_import.drop_duplicates(subset=["bookId"], keep="first")

    # Configure the database connection

    # Espandere i generi in righe separate

    books_to_import["new_genres"] = books_to_import["new_genres"].apply(ast.literal_eval)
    books_expanded = books_to_import.explode("new_genres")
    books_expanded["new_genres"] = books_expanded["new_genres"].str.strip()
    #books_expanded = books_to_import.assign(new_genres=books_to_import["new_genres"].str.split(","))

    # Mappare i nomi dei generi agli ID dei generi
    books_with_genres = books_expanded.merge(genres_to_import, left_on="new_genres", right_on="name", how="inner")
    # Creare la tabella di relazione
    book_genres = books_with_genres[["bookId", "id"]].rename(columns={"bookId": "book_id", "id": "genres_id"})

    db_path = 'instance/library.db'  # Replace with the actual path to the database
    engine = create_engine(f'sqlite:///{db_path}')

    # Import data into the books tablea
    try:
        book_genres.to_sql('belong', engine, if_exists='append', index=False)
        print("Books-genres have been successfully imported into the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
