import pandas as pd
from sqlalchemy import create_engine
def add_genres():
    # Load the CSV file
    genres = pd.read_csv("../data/genres.csv")

    # Keep only the relevant columns
    columns_to_import = [
        "id","name"
    ]
    genres_to_import = genres[columns_to_import]
    genres_to_import = genres_to_import.drop_duplicates(subset=["name"], keep="first")
    # Configure the database connection
    db_path = 'instance/library.db'  # Replace with the actual path to the database
    engine = create_engine(f'sqlite:///{db_path}')

    # Import data into the books tablea
    try:
        genres_to_import.to_sql('genres', engine, if_exists='append', index=False)
        print("Genres have been successfully imported into the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
