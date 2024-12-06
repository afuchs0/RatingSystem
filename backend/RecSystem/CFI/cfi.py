import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# 1. Funzione per caricare i dati
def load_data():
    with open('../data/PICKLE/df_book.pkl', 'rb') as file:
        df_book = pickle.load(file)
    with open("../data/PICKLE/df_visualization.pkl", "rb") as file:
        df_visualizations = pickle.load(file)
    with open("../data/PICKLE/df_ratings.pkl", "rb") as file:
        df_ratings = pickle.load(file)
    return df_book, df_ratings, df_visualizations

# 2. Funzione per creare la matrice utente-libro con tutte le combinazioni
def create_item_user_matrix(df_ratings, df_book):
    all_users = df_ratings['userId'].unique()
    all_books = df_book['bookId'].unique()
    
    all_combinations = pd.DataFrame([(user, book) for user in all_users for book in all_books], columns=['userId', 'bookId'])
    
    all_ratings = all_combinations.merge(df_ratings, on=['userId', 'bookId'], how='left')
    
    item_user_matrix = all_ratings.pivot(index='bookId', columns='userId', values='rating')
    return item_user_matrix

# 3. Funzione per calcolare la similarità tra utenti
def calculate_item_similarity(item_user_matrix):
    item_user_matrix_filled = item_user_matrix.fillna(0)
    item_similarity = cosine_similarity(item_user_matrix_filled)
    item_similarity_df = pd.DataFrame(item_similarity, index=item_user_matrix.index, columns=item_user_matrix.index)
    return item_similarity_df

def get_all_item_based_recommendations(user_id, item_user_matrix, item_similarity_df, df_visualizations, df_book):
    # Trova i libri già letti dall'utente
    books_read_by_user = df_visualizations[df_visualizations['userId'] == user_id]['bookId'].unique()
    
    recommendations = {}
    
    for book_id in books_read_by_user:
        # Trova i libri simili, escludendo il libro stesso
        similar_books = item_similarity_df[book_id].sort_values(ascending=False).drop(book_id)
        
        for similar_book, similarity in similar_books.items():
            if similar_book not in books_read_by_user:
                recommendations[similar_book] = recommendations.get(similar_book, 0) + similarity
    
    # Ordina i libri raccomandati per punteggio
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    # Ritorna i titoli dei libri ordinati per similarità
    recommended_books_ids = [book_id for book_id, _ in sorted_recommendations]
    
    # Ottieni i titoli dei libri dal DataFrame df_book
    recommended_books_titles = df_book[df_book['bookId'].isin(recommended_books_ids)]['bookId'].tolist()
    
    return recommended_books_titles

# Funzione principale
def cfi(user_id=None):
    # Carica i dati
    df_book, df_ratings, df_visualizations = load_data()
    
    # Crea la matrice utente-libro
    user_item_matrix = create_item_user_matrix(df_ratings, df_book)
    
    # Calcola la similarità tra gli item
    user_similarity_df = calculate_item_similarity(user_item_matrix)
    
    if user_id is not None:
        # Genera tutte le raccomandazioni per l'utente specificato
        recommendations = get_all_item_based_recommendations(user_id, user_item_matrix, user_similarity_df, df_visualizations, df_book)
        #print(f"Recommended books for user {user_id}: {recommendations}")
    else:
        print("Please provide a valid user_id.")
    
    return recommendations

# Esegui il programma
if __name__ == "__main__":
    final = cfi(12)
    print(final)
