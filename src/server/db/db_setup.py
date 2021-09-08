import sqlite3


def create_tables(conn):
    conn.execute("""
    CREATE TABLE mytable (foo INT)
    """)


def connect_to_db():
    conn = sqlite3.connect('~/working.db', isolation_level='IMMEDIATE')
    return conn


def main():
    create_tables(connect_to_db())