from models.__init__ import CONN, CURSOR

class Ingredient:
    def __init__(self, name, meal_id, id=None):
        self.id = id
        self.name = name
        self.meal_id = meal_id

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS ingredients(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL, 
                meal_id INTEGER NOT NULL,
                FOREIGN KEY (meal_id) REFERENCES meals(id) 
            )
        """)
        CONN.commit()

    @classmethod
    def create(cls, name, meal_id):
        CURSOR.execute("INSERT INTO ingredients (name, meal_id) VALUES (?, ?)", (name, meal_id))
        CONN.commit()
        return cls.find_by_name(name, meal_id)

    @classmethod
    def find_by_name(cls, name, meal_id):
        CURSOR.execute("SELECT * FROM ingredients where name = ? AND meal_id = ?", (name, meal_id))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    @classmethod
    def get_by_meal_id(cls, meal_id):
        CURSOR.execute("SELECT * FROM ingredients WHERE meal_id = ?", (meal_id,))
        return [cls(row[1], row[2], row[0]) for row in CURSOR.fetchall()]
    
    def delete(self):
        CURSOR.execute("DELETE FROM ingredients WHERE id = ?", (self.id))
        CONN.commit()
    
    def __str__(self):
        return f"{self.name}"