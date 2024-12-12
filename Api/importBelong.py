import pandas as pd
from api import app, db
from api import BelongModel  # Assurez-vous que belongModel est bien défini dans votre modèle
from datetime import datetime

# Fonction pour afficher un aperçu des premières lignes du fichier CSV
def display_sample_rows(file_path, num_rows=10):
    """Afficher un aperçu des premières lignes du fichier CSV."""
    df = pd.read_csv(file_path, nrows=num_rows)
    print(df.head(num_rows))  # Afficher les premières lignes du DataFrame

# Fonction pour nettoyer et valider l'ID utilisateur
def clean_genreid(genreId_str):
    """Nettoyer et valider l'ID utilisateur."""
    return genreId_str.strip() if isinstance(genreId_str, str) else None

# Fonction pour nettoyer et valider l'ID du livre
def clean_bookid(bookid_str):
    """Nettoyer et valider l'ID du livre."""
    return bookid_str.strip() if isinstance(bookid_str, str) else None

# Fonction pour nettoyer et valider la date de lecture (format dd/mm/yyyy)
# def clean_belong_date(belong_date_str):
#     """Nettoyer et convertir la date de lecture au format yyyy-mm-dd."""
#     if not isinstance(belong_date_str, str) or belong_date_str.strip() == "":
#         print(f"Date vide ou invalide : {belong_date_str}")
#         return None
#     try:
#         # Conversion en objet datetime.date
#         belong_date = datetime.strptime(belong_date_str.strip(), "%Y-%m-%d").date()
#         return belong_date
#     except ValueError:
#         print(f"Erreur de conversion pour la date : {belong_date_str}. Ignorée.")
#         return None

def import_belong():
    # Chemin du fichier CSV contenant les données 
    file_path = './data/belong.csv'

    # Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(file_path)

    # Afficher un aperçu des premières lignes pour vérifier les données
    print("Aperçu des premières lignes du fichier CSV:")
    display_sample_rows(file_path)

    # Liste pour stocker les objets belongModel
    belongs = []

    with app.app_context():
        for _, row in df.iterrows():
            # Nettoyer et valider les champs
            genre_id = row['genreId']
            book_id = clean_bookid(row['bookId'])
            # belong_date = row['belong_date']  # Assurez-vous que 'belongDate' existe dans le CSV
            belong_date = datetime.now()  # Assurez-vous que 'belongDate' existe dans le CSV

            print(genre_id, book_id, belong_date)
            if genre_id and book_id and belong_date is not None:
                # Créer l'objet belongModel
                belong_obj = BelongModel(
                    genre_id=genre_id,
                    book_id=book_id,
                    belong_date=belong_date
                )
                belongs.append(belong_obj)

        # Ajouter les visualisations dans la base de données
        db.session.add_all(belongs)
        db.session.commit()

    print(f"{len(belongs)} belong importées avec succès !")

# Exemple d'utilisation :
file_path = './data/belong.csv'

# Importer les visualisations dans la base de données
import_belong()
