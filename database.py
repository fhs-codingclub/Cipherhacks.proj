import sqlite3
import os


#Make sure to delete the database and run this file again if you want to add more tables
#If your getting a problem that is a good debug choice (IT SUCKS AHHHHHHH)
print(f"Current working directory: {os.getcwd()}")
def create_metadata_db():
    conn = sqlite3.connect('metadata.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS makes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS models (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make_id INTEGER,
            name TEXT NOT NULL,
            FOREIGN KEY (make_id) REFERENCES makes(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS software (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    # Add sample data for makes
    makes = ["Canon", "Nikon", "Sony", "Panasonic", "Fujifilm", "Olympus", "Leica", "Sigma", "Pentax", "Blackmagic"]
    cursor.executemany("INSERT INTO makes (name) VALUES (?)", [(make,) for make in makes])

    # Get all make IDs
    cursor.execute("SELECT id FROM makes")
    make_ids = [row[0] for row in cursor.fetchall()]

    # Starting at [0] at Canon and [10] at Blackmagic more models can be added here to increase randomness
    models = [
        (make_ids[0], "EOS 5D Mark IV"),
        (make_ids[1], "D810"),
        (make_ids[2], "A7R IV"),
        (make_ids[3], "Lumix GH5"),
        (make_ids[4], "X-T4"),
        (make_ids[5], "OM-1"),
        (make_ids[6], "M10-R"),
        (make_ids[7], "35mm f/1.4 DG DN"),
        (make_ids[8], "K-1"),
        (make_ids[9], "Cinema Camera")
    ]
    
    cursor.executemany("INSERT INTO models (make_id, name) VALUES (?, ?)", models)
    
    softwares = [
    "Adobe Photoshop", "Adobe Lightroom", "GIMP", "Paint.NET",
    "Capture One", "Affinity Photo", "Darktable", "DxO PhotoLab",
    "Corel PaintShop Pro", "Snapseed", "Pixelmator", "Luminar",
    "Microsoft Paint", "Apple Photos", "Google Photos", "VSCO",
    "Fotor", "ON1 Photo RAW", "PhotoScape", "AfterShot Pro"
]

    cursor.executemany("INSERT INTO software (name) VALUES (?)", [(s,) for s in softwares])


    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Creating metadata database...")
    create_metadata_db()
    print("Metadata database created successfully.")