import numpy as np
import pickle
from .qlearning import get_user_state, load_data

def recommend_books(user_id, Q_table, df_utenti, df_visual, df_ratings, available_books):
    # Get the user's current state
    state = str(get_user_state(user_id, df_utenti, df_visual, df_ratings, available_books))
    print(f"User state: {state}")
    
    if state in Q_table:
        # If the state exists in the Q-table, sort actions by Q-values in descending order
        sorted_actions = sorted(Q_table[state].items(), key=lambda x: x[1], reverse=True)
        # Extract book IDs in order of their Q-values
        recommended_books_ids = [action[0] for action in sorted_actions]
    else:
        # If the state is not in the Q-table, return a randomized list of available books
        print("State not found in Q-table. Returning randomized book list.")
        recommended_books_ids = list(available_books['bookId'].sample(len(available_books)))
    
    # Map book IDs to their titles
    recommended_books_titles = available_books[available_books['bookId'].isin(recommended_books_ids)]['bookId'].tolist()
    return recommended_books_titles

def qlearning(user_id=None):
    # Load necessary data
    df_books, df_ratings, df_visualization, df_users = load_data()
    
    # Load the Q-table
    with open("./RecSystem/model/qlearning.pkl", "rb") as f:
        Q_table = pickle.load(f) 
    
    print(f"Number of states in Q-table: {len(Q_table)}")
    
    # Get the recommendations
    final_recommendations = recommend_books(user_id, Q_table, df_users, df_visualization, df_ratings, df_books)
    return final_recommendations

if __name__ == "__main__":
    # Generate recommendations for a specific user
    recommendations = qlearning(user_id=2)
    print(f"Recommended books: {recommendations}")