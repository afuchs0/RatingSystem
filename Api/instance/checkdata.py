from sqlalchemy import create_engine, MetaData

# Connect to the SQLite database
engine = create_engine('sqlite:///library.db')

# Reflect the database metadata
metadata = MetaData()
metadata.reflect(bind=engine)

# Drop all tables
metadata.drop_all(bind=engine)

print("All tables have been dropped from library.db.")
