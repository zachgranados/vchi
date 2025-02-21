import ebp_finder as ebp
import provider_db_setup as setup
# ebp.write_html()

# creates dictionary with info
providers = ebp.collect_provider_info("static_ebp.txt")

# creates db 
setup.create_db()

