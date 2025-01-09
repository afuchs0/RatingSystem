import torch
import pandas as pd
import numpy as np
from collections import Counter
import pandas as pd
from datetime import datetime
import torch
import torch.nn as nn
import torch.optim as optim
import os
import torch.nn.functional as F
import pickle

def load_data():
    with open('./RecSystem/data/PICKLE/df_book.pkl', 'rb') as file:
        df_book = pickle.load(file)
    with open("./RecSystem/data/PICKLE/df_user.pkl", "rb") as file:
        df_users = pickle.load(file)
    with open("./RecSystem/data/PICKLE/df_visualization.pkl", "rb") as file:
        df_visualizations = pickle.load(file)
    with open("./RecSystem/data/PICKLE/df_ratings.pkl","rb") as file:
        df_ratings = pickle.load(file)

    return df_book, df_ratings, df_visualizations, df_users

class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        """
        Inizializza la rete neurale DQN.
        :param input_dim: Dimensione dell'input (stato codificato).
        :param output_dim: Numero di azioni (dimensione dello spazio delle azioni).
        """
        super(DQN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, output_dim)
            
        )


    def forward(self, x):
        """
        Passa i dati attraverso la rete.
        :param x: Input (batch di stati).
        :return: Valutazione Q per ogni azione.
        """
        return self.network(x)

class DQNAgent:
    def __init__(self, input_dim, output_dim, lr=1e-5, gamma=0.99, target_update=200, model_path="./RecSystem/DQN/dqn_model_v6.pth"):
        """
        Inizializza l'agente DQN.
        :param input_dim: Dimensione dell'input (stato codificato).
        :param output_dim: Numero di azioni.
        :param lr: Tasso di apprendimento per l'ottimizzatore.
        :param gamma: Fattore di sconto per il calcolo del valore futuro.
        :param target_update: Frequenza con cui aggiornare la rete target.
        :param model_path: Percorso per salvare/caricare il modello.
        """

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Utilizzo del dispositivo: {self.device}")
        self.policy_net = DQN(input_dim, output_dim).to(self.device)
        self.target_net = DQN(input_dim, output_dim).to(self.device)

        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()

        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=lr)
        self.loss_fn = nn.MSELoss()
        self.gamma = gamma
        self.target_update = target_update
        self.model_path = model_path
        self.steps_done = 0
        self.losses = []  # Per monitorare la perdita

    def select_action(self, state, epsilon=0.1):
        """
        Seleziona un'azione usando softmax, con esplorazione controllata.
        :param state: Stato corrente (torch.Tensor).
        :param epsilon: Probabilità di esplorare (selezionare un'azione casuale).
        :return: Indice dell'azione selezionata.
        """
        state = state.to(self.device).unsqueeze(0)  # Aggiunge una dimensione batch
        with torch.no_grad():
            q_values = self.policy_net(state)  # Calcola i valori Q per tutte le azioni

        # Esplorazione: seleziona casualmente un'azione con probabilità epsilon
        if torch.rand(1).item() < epsilon:
            action = torch.randint(0, self.policy_net.network[-1].out_features, (1,)).item()
            return action, 0  # Restituisce azione e flag di esplorazione

        # Sfruttamento: usa softmax per determinare la probabilità di ciascuna azione
        q_values = q_values.squeeze(0)  # Rimuove la dimensione del batch
        probs = F.softmax(q_values / 1.0, dim=0)  # Temperatura=1 per softmax
        action = torch.multinomial(probs, 1).item()  # Campiona l'azione in base alla probabilità

        return action, 1  # Restituisce azione e flag di sfruttamento
    
    def optimize(self, memory, batch_size):
        """
        Ottimizza la rete basandosi sull'esperienza raccolta.
        :param memory: Replay buffer contenente esperienze (state, action, reward, next_state, done).
        :param batch_size: Dimensione del batch per l'apprendimento.
        """
        if len(memory) < batch_size:
            return

        # Campiona esperienze casuali dal buffer
        batch = memory.sample_batch(batch_size)
        state, action, reward, next_state, done, indices,weights = batch
        # Converti gli stati e gli stati successivi in tensori
        state = torch.stack([torch.tensor(s, dtype=torch.float32) for s in state]).to(self.device)
        next_state = torch.stack([torch.tensor(ns, dtype=torch.float32) for ns in next_state]).to(self.device)

        action = torch.tensor(action, dtype=torch.long, device=self.device).unsqueeze(1)  # Azioni devono essere 2D
        reward = torch.tensor(reward, dtype=torch.float32, device=self.device).unsqueeze(1)
        
        done = torch.tensor(done, dtype=torch.float32, device=self.device).unsqueeze(1)

        # Calcola Q(s, a) usando la policy network
        q_values = self.policy_net(state).gather(1, action)

        # Calcola Q_target
        with torch.no_grad():
            next_q_values = self.target_net(next_state).max(1)[0].unsqueeze(1)
            q_target = reward + (1 - done) * self.gamma * next_q_values

        # Calcola la perdita
        loss = self.loss_fn(q_values, q_target)
        self.losses.append(loss.item())
        # Ottimizza la rete
        self.optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy_net.parameters(), max_norm=10)
        self.optimizer.step()

        # Aggiorna la rete target se necessario
        self.steps_done += 1
        if self.steps_done % self.target_update == 0:
            self.target_net.load_state_dict(self.policy_net.state_dict())

    def save_model(self):
        """
        Salva i pesi del modello su file.
        """
        torch.save(self.policy_net.state_dict(), self.model_path)

    def load_model(self):
        """
        Carica i pesi del modello da file.
        """
        if os.path.exists(self.model_path):
            self.policy_net.load_state_dict(torch.load(self.model_path, map_location=self.device))  # Assicurati che venga caricato sulla GPU
            self.target_net.load_state_dict(self.policy_net.state_dict())
        else:
            print("Nessun modello salvato trovato.")


