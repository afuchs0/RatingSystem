import pandas as pd
from api import app, db
from api import FavoriteModel  # Assurez-vous que favoriteModel est bien défini dans votre modèle

# Fonction pour afficher un aperçu des premières lignes du fichier CSV
def display_sample_rows(file_path, num_rows=10):
    """Afficher un aperçu des premières lignes du fichier CSV."""
    df = pd.read_csv(file_path, nrows=num_rows)
    print(df.head(num_rows))  # Afficher les premières lignes du DataFrame

# Fonction pour nettoyer et valider l'ID utilisateur
def clean_genreid(genreId_str):
    """Nettoyer et valider l'ID genre."""
    return genreId_str.strip() if isinstance(genreId_str, str) else None

# Fonction pour nettoyer et valider l'ID du livre
def clean_userid(userid_str):
    """Nettoyer et valider l'ID du user."""
    return userid_str.strip() if isinstance(userid_str, str) else None


def import_favorite():
    # Chemin du fichier CSV contenant les données 
    file_path = './data/favorites.csv'

    # Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(file_path)

    # Afficher un aperçu des premières lignes pour vérifier les données
    print("Aperçu des premières lignes du fichier CSV:")
    display_sample_rows(file_path)

    # Liste pour stocker les objets favoriteModel
    favorites = []

    with app.app_context():
        for _, row in df.iterrows():
            # Nettoyer et valider les champs
            genre_id = row['genreId']
            user_id = clean_userid(row['userId'])
            #  = row['']  # Assurez-vous que 'favoriteDate' existe dans le CSV
            
            print(genre_id, user_id)
            if genre_id and user_id   is not None:
                # Créer l'objet favoriteModel
                favorite_obj = FavoriteModel(
                    user_id=user_id,
                    genre_id=genre_id,
                )
                favorites.append(favorite_obj)

        # Ajouter les favorites dans la base de données
        db.session.add_all(favorites)
        db.session.commit()

    print(f"{len(favorites)} favorite importées avec succès !")

# Exemple d'utilisation :
file_path = './data/favorite.csv'

# Importer les favorites dans la base de données
import_favorite()
