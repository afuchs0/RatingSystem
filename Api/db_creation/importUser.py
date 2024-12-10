import pandas as pd
from sqlalchemy import create_engine
def add_users():
    # Load the CSV file
    users_data = pd.read_csv("../data/users.csv")

    # Keep only the relevant columns
    columns_to_import = ["id", "age"]
    users_to_import = users_data[columns_to_import]
    users_to_import = users_to_import.drop_duplicates(subset=["id"], keep="first")
    # Configure the database connection
    db_path = 'instance/library.db'  # Replace with the actual path to the database
    engine = create_engine(f'sqlite:///{db_path}')

    # Import data into the users table
    try:
        users_to_import.to_sql('users', engine, if_exists='append', index=False)
        print("Users have been successfully imported into the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
