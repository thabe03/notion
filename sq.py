import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Define the table schema
table_schema = '''
CREATE TABLE Garage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    TitleInput TEXT,
    Ville TEXT,
    CodePostal TEXT,
    Region TEXT,
    SelectInput TEXT,
    Description TEXT,
    ARefaire TEXT,
    Demande INTEGER,
    Prenom TEXT,
    Nom TEXT,
    Courriel TEXT,
    Telephone TEXT,
    RapportInclusion INTEGER,
    CertificatInclusion INTEGER,
    FraisCessionInclusion INTEGER,
    GarageCheckboxInput INTEGER,
    AnneeConstruction INTEGER,
    Economie INTEGER,
    NumeroLotCadastre INTEGER,
    DateNotaire TEXT,
    Type TEXT,
    Zonage TEXT,
    Terrain INTEGER,
    LargeurBatiment INTEGER,
    Chauffage TEXT,
    RenovationRecente TEXT,
    Chambres INTEGER
);
'''

# Create the table
cursor.execute(table_schema)
conn.commit()

# Close the connection
conn.close()
