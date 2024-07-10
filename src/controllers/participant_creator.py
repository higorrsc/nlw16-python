import uuid
from typing import Dict


class ParticipantCreator:
    def __init__(self, participants_repository, emails_repository) -> None:
        """
        Initializes a new instance of the ParticipantCreator class.

        Args:
            participants_repository (ParticipantsRepository): The repository for managing participants.
            emails_repository (EmailsRepository): The repository for managing emails.

        Returns:
            None
        """
        self.__participants_repository = participants_repository
        self.__emails_repository = emails_repository

    def create(self, body: Dict, trip_id: str) -> Dict:
        """
        Creates a new participant with the provided body information and trip ID.

        Args:
            body (Dict): A dictionary containing the participant information.
            trip_id (str): The ID of the trip associated with the participant.

        Returns:
            Dict: A dictionary containing the participant ID and status code.
                - body (Dict): A dictionary containing the participant ID.
                    - participant_id (str): The ID of the newly created participant.
                - status_code (int): The status code of the response.
                    - 201: The participant was successfully created.
                    - 400: The request body was invalid.

        Raises:
            Exception: If an error occurs during the participant creation process.
        """
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            emails_info = {
                "email": body["email"],
                "id": email_id,
                "trip_id": trip_id,
            }

            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"],
            }

            self.__emails_repository.registry_email(emails_info)
            self.__participants_repository.registry_participant(participant_infos)

            return {
                "body": {
                    "participant_id": participant_id,
                },
                "status_code": 201,
            }
        except Exception as error:
            return {
                "body": {"error": "Bad Request", "message": str(error)},
                "status_code": 400,
            }
