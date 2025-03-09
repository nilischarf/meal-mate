from models.__init__ import CONN, CURSOR

class Meal:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category
    
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS meals(
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL, 
                category TEXT NOT NULL
            )
        """)
        CONN.commit()
    
    @classmethod
    def create(cls, name, category):
        CURSOR.execute("INSERT INTO meals (name, category) VALUES (?, ?)", (name, category))
        CONN.commit()
        return cls.find_by_name(name)
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM meals where name = ?", (name,))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM meals")
        return [cls(row[1], row[2], row[0]) for row in CURSOR.fetchall()]
    
    def delete(self):
        CURSOR.execute("DELETE FROM meals WHERE id = ?", (self.id,))
        CONN.commit()

    def get_ingredients(self):
        from models.ingredient import Ingredient
        return Ingredient.get_by_meal_id(self.id)

    def __str__(self):
        return f"{self.name} ({self.category})"