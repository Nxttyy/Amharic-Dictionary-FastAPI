import sqlite3
from sqlite3 import Error
import json

database = './ahun.sqlite'
conn = None

def create_connection():
    global conn
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    return conn

if(not conn):
    create_connection()
    print("New db connection")

def only_id(row):
    return row[0]

def edit_format(word) -> str:
    return word[0].upper() + word[1:].lower()

def suggest_words(prompt) -> list:
    limit = 5
    prompt = edit_format(prompt)

    cur = conn.cursor()
    cur.execute(f"SELECT * FROM 'dictionary' WHERE instr(_id, '{prompt}') > 0 LIMIT {limit}")
    rows = cur.fetchall()
    res = list(map(only_id, rows))

    return res

def define_word(prompt) -> json:
    prompt = edit_format(prompt)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM 'dictionary' WHERE _id=='{prompt}'")
    rows = cur.fetchall()
    
    for row in rows:
        return [row[0], row[1], row[2]]
    else:
        return ['', '', '']
