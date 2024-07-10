from typing import Dict


class TripFinder:
    def __init__(self, trips_repository) -> None:
        """
        Initializes the TripFinder object.

        Args:
            trips_repository (TripRepository): The repository for managing trips.

        Returns:
            None
        """
        self.__trips_repository = trips_repository

    def find_trip_details(self, trip_id: str) -> Dict:
        """
        Finds a trip details.

        Args:
            trip_id (str): The ID of the trip to find.

        Returns:
            Dict: A dictionary containing the trip information.
                - body (Dict): A dictionary containing the trip information.
                    - id (str): The ID of the trip.
                    - title (str): The title of the trip.
                    - description (str): The description of the trip.
        """
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception("No Trip Found")

            return {
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "starts_at": trip[2],
                        "ends_at": trip[3],
                        "status": trip[6],
                    }
                },
                "status_code": 200,
            }
        except Exception as error:
            return {
                "body": {"error": "Bad Request", "message": str(error)},
                "status_code": 400,
            }
