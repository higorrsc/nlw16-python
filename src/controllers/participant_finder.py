from typing import Dict


class ParticipantsFinder:
    def __init__(self, participants_repository) -> None:
        """
        Initializes the ParticipantsFinder object with the provided participants repository.

        Args:
            participants_repository: The repository for managing participants.

        Returns:
            None
        """
        self.__participants_repository = participants_repository

    def find(self, trip_id: str) -> Dict:
        """
        Finds participants for a given trip ID and formats them into a dictionary.

        Args:
            trip_id (str): The ID of the trip to find participants for.

        Returns:
            Dict: A dictionary containing the formatted participants and the status code.
                - body (Dict): A dictionary containing the participants.
                - participants (List[Dict]): A list of participants with their ID, email and name.
                - status_code (int): The HTTP status code of the response.
        """
        try:
            participants = self.__participants_repository.find_participants_from_trip(
                trip_id
            )
            formatted_participants = []
            for participant in participants:
                formatted_participants.append(
                    {
                        "id": participant[0],
                        "email_to_invite": participant[2],
                        "name": participant[3],
                    }
                )
            return {
                "body": {
                    "participants": formatted_participants,
                },
                "status_code": 200,
            }
        except Exception as error:
            return {
                "body": {"error": "Bad Request", "message": str(error)},
                "status_code": 400,
            }