class Environment:
    def __init__(self, users_df, books_df,visualization_df,ratings_df,max_steps=10, patience=3):
        """
        Inizializza l'ambiente.
        :param users_df: DataFrame degli utenti.
        :param books_df: DataFrame dei libri.
        """
        self.users_df = users_df
        self.books_df = books_df
        self.visualization_df = visualization_df
        self.ratings_df = ratings_df
        self.state = None
        self.current_user = None
        self.max_steps = max_steps
        self.patience = patience
        self.current_step = 0
        self.no_feedback_steps = 0
        self.recommendation_counts = {book_id: 0 for book_id in self.books_df['bookId']}

    def user_recom(self,user_id):
        u = {}
        user = self.users_df[self.users_df["id"] == user_id].iloc[0]
        u["age"] = user["age"]
        u["id"] = user["id"]
        u["generi_preferiti"] = user["generi_preferiti"]
        self.current_user = u
        self.state = self.caluclate_state()
        
        
        return self.encode_state()

    def get_reward(self,given_valuation,book_id,genre_recomendation):
        reward = 0
        if genre_recomendation == 2:
            reward += 80
        if genre_recomendation == 1:
            reward += 40
        if genre_recomendation == 0:
            reward += -10
        if(given_valuation == 5):
            reward += 5
        if(given_valuation == 4):
            reward += 3
        if(given_valuation == 3):
            reward += 1
        if(given_valuation==2):
            reward += -3
        if(given_valuation == 1):
            reward += -5
         # Exploration bonus
        count = self.recommendation_counts.get(book_id, 0)
        exploration_bonus = 1 / (np.sqrt(count + 1))  # Bonus decrescente con il numero di raccomandazioni
        reward += exploration_bonus  # Somma il bonus alla ricompensa
        
        return reward
    def caluclate_state(self):
    
        #AGE CALCULATION
        
        age = int(self.current_user['age'])
        #age = self.current_user['age']
        if age<25:
            age = "young"
        elif age>= 25 and age <=55:
            age = "adult"
        else:
            age = "old"
        #RECENT GENRE CALCULATION
        recent_visualizzazioni = (
        self.visualization_df[self.visualization_df["userId"] == self.current_user["id"]]
        .sort_values(by='reading_date', ascending=False)
        .head(5)
    )
        recent_books = recent_visualizzazioni['bookId'].tolist()
        generi_count = Counter()
        for book_id in recent_books:
        # Trova il libro nel DataFrame dei libri
            book_info = self.books_df[self.books_df['bookId'] == book_id].iloc[0]
            # Supponiamo che i generi siano in una lista nella colonna 'new_genres'
            for genere in book_info['new_genres']:
                generi_count[genere] += 1

        if generi_count:
        # Ottieni il conteggio massimo
            max_count = max(generi_count.values())
        # Ottieni il primo genere con il conteggio massimo
            recent_genre = next(genere for genere, count in generi_count.items() if count == max_count)
        else:
            recent_genre = None  # Nessun libro visualizzato di recente

        avg_rating_user = self.ratings_df.loc[self.ratings_df['userId'] == self.current_user["id"], 'rating'].mean()
        if avg_rating_user<=2:
            severity = "high"
        elif avg_rating_user>2 and avg_rating_user<= 3.5:
            severity = "medium"
        else:
            severity = "low"

        # Definisci lo stato iniziale basato sull'utente selezionato.
        state = {
            "age": age,  # young,adult,old
            "severity": severity,  # low,medium,high
            "preferred_genres": self.current_user["generi_preferiti"],  # Lista di generi separati da virgole
            #"recent_genre": recent_genre
        }
        return state

    def reset(self):
        """
        Resetta l'ambiente per un nuovo episodio.
        :return: Stato iniziale.
        """
        # Seleziona un utente casuale dal DataFrame.
        self.current_step = 0
        self.no_feedback_steps = 0
        self.current_user = self.users_df.sample().iloc[0]
        self.state = self.caluclate_state()
        #print(self.state)
        return self.encode_state()

    def aggiorna_dati(self, book_id, rating):
    # Aggiungi una nuova visualizzazione per l'utente e il libro con la data corrente
        self.visualization_df = pd.concat([
        self.visualization_df,
        pd.DataFrame({"userId": [self.current_user["id"]], "bookId": [book_id], "reading_date": [datetime.now().strftime("%Y-%m-%d")]})
    ], ignore_index=True)

        # Aggiungi o aggiorna la valutazione dell'utente per il libro
        if ((self.ratings_df["userId"] == self.current_user["id"]) & (self.ratings_df["bookId"] == book_id)).any():
            # Aggiorna la valutazione esistente
            self.ratings_df.loc[(self.ratings_df["userId"] == self.current_user["id"]) & (self.ratings_df["bookId"] == book_id), "rating"] = rating
        else:
            # Aggiungi una nuova valutazione
            self.ratings_df = pd.concat([
                self.ratings_df,
                pd.DataFrame({"userId": [self.current_user["id"]], "bookId": [book_id], "rating": [rating]})
            ], ignore_index=True)

        


    def step(self, action):
        """
        Simula il passo successivo nel sistema dato un'azione.
        :param action: Azione intrapresa (indice del libro nel DataFrame).
        :return: Nuovo stato, ricompensa, flag done.
        """
        # Recupera il libro consigliato dall'azione (indice del DataFrame).
        recommended_book = self.books_df.iloc[action]
        book_id = recommended_book["bookId"]
        self.recommendation_counts[book_id] += 1
        # Simula il feedback dell'utente.
        #if not self.visualization_df[self.visualization_df["bookId"] == book_id].empty:
        self.current_step += 1
        valuation,genre_recomandation = self.simulate_user_feedback(book_id)
        reward = self.get_reward(valuation,book_id,genre_recomandation)
        self.aggiorna_dati(book_id,valuation)
        #else:
            #print("entrato")
            #reward = -5

        if reward < 1:  # Soglia per feedback negativo
            self.no_feedback_steps += 1
        else:
            self.no_feedback_steps = 0
        # Aggiorna lo stato (es. il genere recente diventa il genere del libro consigliato).
        self.state = self.caluclate_state()

        # Determina se l'episodio è terminato (può essere basato su un criterio come il numero di raccomandazioni).
        done = (
            self.current_step >= self.max_steps or 
            self.no_feedback_steps >= self.patience
        )
        #print(self.state)
        return self.encode_state(), reward, done
    
    def calculate_severity_deficit(severity,avg_val):
        if avg_val> 3:
            return 0.3
        else:
            return -0.5
    def simulate_user_feedback(self, bookid):
        """
        Simula il voto che un utente darebbe al libro consigliato.
        :param book: Riga del DataFrame (serie con informazioni sul libro).
        :return: Ricompensa calcolata in base al voto simulato.
        """
        user = self.current_user
        book = self.books_df.loc[self.books_df['bookId'] == bookid]
        #print(bookid)
        base_rating = book['rating'].iloc[0]
        user_genres = user['generi_preferiti']
        book_genres = book['new_genres'].iloc[0]
        #print(book_genres,base_rating)
        avg_rating_user = self.ratings_df.loc[self.ratings_df['userId'] == self.current_user["id"], 'rating'].mean()
        user_severity = self.calculate_severity_deficit(avg_rating_user)
        genre_recomendation = 0
        if len(set(user_genres).intersection(book_genres))==2:
            #print("\n\n\n sono entrato qui2 \n\n\n")
            rating = np.random.normal(loc=base_rating + 0.75 + user_severity, scale=0.1)
            genre_recomendation = 2
        elif len(set(user_genres).intersection(book_genres))==1:
            rating = np.random.normal(loc=base_rating  + user_severity+ 0.5, scale=0.3)
            genre_recomendation = 1
            #print("\n\n\n sono entrato qui\n\n\n")
        else:
            rating = np.random.normal(loc=base_rating - 0.3 + user_severity, scale=0.5)
        #print(rating)
        return int(min(max(round(rating), 1), 5)),genre_recomendation

    def encode_state(self):
        """
        Converte lo stato in una rappresentazione numerica (es. one-hot encoding).
        :return: Stato codificato.
        """
        #age_mapping = {"young": 0, "adult": 1, "old": 2}
        severity_mapping = {"low": 0, "medium": 1, "high": 2}

        # One-hot encoding per età e severità.
        #age_encoded = np.eye(3)[age_mapping[self.state["age"]]]
        severity_encoded = np.eye(3)[severity_mapping[self.state["severity"]]]

        all_genres = set(genre for genres in self.books_df["new_genres"] for genre in genres)
        all_genres = sorted(all_genres)  # Ordine deterministico
        genre_to_index = {genre: idx for idx, genre in enumerate(all_genres)}
        # Codifica i generi come un array binario
        fav_genre_encoded = np.zeros(len(all_genres))
        for genre in self.state["preferred_genres"]:
            genre_index = genre_to_index[genre]
            fav_genre_encoded[genre_index] = 1

        # Codifica il genere recente.
        #recent_genre_encoded = np.zeros(len(all_genres))
        #if self.state["recent_genre"] in all_genres:
        #    genre_index = np.where(all_genres == self.state["recent_genre"])[0][0]
        #    recent_genre_encoded[genre_index] = 1

        # Concatenazione finale dello stato codificato.
        #return np.concatenate([age_encoded, severity_encoded, genre_encoded, recent_genre_encoded])
        #return np.concatenate([age_encoded, severity_encoded, fav_genre_encoded])
        return np.concatenate([ fav_genre_encoded])



