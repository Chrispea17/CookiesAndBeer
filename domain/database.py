'''
This database has this schema
Recommendations:
RecommendationID: Primary Key - Unique ID for the Recommendation (iter)
UniqueUserMatchID: Foreign Key Identifying User to User Match (eg User1User2 is distinct from User2User1 because of the direction the recommendation is going)
ItemID: Foreign Key Identifying an Item
URL: URL of the Place or Item
Rating: Boolean options 1,0,null based on whether the recommendation was liked or disliked or not taken

Items: 
Item ID: Primary Key Identifying an Item (iter)
Item Name: Name of Item (lc string)

Relationships (stashed for later)
UserIDRequester: ID of the requester
User ID Reccommend: ID of the recommender
UniqueUserMatchID: Iter Match for RequestUser->RecommendUser

Rankings:
UniqueUserMatchID: ForeignKey identifying the relationship
UniqueUserMatchSeq: String Identifying UserIDRequester - UserIDRecommender
SumRatings: Cumulative Sum for the ratings for this UniqueUSerMatchID
Counter: A Counter Identifying how many requests have been taken
Rank: Calculated as the SumRatings/Counter

CREATE TABLE IF NOT EXISTS recommendations
(
    recommendationID INTEGER PRIMARY KEY AUTOINCREMENT
    uniqueUserMatchID INTEGER FOREIGN KEY
    itemID INTEGER FOREIGN KEY
    url TEXT NOT NULL
    rating BOOLEAN
)

CREATE TABLE IF NOT EXISTS items
(
    itemID INTEGER FOREIGN KEY
    itemName TEXT NOT NULL
)

CREATE TABLE IF NOT EXISTS rankings
(
    uniqueUserMatchID INTEGER PRIMARY KEY AUTOINCREMENT
    uniqueUserMatchSeq TEXT NOT NULL
    sumRatings REAL
    counter INTEGER
    RANK REAL
)
'''
import sqlite3

##used from database barky code
class DatabaseManager:
    def __init__(self, database_filename) -> None:
        self.database_filename = database_filename
        self.connection = sqlite.connect(database_filename)

    def __del__(self):
        self.connection.close()

    def _execute(self,statement, values=None):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement,values or [])
            return cursor

    def create_table(self, table_name, columns):
        columns_with_types = [f'{column_name} {data type}' for column_name, data_type in columns.items()
        ]

        self._execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name}
            ({','.join(columns_with_types)});
            '''
        )

def drop_table(self,table_name):
    self._execute(f'''
    DROP TABLE {table_name};
            '''
        )

#this is where the fun starts and where I will really start to use this in my code

def add(self, table_name, data):
    placeholders = ', '.join('?' * len(data))
    column_names = ', '.join(data.keys())
    column_values = tuple(data.values())
    
    self._execute(
            f'''
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            ''',
            column_values,
        )

def delete(self, table_name, criteria):
    placeholders = [f'{column} = ?' for column in criteria.keys()]
    delete_criteria = ' AND '.join(placeholders)
    self._execute(
        f'''
        DELETE FROM {table_name}
        WHERE {delete_criteria};
        ''',
        tuple(criteria.values()), #https://www.w3schools.com/python/python_tuples.asp
    )

def select(self, table_name, criteria=None, order_by=None):
        criteria = criteria or {}

        query = f'SELECT * FROM {table_name}'
        if criteria:
            placeholders = [f'{column} = ?' for column in criteria.keys()]
            select_criteria = ' AND '.join(placeholders)
            query += f' WHERE {select_criteria}'

        if order_by:
            query += f' ORDER BY {order_by}'

        return self._execute(
            query,
            tuple(criteria.values()),
        )

def update(self, table_name, data, criteria):
    placeholders = ', '.join('?' * len(data))
    column_names = ', '.join(data.keys())
    column_values = tuple(data.values())
    self._execute(
            f'''
            UPDATE {table_name}
            SET {data}
            WHERE {criteria};
            ''',
            column_values,
        )   