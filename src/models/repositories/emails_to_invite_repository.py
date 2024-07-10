from sqlite3 import Connection
from typing import Dict, List, Tuple


class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        """
        Initializes the TripsRepository object with the provided database connection.

        Args:
            conn (Connection): A connection to the database.

        Returns:
            None
        """
        self.__conn = conn

    def registry_email(self, email_infos: Dict) -> None:
        """
        Inserts email information into the 'emails_to_invite'
        table based on the provided email_infos dictionary.

        Args:
            email_infos (Dict): A dictionary containing information about the email
                                including id, trip_id, and email.

        Returns:
            None
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO emails_to_invite
                (id, trip_id, email)
            VALUES
                (?, ?, ?)
            """,
            (
                email_infos["id"],
                email_infos["trip_id"],
                email_infos["email"],
            ),
        )
        self.__conn.commit()

    def find_emails_from_trip(self, trip_id: str) -> List[Tuple]:
        """
        Finds all the emails associated with a given trip ID.

        Args:
            trip_id (str): The ID of the trip to find emails for.

        Returns:
            List[Tuple]: A list of tuples, where each tuple represents an
                        email and contains the following information:
                - id (str): The ID of the email.
                - trip_id (str): The ID of the trip the email is associated with.
                - email (str): The email address.
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                SELECT *
                FROM emails_to_invite
                WHERE trip_id = ?
            """,
            (trip_id,),
        )
        emails = cursor.fetchall()
        return emails
