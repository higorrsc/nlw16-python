import uuid
from typing import Dict

from src.drivers.email_sender import send_email


class TripCreator:
    def __init__(self, trip_repository, emails_repository) -> None:
        """
        Initializes the TripCreator object.

        Args:
            trip_repository (TripRepository): The repository for managing trips.
            emails_repository (EmailsRepository): The repository for managing emails.

        Returns:
            None
        """
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> Dict:
        """
        Creates a new trip with the given body information.

        Args:
            body (Dict): A dictionary containing the trip information.

        Returns:
            Dict: A dictionary containing the trip ID and status code.
                - body (Dict): A dictionary containing the trip ID.
                    - id (str): The ID of the newly created trip.
                - status_code (int): The status code of the response.
                    - 201: The trip was successfully created.
                    - 400: The request body was invalid.

        Raises:
            Exception: If an error occurs during the trip creation process.
        """
        try:
            emails = body.get("emails_to_invite")

            trip_id = str(uuid.uuid4())
            trip_infos = {
                **body,
                "id": trip_id,
            }

            self.__trip_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__emails_repository.registry_email(
                        {
                            "id": str(uuid.uuid4()),
                            "trip_id": trip_id,
                            "email": email,
                        }
                    )
            send_email(
                [body["owner_email"]],
                f"<p>Confirmação de viagem: <a href='http://localhost:3000/trips/{trip_id}/confirm'>clique aqui</a></p>",
            )
            return {"body": {"id": trip_id}, "status_code": 201}

        except Exception as error:
            return {
                "body": {"error": "Bad Request", "message": str(error)},
                "status_code": 400,
            }
