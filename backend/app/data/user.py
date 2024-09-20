from models.user import User

lista_utenti = [
    User(1, "Alice", {}, ["Fantascienza"], 25),
    User(2, "Marco", {}, ["Fantasy"], 30),
    User(3, "Giulia", {}, ["Romance"], 28),
    User(4, "Luca", {}, ["Horror"], 22),
    User(5, "Sara", {}, ["Giallo"], 35),
    User(6, "Tommaso", {}, ["Avventura"], 40)
]
lista_utenti[0].add_val(101, 5)  # Alice vota il libro con ID 101 con 5
lista_utenti[1].add_val(102, 4)  # Marco vota il libro con ID 102 con 4
lista_utenti[2].add_val(103, 3)  # Giulia vota il libro con ID 103 con 3

# Aggiungere generi preferiti per alcuni utenti
lista_utenti[3].add_pref("Thriller")  # Luca aggiunge il genere Thriller
lista_utenti[4].add_pref("Storico")   # Sara aggiunge il genere Storico