import sqlite3

# Connetti al database
conn = sqlite3.connect('library.db')

# Crea un cursore
cur = conn.cursor()

# Esegui la query per contare il numero di libri nella tabella 'books'
cur.execute("SELECT COUNT(*) FROM books;")

# Recupera il risultato
row = cur.fetchone()  # Con 'fetchone' ottieni un solo risultato (un singolo valore)

# Stampa il risultato
if row:
    print(f"Numero di libri nella tabella 'books': {row[0]}")  # row[0] contiene il risultato del COUNT(*)
else:
    print("La tabella 'books' è vuota.")

# Chiudi la connessione
conn.close()
