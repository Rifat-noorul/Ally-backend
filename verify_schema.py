import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

print(f"Connecting to {url}...")
supabase: Client = create_client(url, key)

tables = ["users", "sos_videos", "user_activity_logs"]

for table in tables:
    try:
        response = supabase.table(table).select("*").limit(1).execute()
        print(f"✅ Schema for '{table}' is verified and accessible! Data: {response.data}")
    except Exception as e:
        print(f"❌ Error accessing '{table}': {e}")
