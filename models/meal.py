from models.__init__ import CONN, CURSOR

class Meal:
    def __init__(self, id, name, easiness, prep_time, rating, category_id):
        self.id = id
        self.name = name
        self.easiness = easiness
        self.prep_time = prep_time
        self.rating = rating
        self.category_id = category_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @classmethod
    def create_table(cls):
        # take out check(easiness) and do it in validations in setters 
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS meals(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL, 
                easiness INTEGER CHECK(easiness BETWEEN 1 AND 5),
                prep_time INTEGER NOT NULL,
                rating INTEGER CHECK(easiness BETWEEN 1 AND 5), 
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """)
        CONN.commit()

    @classmethod
    def create(cls, name, easiness, prep_time, rating, category_id):
        CURSOR.execute("""
            INSERT INTO meals (name, easiness, prep_time, rating, category_id) 
            VALUES (?, ?, ?, ?, ?)
        """, (name, easiness, prep_time, rating, category_id))
        CONN.commit()
        return cls(CURSOR.lastrowid, name, easiness, prep_time, rating, category_id)
    
    @classmethod
    def get_by_category(cls, category_id):
        CURSOR.execute("SELECT * FROM meals WHERE category_id = ?", (category_id,))
        return [cls(*row) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM meals where name = ?", (name,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM meals")
        return [cls(*row) for row in CURSOR.fetchall()]
    
    def update(self, new_easiness=None, new_prep_time=None, new_rating=None):
        if new_easiness is not None:
            self.easiness = new_easiness
            CURSOR.execute("UPDATE meals SET easiness = ? WHERE id= ?", (self.easiness, self.id))

        if new_prep_time is not None:
            self.prep_time = new_prep_time
            CURSOR.execute("UPDATE meals SET prep_time = ? WHERE id= ?", (self.prep_time, self.id))

        if new_rating is not None:
            self.new_rating = new_rating
            CURSOR.execute("UPDATE meals SET rating = ? WHERE id= ?", (self.rating, self.id))

        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM meals WHERE id = ?", (self.id,))
        CONN.commit()

    def get_categories(self):
        from models.category import Category
        return Category.find_by_id(self.id)

    def __str__(self): # move to cli 
        return f"{self.name} ({self.category})"