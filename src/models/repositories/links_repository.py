from sqlite3 import Connection
from typing import Dict, List, Tuple


class LinksRepository:

    def __init__(self, conn: Connection) -> None:
        """
        Initializes the TripsRepository object with the provided database connection.

        Args:
            conn (Connection): A connection to the database.

        Returns:
            None
        """
        self.__conn = conn

    def registry_link(self, link_infos: Dict) -> None:
        """
        Inserts link information into the 'links' table based on the provided link_infos dictionary.

        Args:
            link_infos (Dict): A dictionary containing information about the link
                               including id, trip_id, link, and title.

        Returns:
            None
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO links
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            """,
            (
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["link"],
                link_infos["title"],
            ),
        )
        self.__conn.commit()

    def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
        """
        Finds all the links associated with a given trip ID.

        Args:
            trip_id (str): The ID of the trip to find links for.

        Returns:
            List[Tuple]: A list of tuples, where each tuple represents a
                        link and contains the following information:
                - id (str): The ID of the link.
                - trip_id (str): The ID of the trip the link is associated with.
                - link (str): The link URL.
                - title (str): The link title.
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                SELECT *
                FROM links
                WHERE trip_id = ?
            """,
            (trip_id,),
        )
        trips = cursor.fetchall()
        return trips
