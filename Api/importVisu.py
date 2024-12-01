import pandas as pd
from api import app, db
from api import VisualizationModel  # Assurez-vous que VisualizationModel est bien défini dans votre modèle
from datetime import datetime

# Fonction pour afficher un aperçu des premières lignes du fichier CSV
def display_sample_rows(file_path, num_rows=10):
    """Afficher un aperçu des premières lignes du fichier CSV."""
    df = pd.read_csv(file_path, nrows=num_rows)
    print(df.head(num_rows))  # Afficher les premières lignes du DataFrame

# Fonction pour nettoyer et valider l'ID utilisateur
def clean_userid(userid_str):
    """Nettoyer et valider l'ID utilisateur."""
    return userid_str.strip() if isinstance(userid_str, str) else None

# Fonction pour nettoyer et valider l'ID du livre
def clean_bookid(bookid_str):
    """Nettoyer et valider l'ID du livre."""
    return bookid_str.strip() if isinstance(bookid_str, str) else None

# Fonction pour nettoyer et valider la date de lecture (format dd/mm/yyyy)
def clean_reading_date(reading_date_str):
    """Nettoyer et convertir la date de lecture au format yyyy-mm-dd."""
    if not isinstance(reading_date_str, str) or reading_date_str.strip() == "":
        print(f"Date vide ou invalide : {reading_date_str}")
        return None
    try:
        # Conversion en objet datetime.date
        reading_date = datetime.strptime(reading_date_str.strip(), "%Y-%m-%d").date()
        return reading_date
    except ValueError:
        print(f"Erreur de conversion pour la date : {reading_date_str}. Ignorée.")
        return None

def import_visualizations():
    # Chemin du fichier CSV contenant les données des visualisations
    file_path = './data/visualization.csv'

    # Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(file_path)

    # Afficher un aperçu des premières lignes pour vérifier les données
    print("Aperçu des premières lignes du fichier CSV:")
    display_sample_rows(file_path)

    # Liste pour stocker les objets VisualizationModel
    visualizations = []

    with app.app_context():
        for _, row in df.iterrows():
            # Nettoyer et valider les champs
            user_id = row['userId']
            book_id = clean_bookid(row['bookId'])
            # reading_date = row['reading_date']  # Assurez-vous que 'readingDate' existe dans le CSV
            reading_date = clean_reading_date(row['reading_date'])  # Assurez-vous que 'readingDate' existe dans le CSV

            print(user_id, book_id, reading_date)
            if user_id and book_id and reading_date is not None:
                # Créer l'objet VisualizationModel
                visualization_obj = VisualizationModel(
                    user_id=user_id,
                    book_id=book_id,
                    reading_date=reading_date
                )
                visualizations.append(visualization_obj)

        # Ajouter les visualisations dans la base de données
        db.session.add_all(visualizations)
        db.session.commit()

    print(f"{len(visualizations)} visualisations importées avec succès !")

# Exemple d'utilisation :
file_path = './data/visualization.csv'

# Importer les visualisations dans la base de données
import_visualizations()
