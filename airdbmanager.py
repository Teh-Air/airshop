import mysql.connector

class AirDBManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host="194.28.226.217:33062",
            user="air",
            password="@@@AIR777",
            database="air"
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except mysql.connector.Error as error:
            print("Database error:", error)
            self.connection.rollback()
            return False

    def fetch_one(self, query, values=None):
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result

    def fetch_all(self, query, values=None):
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    def insert_counterparty(self, name, inn, address, email, phone, info):
        query = "INSERT INTO counterparty (name, inn, address, email, phone, info) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, inn, address, email, phone, info)
        return self.execute_query(query, values)

    def insert_service(self, name, cost, counterparty, info, availability):
        query = "INSERT INTO services (name, cost, counterparty, info, availability) VALUES (%s, %s, %s, %s, %s)"
        values = (name, cost, counterparty, info, availability)
        return self.execute_query(query, values)

    # Добавьте функции для работы с другими таблицами (product, income, user, и т. д.) по аналогии.
