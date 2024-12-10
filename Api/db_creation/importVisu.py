import pandas as pd
from sqlalchemy import create_engine
def add_visuals():
    # Load the CSV file
    visuals = pd.read_csv("../data/visualization.csv")

    # Keep only the relevant columns
    columns_to_import = [
        "user_id","book_id","reading_date"
    ]
    visuals_to_import = visuals[columns_to_import]
    # Configure the database connection
    db_path = 'instance/library.db'  # Replace with the actual path to the database
    engine = create_engine(f'sqlite:///{db_path}')

    # Import data into the books tablea
    try:
        visuals_to_import.to_sql('visualizations', engine, if_exists='append', index=False)
        print("Visuals have been successfully imported into the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
