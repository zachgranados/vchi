import sqlite3
import os


# sets up a sqlite db
def create_db(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn


# creates table for all providers
def create_provider_table(cur, conn):
    # creates a table for all provider names, allows us to track duplicates
    cur.execute(
        "CREATE TABLE IF NOT EXISTS providers (provider_id INTEGER PRIMARY KEY AUTOINCREMENT, provider_name TEXT UNIQUE, address TEXT UNIQUE, zip_code TEXT, website TEXT UNIQUE, email TEXT UNIQUE, phone TEXT UNIQUE, source TEXT)"
    )
    conn.commit()

def input_providers(cur, conn, provider_dict):
    for office in provider_dict:
        cur.execute("SELECT COUNT(*) FROM providers WHERE provider_name = ?", (office,))
        row_count = cur.fetchone()[0]
        
        # checks for no duplicates
        if row_count != 0:
            continue
        
        address = provider_dict[office]["ADDRESS"]
        email = provider_dict[office]["EMAIL"]
        phone = provider_dict[office]["PHONE"]
        zip_code = provider_dict[office]["ZIP"]
        website = provider_dict[office]["WEBSITE"]
        source = provider_dict[office]["SOURCE"]
        #print(office + " Added to database")

        cur.execute("INSERT OR IGNORE INTO providers (provider_name, address, zip_code, website, email, phone, source) VALUES (?,?,?,?,?,?,?)", (office, address, zip_code, website, email, phone, source))
    
    conn.commit()



            
