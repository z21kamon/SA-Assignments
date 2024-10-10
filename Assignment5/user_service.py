import sqlite3


class UserService:
    def sign_up(self, username):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        if self.user_exists(username):
            return False
        cur.execute("INSERT INTO users(username) VALUES(?)",
                    (username,))
        con.commit()
        return True

    def user_exists(self, username):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        res = cur.execute("SELECT * FROM users WHERE username=?",
                          (username,)).fetchone()
        return True if res else False