import ebp_finder as ebp
import provider_db_setup as setup

import sqlite3
import pandas as pd

# gets data
data = ebp.collect_provider_info("static_ebp.txt")

# creates db
result = setup.create_db("bh_directory.db")
cur = result[0]
conn = result[1]

# creates the provider table
setup.create_provider_table(cur, conn)

#inputs into provider table
setup.input_providers(cur, conn, data)


# writing sample db to an excel file for testing
def export_db_to_excel(db_path, excel_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Get all table names
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql(query, conn)

    # Create a Pandas Excel writer
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        for table in tables["name"]:
            # Read table into a DataFrame
            df = pd.read_sql(f"SELECT * FROM {table}", conn)
            # Write to a new sheet in the Excel file
            df.to_excel(writer, sheet_name=table, index=False)
    
    # Close the database connection
    conn.close()
    print(f"Database exported to {excel_path}")


export_db_to_excel("bh_directory.db", "test_bh_directory.xlsx")

