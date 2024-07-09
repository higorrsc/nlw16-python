import uuid

import pytest

from src.models.settings.db_connection_handler import db_connection_handler

from .links_repository import LinksRepository


db_connection_handler.connect()
TRIP_ID = str(uuid.uuid4())


@pytest.mark.skip(reason="database interaction")
def test_registry_link() -> None:
    """
    A test case that skips due to database interaction. It initializes connection,
    creates link information, and calls the registry_link function.
    """
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    link_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": TRIP_ID,
        "link": "https://www.google.com",
        "title": "Google",
    }
    links_repository.registry_link(link_infos=link_infos)


@pytest.mark.skip(reason="database interaction")
def test_find_links_from_trip() -> None:
    """
    A test case that skips due to database interaction. It initializes connection,
    retrieves links associated with a specific trip ID, and prints the result.
    """
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    links = links_repository.find_links_from_trip(trip_id=TRIP_ID)
    print(links)
