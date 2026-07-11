"""Check database schema and restore species files"""
import sqlite3, os

db = sqlite3.connect("D:/Reasonix/database.db")

# List all tables
tables = db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tables:", [t[0] for t in tables])

# Check species table
for table_name, in tables:
    print(f"\n=== {table_name} ===")
    cols = db.execute(f"PRAGMA table_info({table_name})").fetchall()
    for c in cols:
        print(f"  {c[1]} ({c[2]})")
    try:
        count = db.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        print(f"  rows: {count}")
    except:
        pass

db.close()
