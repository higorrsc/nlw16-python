from sqlite3 import Connection
from typing import Dict, Tuple


class TripsRepository:
    def __init__(self, conn: Connection) -> None:
        """
        Initializes the TripsRepository object with the provided database connection.

        Args:
            conn (Connection): A connection to the database.

        Returns:
            None
        """
        self.__conn = conn

    def create_trip(self, trip_infos: Dict) -> None:
        """
        Inserts a new trip into the 'trips' table with the provided trip_infos.

        Args:
            trip_infos (Dict): A dictionary containing information about the trip
            including id, destination, start_date, end_date, owner_name, and owner_email.

        Returns:
            None
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO trips
                (id, destination, start_date, end_date, owner_name, owner_email)
            VALUES
                (?, ?, ?, ?, ?, ?)
            """,
            (
                trip_infos["id"],
                trip_infos["destination"],
                trip_infos["start_date"],
                trip_infos["end_date"],
                trip_infos["owner_name"],
                trip_infos["owner_email"],
            ),
        )
        self.__conn.commit()

    def find_trip_by_id(self, trip_id: str) -> Tuple:
        """
        Find a trip by its ID.

        Args:
            trip_id (str): The ID of the trip to find.

        Returns:
            Tuple: A tuple containing the details of the trip found, or None if no trip is found.

        Description:
            This function retrieves a trip from the 'trips' table in the database
            based on the provided trip ID. It uses a cursor to execute a SQL query
            and fetches the first row of the result set. The function returns the
            fetched row as a tuple, or None if no trip is found.

        Example:
            trip = find_trip_by_id('123')
            print(trip)  # Output: ('123',
                                    'Destination',
                                    '2022-01-01',
                                    '2022-01-05',
                                    'John Doe',
                                    'john.doe@example.com')
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                SELECT *
                FROM trips
                WHERE id = ?
            """,
            (trip_id,),
        )
        trip = cursor.fetchone()
        return trip

    def update_trip_status(self, trip_id: str) -> None:
        """
        Update the status of a trip in the 'trips' table.

        Args:
            trip_id (str): The ID of the trip to update.

        Returns:
            None
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            UPDATE trips
            SET status = 1
            WHERE id = ?
            """,
            (trip_id,),
        )
        self.__conn.commit()
