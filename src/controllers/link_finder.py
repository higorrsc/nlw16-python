from typing import Dict


class LinkFinder:
    def __init__(self, links_repository) -> None:
        """
        Initializes the LinkFinder object.

        Args:
            links_repository (LinksRepository): The repository for managing links.

        Returns:
            None
        """
        self.__links_repository = links_repository

    def find(self, trip_id: str) -> Dict:
        try:
            links = self.__links_repository.find_links_from_trip(trip_id)
            formatted_links = []
            for link in links:
                formatted_links.append(
                    {"id": link[0], "url": link[2], "title": link[3]}
                )
            return {
                "body": {
                    "links": formatted_links,
                },
                "status_code": 200,
            }
        except Exception as error:
            return {
                "body": {"error": "Bad Request", "message": str(error)},
                "status_code": 400,
            }
