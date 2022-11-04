import sqlite3
import database_starter

default_database = "database"

if not database_starter.db_exists(default_database):
    database_starter.create_template_database()

print("Python SQLite Console")


def strip_text(text, to_strip):
    ret_val = text
    ret_val = ret_val.replace(to_strip.upper(), '', 1)
    ret_val = ret_val.replace(to_strip.lower(), '', 1)
    ret_val = ret_val.replace(';', '')
    ret_val = ret_val.replace(' ', '')
    return ret_val


def main_loop():
    loop_continues = True
    con = sqlite3.connect("dbs/database.db")
    cur = con.cursor()

    while loop_continues:
        var = input("py-sqlite3> ")

        if var == "exit" or var == "exit()":
            loop_continues = False
        elif var.startswith("CREATE DATABASE ") or var.startswith("create database "):
            new_db = strip_text(var, "CREATE DATABASE ")
            if not database_starter.db_exists(new_db):
                con.close()
                con = sqlite3.connect("dbs/" + new_db + ".db")
                cur = con.cursor()
            else:
                print("Database already exists! Aborting.")
        elif var.startswith("USE ") or var.startswith("use "):D
            use_db = strip_text(var, "USE ")
            if database_starter.db_exists(use_db):
                con.close()
                con = sqlite3.connect("dbs/" + use_db + ".db")
                cur = con.cursor()
                print("Changed to database " + use_db)
            else:
                print(use_db + " doesn't exist!")
        else:
            try:
                query = cur.execute(var)

                if query.description is not None:
                    column_names = [
                        description[0] for description in query.description
                    ]
                    print("(", ", ".join(column_names), ")", sep='')
                    for row in query:
                        print(row)
                else:
                    con.commit()
            except sqlite3.Error as e:
                print("Error: ", e, sep='')
    else:
        con.close()


main_loop()
