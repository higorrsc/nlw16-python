import uuid
from typing import Dict


class LinkCreator:
    def __init__(self, links_repository) -> None:
        """
        Initializes the LinkCreator object.

        Args:
            links_repository (LinksRepository): The repository for managing links.

        Returns:
            None
        """
        self.__links_repository = links_repository

    def create(self, body: Dict, trip_id: str) -> Dict:
        """
        Creates a new link with the provided body and trip ID.

        Args:
            body (Dict): A dictionary containing the link information.
            trip_id (str): The ID of the trip associated with the link.

        Returns:
            Dict: A dictionary containing the newly created link ID and the status code.
                - body (Dict): A dictionary containing the link ID.
                    - linkId (str): The ID of the newly created link.
                - status_code (int): The status code of the response.
                    - 201: The link was successfully created.
                    - 400: The request body was invalid.

        Raises:
            Exception: If an error occurs during the link creation process.
        """
        try:
            link_id = str(uuid.uuid4())
            link_infos = {
                "link": body["url"],
                "title": body["title"],
                "id": link_id,
                "trip_id": trip_id,
            }
            self.__links_repository.registry_link(link_infos)
            return {
                "body": {
                    "linkId": link_id,
                },
                "status_code": 201,
            }
        except Exception as error:
            return {
                "body": {"error": "Bad Request", "message": str(error)},
                "status_code": 400,
            }
