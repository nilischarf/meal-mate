from models.__init__ import CONN, CURSOR

class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL, 
            )
        """)
        CONN.commit()

    @classmethod
    def create(cls, name):
        CURSOR.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        CONN.commit()
        return cls(CURSOR.lastrowid, name)

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM categories")
        return [cls(*row) for row in CURSOR.fetchall()]
   
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM categories where name = ?", (name,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM categories WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None
    
    def delete(self):
        CURSOR.execute("DELETE FROM categories WHERE id = ?", (self.id))
        CONN.commit()
    
    def __str__(self):
        return f"{self.name}"