import os
import sqlite3


def db_exists(db_name):
    db_exists = os.path.isfile("dbs/" + db_name + ".db")
    return db_exists


def create_template_database():
    print("Create template database...")

    con = sqlite3.connect("dbs/database.db")
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS song(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, song_title TEXT DEFAULT \"Untitled\" NOT NULL);"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS alternate_title(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, song_id INTEGER NOT NULL, alternate_title TEXT NOT NULL, FOREIGN KEY(song_id) REFERENCES song(id));"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS artist(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, artist_name TEXT NOT NULL, is_active INTEGER DEFAULT 1);"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS artist_alias(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, artist_id INTEGER NOT NULL, alias TEXT NOT NULL, FOREIGN KEY(artist_id) REFERENCES artist(id));"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS music_group(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, group_name TEXT NOT NULL, is_active INTEGER DEFAULT 1);"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS group_alias(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, group_id INTEGER NOT NULL, alias TEXT NOT NULL, FOREIGN KEY(group_id) REFERENCES music_group(id));"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS group_artists(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, group_id INTEGER NOT NULL, artist_id INTEGER NOT NULL, FOREIGN KEY(group_id) REFERENCES music_group(id), FOREIGN KEY(artist_id) REFERENCES artist(id));"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS song_artists(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, song_id INTEGER NOT NULL, group_id INTEGER, artist_id INTEGER, FOREIGN KEY(song_id) REFERENCES song(id), FOREIGN KEY(group_id) REFERENCES music_group(id), FOREIGN KEY(artist_id) REFERENCES artist(id));"
    )

    con.commit()
    con.close()

    print("Finished creating database!")