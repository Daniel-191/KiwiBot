import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPA_URL = os.getenv("SUPABASE_URL")
SUPA_KEY = os.getenv("SUPABASE_KEY")

if not SUPA_URL or not SUPA_KEY:
    raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY environment variables.")

supabase: Client = create_client(SUPA_URL, SUPA_KEY)
