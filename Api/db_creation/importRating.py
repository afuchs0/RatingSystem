import pandas as pd
from sqlalchemy import create_engine
def add_ratimgs():
    # Load the CSV file
    ratings = pd.read_csv("../data/ratings_updated.csv")

    # Keep only the relevant columns
    columns_to_import = [
        "user_id","book_id","rating","rating_date"
    ]
    ratings_to_import = ratings[columns_to_import]
    # Configure the database connection
    db_path = 'instance/library.db'  # Replace with the actual path to the database
    engine = create_engine(f'sqlite:///{db_path}')

    # Import data into the books tablea
    try:
        ratings_to_import.to_sql('ratings', engine, if_exists='append', index=False)
        print("Ratings have been successfully imported into the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
