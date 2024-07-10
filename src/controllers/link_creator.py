from typing import Dict
import uuid


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
