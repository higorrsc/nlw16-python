import uuid
from typing import Dict


class ActivityCreator:
    def __init__(self, activities_repository) -> None:
        """
        Initializes a new instance of the `ActivityCreator` class.

        Args:
            activities_repository (ActivitiesRepository): The repository for managing activities.

        Returns:
            None
        """
        self.__activities_repository = activities_repository

    def create(self, body: Dict, trip_id: str) -> Dict:
        """
        Creates a new activity with the provided body information and trip ID.

        Args:
            body (Dict): A dictionary containing the activity information.
            trip_id (str): The ID of the trip associated with the activity.

        Returns:
            Dict: A dictionary containing the newly created activity ID and the status code.
                - body (Dict): A dictionary containing the activity ID.
                    - activity_id (str): The ID of the newly created activity.
                - status_code (int): The status code of the response.
                    - 201: The activity was successfully created.
                    - 400: The request body was invalid.

        Raises:
            Exception: If an error occurs during the activity creation process.
        """
        try:
            activity_id = str(uuid.uuid4())

            activity_infos = {
                "id": activity_id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
            }

            self.__activities_repository.registry_activity(activity_infos)

            return {
                "body": {
                    "activity_id": activity_id,
                },
                "status_code": 201,
            }
        except Exception as error:
            return {
                "body": {"error": "Bad Request", "message": str(error)},
                "status_code": 400,
            }
