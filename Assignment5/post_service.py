import sqlite3
from datetime import datetime


class PostService:
    def post(self, username, content):
        con = sqlite3.connect('database.db')
        cur = con.cursor()

        if len(content) > 400:
            return False

        cur.execute("INSERT INTO posts(author, content, likes_count, time) VALUES(?, ?, 0, ?)",
                    (username, content, datetime.now().strftime("%Y-%m-%d %H:%M:%S%z"))).fetchone()
        con.commit()
        return True

    def get_feed(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        res = cur.execute("SELECT * FROM posts ORDER BY rowid DESC LIMIT 10").fetchall()
        return res