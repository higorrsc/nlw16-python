import uuid
from datetime import datetime, timedelta

import pytest

from src.models.settings.db_connection_handler import db_connection_handler

from .trips_repository import TripsRepository

db_connection_handler.connect()
TRIP_ID = str(uuid.uuid4())


@pytest.mark.skip(reason="database interaction")
def test_create_trip() -> None:
    """
    A test case that creates a trip in the database. It initializes connection,
    creates trip information, and inserts the trip into the 'trips' table.
    """
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trips_infos = {
        "id": TRIP_ID,
        "destination": "Osasco",
        "start_date": datetime.strptime("30-07-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("30-07-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Higor Cruz",
        "owner_email": "higorrsc@gmail.com",
    }

    trips_repository.create_trip(trips_infos=trips_infos)


@pytest.mark.skip(reason="database interaction")
def test_find_trip_by_id() -> None:
    """
    A test case that finds a trip by its ID. It initializes connection,
    creates a TripsRepository object, finds a trip based on the provided trip ID,
    and prints the result.
    """
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trip = trips_repository.find_trip_by_id(trip_id=TRIP_ID)
    print(trip)


@pytest.mark.skip(reason="database interaction")
def test_update_trip_status() -> None:
    """
    A test case that updates the status of a trip in the database. It initializes connection,
    creates an instance of the TripsRepository class, and calls the update_trip_status method
    with the provided trip_id. This test is marked to skip database interaction.
    """
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trips_repository.update_trip_status(trip_id=TRIP_ID)
