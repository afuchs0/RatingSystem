import pandas as pd
from sqlalchemy import create_engine
import ast
def add_fav():
    genres = pd.read_csv("../data/genres.csv")
    columns_to_import = [
        "id","name"
    ]
    genres_to_import = genres[columns_to_import]
    genres_to_import = genres_to_import.drop_duplicates(subset=["name"], keep="first")
    users = pd.read_csv("../data/users.csv")
    columns_to_import = [
        "id","age","generi_preferiti"
    ]
    users_to_import = users[columns_to_import]


    # Configure the database connection

    # Espandere i generi in righe separate

    users_to_import["generi_preferiti"] = users_to_import["generi_preferiti"].apply(ast.literal_eval)
    users_expanded = users_to_import.explode("generi_preferiti")
    users_expanded["generi_preferiti"] = users_expanded["generi_preferiti"].str.strip()
    #books_expanded = books_to_import.assign(new_genres=books_to_import["new_genres"].str.split(","))

    # Mappare i nomi dei generi agli ID dei generi
    users_with_genres = users_expanded.merge(genres_to_import, left_on="generi_preferiti", right_on="name", how="inner")
    # Creare la tabella di relazione
    user_genres = users_with_genres[["id_x", "id_y"]].rename(columns={"id_x": "user_id", "id_y": "genres_id"})

    db_path = 'instance/library.db'  # Replace with the actual path to the database
    engine = create_engine(f'sqlite:///{db_path}')

    # Import data into the books tablea
    try:
        user_genres.to_sql('favourite', engine, if_exists='append', index=False)
        print("User-genres have been successfully imported into the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
