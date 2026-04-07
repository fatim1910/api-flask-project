import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "database.db")

DEBUG = True
HOST  = "0.0.0.0"
PORT  = 5000