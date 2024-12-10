import pandas as pd
from datetime import datetime, timedelta
import random
import os

# Percorso del file di input (ratings.csv nella cartella data)
input_path = os.path.join("..", "Api", "data", "ratings.csv")

# Percorso del file di output aggiornato
output_path = os.path.join("..", "Api", "data", "ratings_updated.csv")

# Leggi il file CSV
df = pd.read_csv(input_path)

# Aggiungi una colonna 'ratingdate' con date casuali (negli ultimi 30 giorni)
today = datetime.now()
df['ratingdate'] = [today - timedelta(days=random.randint(0, 30)) for _ in range(len(df))]

# Formatta le date in formato 'YYYY-MM-DD'
df['ratingdate'] = df['ratingdate'].dt.strftime('%Y-%m-%d')

# Salva il file aggiornato
df.to_csv(output_path, index=False)

print(f"Colonna 'ratingdate' aggiunta e file salvato in: {output_path}")
