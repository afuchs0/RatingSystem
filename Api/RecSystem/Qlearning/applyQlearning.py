import pickle
import pandas as pd
import numpy as np
import random
from collections import Counter
from datetime import datetime
import time


# 1. Funzione per caricare i dati
# def load_data():
#     with open('../data/PICKLE/df_book.pkl', 'rb') as file:
#         df_book = pickle.load(file)
#     with open("../data/PICKLE/df_visualization.pkl", "rb") as file:
#         df_visualizations = pickle.load(file)
#     with open("../data/PICKLE/df_ratings.pkl", "rb") as file:
#         df_ratings = pickle.load(file)
#     with open("../data/PICKLE/df_user.pkl", "rb") as file:
#         df_users = pickle.load(file)
#     return df_book, df_ratings, df_visualizations,df_users

def load_data():
    with open('./RecSystem/data/PICKLE/df_book.pkl', 'rb') as file:
        df_book = pickle.load(file)
    with open("./RecSystem/data/PICKLE/df_user.pkl", "rb") as file:
        df_users = pickle.load(file)
    with open("./RecSystem/data/PICKLE/df_visualization.pkl", "rb") as file:
        df_visualizations = pickle.load(file)
    with open("./RecSystem/data/PICKLE/df_ratings.pkl","rb") as file:
        df_ratings = pickle.load(file)
    
      # Debug: stampa gli ID degli utenti disponibili
    #print("User IDs in df_user:", df_users['id'].tolist())

    return df_book, df_ratings, df_visualizations, df_users


def get_reward(given_valuation):
    if(given_valuation == 5):
        reward = 4
    if(given_valuation == 4):
        reward = 3
    if(given_valuation == 3):
        reward = 1
    if(given_valuation==2):
        reward = -3
    if(given_valuation == 1):
        reward = -5
    return reward

def calculate_severity(avg_val):
    if avg_val> 3:
        return 0.3
    else:
        return -0.5

def simualate_valuation(df_users,df_books,df_valuation,user_id, book_id):
    user = df_users.loc[df_users['id'] == user_id]
    book = df_books.loc[df_books['bookId'] == book_id]

    base_rating = book['rating'].iloc[0] -1

    user_genres = user['generi_preferiti'].iloc[0]
    book_genres = book['new_genres'].iloc[0]
    avg_rating_user = df_valuation.loc[df_valuation['userId'] == user_id, 'rating'].mean()
    user_severity = calculate_severity(avg_rating_user)

    if len(set(user_genres).intersection(book_genres))==2:
        rating = np.random.normal(loc=base_rating + 1.5 + user_severity, scale=0.75)
    elif len(set(user_genres).intersection(book_genres))==1:
        rating = np.random.normal(loc=base_rating + 1 + user_severity, scale=0.75)
    else:
        rating = np.random.normal(loc=base_rating - 1.5 + user_severity, scale=1)

    return int(min(max(round(rating), 1), 5))



def get_book_actions(df_libri):
    available_books = df_libri['bookId'].tolist()
    return available_books


def get_user_state(user_id, df_user, df_visualizzazioni, df_ratings, df_book, num_recent=5):
    # Ottieni dati di base dell'utente (età e generi preferiti)
    # user_info = df_user[df_user['id'] == user_id].iloc[0]
    filtered_user = df_user[df_user['id'] == user_id]
    if filtered_user.empty:
        raise ValueError(f"User with ID {user_id} not found in the dataset.")
    user_info = filtered_user.iloc[0]
    age = user_info['age']
    if age<25:
        age = "young"
    elif age>= 25 and age <=55:
        age = "adult"
    else:
        age = "old"
    generi_preferiti = user_info['generi_preferiti']

    # Ottieni gli ultimi libri visualizzati dall'utente
    recent_visualizzazioni = (
        df_visualizzazioni[df_visualizzazioni['userId'] == user_id]
        .sort_values(by='reading_date', ascending=False)
        .head(num_recent)
    )
    recent_books = recent_visualizzazioni['bookId'].tolist()

 # Conta i generi degli ultimi libri visualizzati
    generi_count = Counter()
    for book_id in recent_books:
        # Trova il libro nel DataFrame dei libri
        book_info = df_book[df_book['bookId'] == book_id].iloc[0]
        # Supponiamo che i generi siano in una lista nella colonna 'new_genres'
        for genere in book_info['new_genres']:
            generi_count[genere] += 1

    # Ottieni il genere più comune, in caso di parità restituisci il primo
    if generi_count:
        # Ottieni il conteggio massimo
        max_count = max(generi_count.values())
        # Ottieni il primo genere con il conteggio massimo
        recent_genre = next(genere for genere, count in generi_count.items() if count == max_count)
    else:
        recent_genre = None  # Nessun libro visualizzato di recente

    avg_rating_user = df_ratings.loc[df_ratings['userId'] == user_id, 'rating'].mean()
    if avg_rating_user<=2:
        severity = "high"
    elif avg_rating_user>2 and avg_rating_user<= 3.5:
        severity = "medium"
    else:
        severity = "low"
    # Costruisci lo stato come dizionario
    user_state = {
        "age": age,
        "generi_preferiti": generi_preferiti,
        "severity":severity,
        "recent_genre":recent_genre
    }

    return user_state
