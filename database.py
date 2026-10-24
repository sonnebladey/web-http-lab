import os
import psycopg 
from dotenv import load_dotenv 
load_dotenv() #load .env env gives us connection to db 
#through local base unix socket with current user macos 
DATABASE_URL = os.getenv("DATABASE_URL") # receives database adress from enviroment's variables 

def get_connection(): # for connection establishing
    return psycopg.connect(DATABASE_URL)
