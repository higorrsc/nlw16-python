from typing import Dict


class ActivitiesFinder:
    def __init__(self, activities_repository) -> None:
        """
        Initializes a new instance of the `ActivitiesFinder` class.

        Args:
            activities_repository (ActivitiesRepository): The repository for managing activities.

        Returns:
            None
        """
        self.__activities_repository = activities_repository

    def find(self, trip_id: str) -> Dict:
        """
        Finds activities associated with a given trip ID.

        Args:
            trip_id (str): The ID of the trip to find activities for.

        Returns:
            Dict: A dictionary containing the activities and the status code.
                - body (Dict): A dictionary containing the activities.
                    - activities (List[Dict]): A list of activities with their ID,
                    trip ID, title, and occurs_at.
                - status_code (int): The HTTP status code of the response.
                    - 200: The activities were successfully found.
                    - 400: An error occurred while finding the activities.

        Raises:
            Exception: If an error occurs during the activity finding process.
        """
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)
            formatted_activities = []
            for activity in activities:
                formatted_activities.append(
                    {
                        "id": activity[0],
                        "title": activity[2],
                        "occurs_at": activity[3],
                    }
                )
            return {
                "body": {
                    "activities": formatted_activities,
                },
                "status_code": 200,
            }
        except Exception as error:
            return {
                "body": {"error": "Bad Request", "message": str(error)},
                "status_code": 400,
            }