def aggiorna_dati(user_id, book_id, rating, df_visualizzazion, df_ratings):
    # Aggiungi una nuova visualizzazione per l'utente e il libro con la data corrente
    df_visualizzazion = pd.concat([
        df_visualizzazion,
        pd.DataFrame({"userId": [user_id], "bookId": [book_id], "date": [datetime.now()]})
    ], ignore_index=True)

    # Aggiungi o aggiorna la valutazione dell'utente per il libro
    if ((df_ratings["userId"] == user_id) & (df_ratings["bookId"] == book_id)).any():
        # Aggiorna la valutazione esistente
        df_ratings.loc[(df_ratings["userId"] == user_id) & (df_ratings["bookId"] == book_id), "rating"] = rating
    else:
        # Aggiungi una nuova valutazione
        df_ratings = pd.concat([
            df_ratings,
            pd.DataFrame({"userId": [user_id], "bookId": [book_id], "rating": [rating]})
        ], ignore_index=True)

    return df_visualizzazion, df_ratings

def setup():
    Q_table= {}
    df_books,df_ratings,df_visualization,df_users = load_data()
    num_episodes =20000
    alpha = 0.1
    gamma = 0.9
    epsilon = 1
    epsilon_min = 0.1
    epsilon_decay = 0.99
    available_books = get_book_actions(df_books)
    train_Q_learning(num_episodes,alpha,gamma,epsilon,epsilon_min,epsilon_decay,available_books,df_books,df_users,df_visualization,df_ratings,Q_table)


def update_Q(Q_table, state, action, reward, next_state, alpha, gamma,available_books):
    if state not in Q_table:
        Q_table[state] = {a: 0 for a in available_books}

    # Formula di aggiornamento Q-learning
    max_next_Q = max(Q_table.get(next_state, {a: 0 for a in available_books}).values())
    Q_table[state][action] = Q_table[state][action] + alpha * (reward + gamma * max_next_Q - Q_table[state][action])

def epsilon_greedy_policy(Q_table, state, epsilon,available_books):
    if state not in Q_table:
        Q_table[state] = {a: 0 for a in available_books}
    if random.uniform(0, 1) < epsilon:
        return random.choice(available_books)  # Esplora
    else:
        return max(Q_table[state], key=Q_table[state].get)  # Sfrutta

def train_Q_learning(num_episodes, alpha, gamma, epsilon,epsilon_min, epsilon_decay, available_books,df_books, df_utenti, df_visual, df_ratings, Q_table):
    for episode in range(num_episodes):
        start_time = time.time()
        for user_id in df_utenti['id']:
            # Ottieni lo stato iniziale dell'utente

            state = str(get_user_state(user_id, df_utenti, df_visual, df_ratings, df_books))
            # Scegli un'azione (libro) basata sulla politica epsilon-greedy
            action = epsilon_greedy_policy(Q_table, state, epsilon, available_books)

            # Simula la valutazione dell'utente (da migliorare con feedback reale)
            rating = simualate_valuation(df_utenti, df_books, df_ratings, user_id, action)
            reward = get_reward(rating)

            # Aggiorna Q-table
            df_visual, df_ratings = aggiorna_dati(user_id, action, rating, df_visual, df_ratings)
            next_state = str(get_user_state(user_id, df_utenti, df_visual, df_ratings, df_books))
            update_Q(Q_table, state, action, reward, next_state, alpha, gamma, available_books)

        epsilon = max(epsilon_min, epsilon *epsilon_decay)

        # Puoi stampare l'avanzamento per il debug
        if episode % 100 == 0:
            print(time.time()-start_time)
            print(f"Episode {episode} completed.")
        if episode % 1000 == 0 and episode != 0:
            with open("./RecSystem/model/qlearning{episode}.pkl", "wb") as f:
                pickle.dump(Q_table, f)
            #print("Q-table saved successfully.")

    # Salva la Q-table alla fine dell'addestramento
    with open("./RecSystem/model/qlearning.pkl", "wb") as f:
        pickle.dump(Q_table, f)
    #print("Q-table saved successfully.")


def recommend_books(user_id, Q_table, df_utenti, df_visual, df_ratings, available_books):
    # Get the user's current state
    state = str(get_user_state(user_id, df_utenti, df_visual, df_ratings, available_books))
    #print(f"User state: {state}")
    
    if state in Q_table:
        # If the state exists in the Q-table, sort actions by Q-values in descending order
        sorted_actions = sorted(Q_table[state].items(), key=lambda x: x[1], reverse=True)
        # Extract book IDs in order of their Q-values
        recommended_books_ids = [action[0] for action in sorted_actions]
    else:
        # If the state is not in the Q-table, return a randomized list of available books
        #print("State not found in Q-table. Returning randomized book list.")
        recommended_books_ids = list(available_books['bookId'].sample(len(available_books)))
    
    # Map book IDs to their titles
    recommended_books_titles = available_books[available_books['bookId'].isin(recommended_books_ids)]['bookId'].tolist()
    return recommended_books_titles

def qlearning(id_utente):
    #print(f"User ID provided: {id_utente}")
    # Ensure user_id is an integer
    id_utente = int(id_utente)

    # Load necessary data
    df_books, df_ratings, df_visualization, df_users = load_data()
    #print(f"Data Loaded")

    # Load the Q-table
    with open("./RecSystem/model/qlearning.pkl", "rb") as f:
        Q_table = pickle.load(f) 
    #print(f"Qtable loaded")
    #print(f"Number of states in Q-table: {len(Q_table)}")
    
    # Get the recommendations
    final_recommendations = recommend_books(id_utente, Q_table, df_users, df_visualization, df_ratings, df_books)
    #print(f"Printing Final Recommendation: {final_recommendations}")
    return final_recommendations

if __name__ == "__main__":
    # Generate recommendations for a specific user
    recommendations = qlearning(id_utente=2)
    #print(f"Recommended books: {recommendations}")