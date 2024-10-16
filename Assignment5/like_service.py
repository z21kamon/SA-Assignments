import sqlite3

class LikeService:
    def like_post(self, id_):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        likes_count = self.get_likes(id_)
        if likes_count is not None:
            cur.execute("UPDATE posts SET likes_count=? WHERE id=?",
                        (likes_count + 1, id_,))
            con.commit()
            return True
        return False

    def get_likes(self, message_id):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        res = cur.execute("SELECT likes_count FROM posts WHERE id=?",
                          (message_id,)).fetchone()
        return res[0] if res is not None else None