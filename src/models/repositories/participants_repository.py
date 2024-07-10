from sqlite3 import Connection
from typing import Dict, List, Tuple


class ParticipantsRepository:

    def __init__(self, conn: Connection) -> None:
        """
        Initializes the ParticipantsRepository object with the provided database connection.

        Args:
            conn (Connection): A connection to the database.

        Returns:
            None
        """
        self.__conn = conn

    def registry_participant(self, participant_infos: Dict) -> None:
        """
        Inserts participant information into the 'participants' table
        based on the provided participant_infos dictionary.

        Args:
            participant_infos (Dict): A dictionary containing information about the participant
                                      including id, trip_id, email_to_invite_id, and name.

        Returns:
            None
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO participants
                    (id, trip_id, emails_to_invite_id, name)
                VALUES
                    (?, ?, ?, ?)
            """,
            (
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["emails_to_invite_id"],
                participant_infos["name"],
            ),
        )
        self.__conn.commit()

    def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
        """
        Finds all the participants associated with a given trip ID.

        Args:
            trip_id (str): The ID of the trip to find participants for.

        Returns:
            List[Tuple]: A list of tuples, where each tuple represents a
                        participant and contains the following information:
                - id (str): The ID of the participant.
                - name (str): The participant name.
                - is_confirmed (bool): The ID of the trip the participant is associated with.
                - email (str): The participant email.
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                SELECT
                    p.id,
                    p.name,
                    p.is_confirmed,
                    e.email
                FROM
                    participants as p
                        INNER JOIN emails_to_invite as e
                        ON p.emails_to_invite_id = e.id
                WHERE
                    p.trip_id = ?
            """,
            (trip_id,),
        )
        participants = cursor.fetchall()
        return participants

    def update_participant_status(self, participant_id: str) -> None:
        """
        Updates the status of a participant to confirmed in the database.

        Args:
            participant_id (str): The ID of the participant to update.

        Returns:
            None
        """
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                UPDATE participants
                SET is_confirmed = 1
                WHERE id = ?
            """,
            (participant_id,),
        )
        self.__conn.commit()
