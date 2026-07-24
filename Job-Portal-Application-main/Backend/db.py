import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_raw_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS candidate (
        candidate_id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        qualification TEXT,
        skills TEXT,
        experience INTEGER,
        password TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employer (
        employer_id INTEGER PRIMARY KEY,
        company_name TEXT NOT NULL,
        hr_name TEXT,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        location TEXT,
        industry TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS job (
        job_id INTEGER PRIMARY KEY,
        job_title TEXT NOT NULL,
        company_name TEXT NOT NULL,
        location TEXT,
        job_type TEXT,
        experience_required INTEGER,
        salary REAL,
        last_date TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS job_application (
        application_id INTEGER PRIMARY KEY,
        candidate_name TEXT NOT NULL,
        company_name TEXT NOT NULL,
        job_title TEXT NOT NULL,
        applied_date TEXT,
        resume TEXT,
        application_status TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS interview (
        interview_id INTEGER PRIMARY KEY,
        candidate_name TEXT NOT NULL,
        company_name TEXT NOT NULL,
        interview_date TEXT,
        interview_time TEXT,
        interview_mode TEXT,
        interview_status TEXT
    )''')
    
    conn.commit()
    conn.close()
