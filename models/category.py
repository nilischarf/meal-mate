from models.__init__ import CONN, CURSOR

class Category:
    all = {}

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
            sql = """
                CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY,
                name TEXT)
            """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS categories;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO categories (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    @classmethod
    def create(cls, name):
        CURSOR.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        CONN.commit()
        return cls(CURSOR.lastrowid, name)

    @classmethod
    def get_all(cls):
        category = cls(name)
        category.save()
        return category
   
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
        CURSOR.execute("DELETE FROM categories WHERE id = ?", (self.id,))
        CONN.commit()
    
    def __str__(self): # move to cli 
        return f"{self.name}"