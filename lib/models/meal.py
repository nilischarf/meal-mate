from models.__init__ import CONN, CURSOR
from models.category import Category

class Meal:
    all = {} 

    def __init__(self, name, easiness, prep_time, rating, category_id, id=None):
        self.id = id
        self.name = name
        self.easiness = easiness
        self.prep_time = prep_time
        self.rating = rating
        self.category_id = category_id
    
    def __repr__(self):
        return (
            f"<Meal {self.id}: {self.name}, {self.easiness}, {self.prep_time}, {self.rating}, " +
            f"Category ID: {self.category_id}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string."
            )

    @property
    def easiness(self):
        return self._easiness

    @easiness.setter
    def easiness(self, easiness):
        if isinstance(easiness, int) and 1 <= easiness <= 5:
            self._easiness = easiness
        else:
            raise ValueError(
                "Easiness must be an integer between 1 and 5."
            )

    @property
    def prep_time(self):
        return self._prep_time

    @prep_time.setter
    def prep_time(self, prep_time):
        if isinstance(prep_time, int) and 0 < prep_time:
            self._prep_time = prep_time
        else:
            raise ValueError(
                "Prep time must be an integer greater than 0."
            )

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5:
            self._rating = rating
        else:
            raise ValueError(
                "Rating must be an integer between 1 and 5."
            )

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if type(category_id) is int and Category.find_by_id(category_id):
            self._category_id = category_id
        else:
            raise ValueError(
                "category_id must reference a category in the database."
            )
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE meals (
                id INTEGER PRIMARY KEY,
                name TEXT, 
                easiness INTEGER,
                prep_time INTEGER,
                rating INTEGER, 
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS meals;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO meals (name, easiness, prep_time, rating, category_id)
                VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.easiness, self.prep_time, self.rating, self.category_id,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE meals
            SET name = ?, easiness = ?, prep_time = ?, rating = ?, category_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.easiness, self.prep_time, self.rating, self.category_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM meals
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, easiness, prep_time, rating, category_id):
        meal = cls(name, easiness, prep_time, rating, category_id)
        meal.save()
        return meal

    @classmethod
    def instance_from_db(cls, row):
        meal = cls.all.get(row[0])
        if meal:
            meal.name = row[1]
            meal.easiness = row[2]
            meal.prep_time = row[3]
            meal.rating = row[4]
            meal.category_id = row[5]
        else:
            meal = cls(row[1], row[2], row[3], row[4], row[5], row[0])
            cls.all[meal.id] = meal
        return meal

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM meals
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM meals
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM meals
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
