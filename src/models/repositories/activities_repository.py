from sqlite3 import Connection
from typing import Dict, List, Tuple


class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        """
        Initializes the ActivitiesRepository object with the provided database connection.

        Args:
            conn (Connection): A connection to the database.

        Returns:
            None
        """
        self.__conn = conn

    def registry_activity(self, activity_infos: Dict) -> None:
        """
        Inserts activity information into the 'activities'
        table based on the provided activity_infos dictionary.

        Args:
            activity_infos (Dict): A dictionary containing information about the activity
                                including id, trip_id, and activity.

        Returns:
            None
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO activities
                (id, trip_id, title, occurs_at)
            VALUES
                (?, ?, ?, ?)
            """,
            (
                activity_infos["id"],
                activity_infos["trip_id"],
                activity_infos["title"],
                activity_infos["occurs_at"],
            ),
        )
        self.__conn.commit()

    def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
        """
        Finds all the activities associated with a given trip ID.

        Args:
            trip_id (str): The ID of the trip to find activities for.

        Returns:
            List[Tuple]: A list of tuples, where each tuple represents an
                        activity and contains the following information:
                - id (str): The ID of the activity.
                - trip_id (str): The ID of the trip the activity is associated with.
                - title (str): The title of the activity.
                - occurs_at (str): The date and time the activity occurs.
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                SELECT *
                FROM activities
                WHERE trip_id = ?
            """,
            (trip_id,),
        )
        activities = cursor.fetchall()
        return activities
