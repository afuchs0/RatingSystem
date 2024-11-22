import pandas as pd
from api import app, db
from api import RatingModel  # Assurez-vous que RatingModel est bien défini dans votre modèle

# Afficher un aperçu des premières lignes du fichier CSV
def display_sample_rows(file_path, num_rows=10):
    """Afficher un aperçu des premières lignes du fichier CSV."""
    # Charger le fichier CSV en DataFrame
    df = pd.read_csv(file_path, nrows=num_rows)
    print(df.head(num_rows))  # Afficher les premières lignes du DataFrame


def clean_userid(userid_str):
    """Nettoyer et valider l'ID utilisateur."""
    return userid_str.strip() if isinstance(userid_str, str) else None


def clean_bookid(bookid_str):
    """Nettoyer et valider l'ID du livre."""
    return bookid_str.strip() if isinstance(bookid_str, str) else None


def clean_rating(rating_str):
    """Nettoyer et valider la notation."""
    try:
        rating = int(rating_str)
        if 1 <= rating <= 5:
            return rating
        else:
            print(f"Rating invalide (hors plage) : {rating_str}. Ignoré.")
            return None
    except ValueError:
        print(f"Erreur de conversion pour le rating : {rating_str}. Ignoré.")
        return None


def import_ratings():
    # Chemin du fichier CSV contenant les données des notations
    file_path = '/mnt/c/Users/leoba/Documents/CoursesProject/DigitalL/RatingSystem/Api/data/ratings.csv'

    # Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(file_path)

    # Afficher un aperçu des premières lignes pour vérifier les données
    print("Aperçu des premières lignes du fichier CSV:")
    # display_sample_rows(file_path)

    # Liste pour stocker les objets RatingModel
    ratings = []

    with app.app_context():
        for _, row in df.iterrows():
            # Nettoyer et valider les champs
            # user_id = clean_userid(row['userId'])
            user_id = row['userId']
            book_id = clean_bookid(row['bookId'])
            rating = clean_rating(row['rating'])
            print(user_id, book_id, rating)
            if user_id and book_id and rating is not None:
                # Créer l'objet RatingModel
                rating_obj = RatingModel(
                    user_id=user_id,
                    book_id=book_id,
                    rating=rating
                )
                ratings.append(rating_obj)

        # Ajouter les notations dans la base de données
        db.session.add_all(ratings)
        db.session.commit()

    print(f"{len(ratings)} notations importées avec succès !")


# Exemple d'utilisation :
file_path = '/mnt/c/Users/leoba/Documents/CoursesProject/DigitalL/RatingSystem/Api/data/ratings.csv'

# Importer les notations dans la base de données
import_ratings()
