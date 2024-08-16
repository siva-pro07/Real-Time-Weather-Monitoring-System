import sqlite3

def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            date TEXT NOT NULL,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_daily_summary(location, summary):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO daily_summary (location, date, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (location, summary['date'], summary['avg_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    conn.close()


