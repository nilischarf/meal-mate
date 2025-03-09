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
                name TEXT, 
                meal_id INTEGER
                # check out foreign key
            )
        """)
        CONN.commit()