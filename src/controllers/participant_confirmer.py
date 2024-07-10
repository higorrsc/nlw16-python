from typing import Dict


class ParticipantConfirmer:
    def __init__(self, participants_repository) -> None:
        """
        Initializes the ParticipantConfirmer class.

        Args:
            participants_repository (ParticipantsRepository): The repository
                                                            for managing participants.

        Returns:
            None
        """
        self.__participants_repository = participants_repository

    def confirm(self, participant_id: str) -> Dict:
        """
        Confirm the status of a participant.

        Args:
            participant_id (str): The ID of the participant.

        Returns:
            Dict: A dictionary containing the response body and the HTTP status code.
                - body (Dict or None): A dictionary containing the response body.
                  If the operation is successful, the dictionary will be empty.
                - status_code (int): The HTTP status code of the response.
                    - 204: The participant status was successfully updated.
                    - 400: An error occurred during the operation.

        Raises:
            Exception: If an error occurs during the operation.

        """
        try:
            self.__participants_repository.update_participant_status(participant_id)
            return {"body": None, "status_code": 204}
        except Exception as error:
            return {
                "body": {"error": "Bad Request", "message": str(error)},
                "status_code": 400,
            }
