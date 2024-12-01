import pandas as pd
import json
from api import app, db
from api import UserModel
# , BookModel, RatingModel, VisualizationModel
from datetime import datetime

# Function to import data from CSV files into the database
def import_data():
    # Read CSV files with pandas
    users_df = pd.read_csv('/RatingSystem/Api/data/users.csv')
    books_df = pd.read_csv('RatingSystem/Api/data/books_def.csv')
    ratings_df = pd.read_csv('/RatingSystem/Api/data/ratings.csv')
    visualizations_df = pd.read_csv('/RatingSystem/Api/data/visualization.csv')

    # Function to clean and convert string to float
    def clean_float(value):
        try:
            if isinstance(value, float):  # If it's already a float, return it as-is
                return value
            if pd.isna(value) or value in ['', 'nan']:  # Check for NaN or empty values
                return 0.0
            return float(value.replace('.', '').replace(',', '.'))  # Process string values
        except ValueError:
            return 0.0


    # Convert DataFrames to SQLAlchemy objects and add to session
    with app.app_context():
        # Add users
        users = [
            UserModel(
                idd=row['idd'],
                id=row['id'],
                age=row['age'],
                generi_preferiti=row['generi_preferiti']
            )
            for _, row in users_df.iterrows()
        ]
        db.session.add_all(users)

    #     # Add books
    #     books = [
    #         BookModel(
    #             id=row['bookId'],
    #             title=row['title'] if pd.notna(row['title']) else '',  # Default to an empty string if NaN
    #             serie=row['series'] if pd.notna(row['series']) else '',  # Default to an empty string if NaN
    #             desc=row['description'] if pd.notna(row['description']) else '',  # Default to an empty string if NaN
    #             lang=row['language'] if pd.notna(row['language']) else '',  # Default to an empty string if NaN
    #             pages=int(row['pages']) if pd.notna(row['pages']) and isinstance(row['pages'], (int, float)) else None,
    #             nawards=0 if not pd.notna(row['awards']) else len(eval(row['awards'])) if isinstance(eval(row['awards']), list) else 0,
    #             avg_vote=clean_float(row['rating']),
    #             price=clean_float(row['price']),
    #             author=row['author'] if pd.notna(row['author']) else '',
    #             genres=", ".join(eval(row['new_genres'])) if pd.notna(row['new_genres']) else ''
    #         ) for _, row in books_df.iterrows()
    #     ]
    #     # db.session.add_all(books)

    #     # Add ratings
    #     ratings = [
    #         RatingModel(
    #             user_id=row['userId'],
    #             book_id=row['bookId'],
    #             rating=row['rating']
    #         ) for _, row in ratings_df.iterrows()
    #     ]
    #     # db.session.add_all(ratings)

    #     # Add visualizations
    #     visualizations = [
    #         VisualizationModel(
    #             user_id=row['userId'],
    #             book_id=row['bookId'],
    #             reading_date=pd.to_datetime(row['reading_date']).date() if pd.notna(row['reading_date']) else None  # Convert date
    #         ) for _, row in visualizations_df.iterrows()
    #     ]
    #     # db.session.add_all(visualizations)

        # Commit changes to the database
        db.session.commit()

        print("Data imported successfully!")

# Execute data import
import_data()
