import pandas as pd
from api import app, db
from api import BookModel
from charset_normalizer import from_path


# def display_sample_rows(file_path, num_rows=10):
#     """Afficher un aperçu des premières lignes du fichier CSV."""
#     # Charger le fichier CSV en DataFrame
#     df = pd.read_csv(file_path, nrows=num_rows)
#     print(df.head(num_rows))

file_path = '/mnt/c/Users/leoba/Documents/CoursesProject/DigitalL/RatingSystem/Api/data/books_def1.csv'

def detect_file_encoding(file_path):
    """Détecter l'encodage d'un fichier."""
    result = from_path(file_path).best()
    return result.encoding

def preview_csv(file_path, encoding, num_lines=10):
    """Afficher les premières lignes du fichier."""
    print(f"--- Aperçu des {num_lines} premières lignes ---")
    with open(file_path, 'r', encoding=encoding) as f:
        for i in range(num_lines):
            print(f"Ligne {i + 1}: {f.readline().strip()}")

def clean_price(price_str):
    """Nettoyer et convertir la chaîne de caractères en un prix valide."""
    try:
        # Supprimer les séparateurs de milliers et remplacer le séparateur décimal si nécessaire
        cleaned_price = price_str.replace('.', '', price_str.count('.') - 1).replace(',', '.')  # Remplacer les points, sauf le dernier
        return float(cleaned_price)
    except ValueError:
        print(f"Erreur de conversion pour le prix : {price_str}")
        return None

def import_books():
    # Chemin du fichier CSV contenant les données des livres
    file_path = '/mnt/c/Users/leoba/Documents/CoursesProject/DigitalL/RatingSystem/Api/data/books_def1.csv'
    encoding = detect_file_encoding(file_path)
    print(f"Encodage détecté : {encoding}")

    # # Aperçu des premières lignes
    # preview_csv(file_path, encoding)

    # Lire les données
    try:
        df = pd.read_csv(
            file_path,
            encoding=encoding,
            sep=None,  # Détecter automatiquement le séparateur
            engine='python',
            on_bad_lines='skip'  # Ignore les lignes problématiques
        )
    except Exception as e:
        print(f"Erreur lors de la lecture du CSV : {e}")
        return

    # Liste pour stocker les objets BookModel
    books = []

    with app.app_context():
        for _, row in df.iterrows():
            # Vérifier si le livre existe déjà dans la base de données
            if BookModel.query.get(row['bookId']):
                print(f"Le livre avec l'ID {row['bookId']} existe déjà. Ignoré.")
                continue

            # Créer l'objet BookModel
            book = BookModel(
                id=row['bookId'],
                title=row['title'],
                serie=row['series'] if pd.notna(row['series']) else None,
                desc=row['description'] if pd.notna(row['description']) else None,
                lang=row['language'] if pd.notna(row['language']) else None,
                pages=int(row['pages']) if pd.notna(row['pages']) else None,
                nawards= 0,
                avg_vote=float(row['rating']) if pd.notna(row['rating']) else 0.0,
                price=clean_price(row['price']) if pd.notna(row['price']) else None,
                # price=float(row['price']) if pd.notna(row['price']) else None,
                author=row['author'],
                genres=row['new_genres'] if pd.notna(row['new_genres']) else ""
            )
            books.append(book)

        # Ajouter les livres dans la base de données
        db.session.add_all(books)
        db.session.commit()

    print(f"{len(books)} livres importés avec succès !")


# Exemple d'utilisation :
file_path = '/mnt/c/Users/leoba/Documents/CoursesProject/DigitalL/RatingSystem/Api/data/books_def1.csv'

# Afficher les premières lignes pour vérification
# display_sample_rows(file_path)

# Importer les livres dans la base de données
import_books()
