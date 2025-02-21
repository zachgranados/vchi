import ebp_finder as ebp
import provider_db_setup as setup

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