def recommend_book(agent, environment, user_id, df_books,device=torch.device("cpu")):
    """
    Raccomanda un libro dato un utente specifico.
    :param agent: L'agente DQN addestrato.
    :param environment: L'ambiente che gestisce utenti e libri.
    :param user_id: ID dell'utente per cui fare la raccomandazione.
    :param device: Dispositivo (CPU).
    :return: Dettagli del libro raccomandato.
    """
    # Imposta il dispositivo su CPU
    agent.policy_net.to(device)

    # Reset dell'ambiente per l'utente specifico
    state = environment.user_recom(user_id=user_id)


    state = torch.tensor(state, dtype=torch.float32, device='cpu')  # Usa il device del modello
    #print(state)
     # Prevedi i valori Q per tutte le azioni (libri)
    with torch.no_grad():
        q_values = agent.policy_net(state).squeeze(0)  # Rimuovi dimensione batch
    
    # Trova gli indici delle `num_books` migliori azioni
    top_actions = torch.topk(q_values,len(df_books)).indices.tolist()

    # Ottieni i dettagli dei libri corrispondenti
    recommended_books = []
    for action in top_actions:
        book_info = environment.books_df.iloc[action]  # Ottieni info libro da df
        recommended_books.append(book_info["bookId"])
    
    return recommended_books

def dqn(user_id):
    # Carica i dati e inizializza l'ambiente
    df_books, df_ratings, df_visualization, df_users = load_data()
    env = Environment(df_users, df_books, df_visualization, df_ratings)

    # Parametri del modello
    input_dim = 50  # Dimensione dello stato
    output_dim = len(df_books)  # Numero totale di libri (azioni possibili)

    # Inizializza l'agente DQN
    device = torch.device("cpu")
    agent = DQNAgent(input_dim, output_dim)
    agent.load_model()  # Carica il modello addestrato
    recommended_books = recommend_book(agent, env, user_id,df_books, device=device)
    #print(recommended_books)
    return recommended_books









