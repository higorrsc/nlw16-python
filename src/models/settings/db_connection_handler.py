import sqlite3
from sqlite3 import Connection


class DbConnectionHandler:
    def __init__(self) -> None:
        """
        Initializes the DbConnectionHandler object with the default
        connection string "storage.db" and sets the connection to None.
        """
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        """
        Connects to the database using the provided connection string
        and sets the connection object.
        """
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        self.__conn = conn

    def close(self) -> None:
        """
        Closes the database connection.
        """
        self.__conn.close()

    def get_connection(self) -> Connection:
        """
        Retrieves the current database connection object.

        Returns:
            The current database connection object.
        """
        return self.__conn


db_connection_handler = DbConnectionHandler()
