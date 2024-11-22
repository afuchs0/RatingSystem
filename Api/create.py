from api import app, db  # Assurez-vous que db est correctement importé

# Créer les tables dans la base de données
with app.app_context():
    db.create_all()
