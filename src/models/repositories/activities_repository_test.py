from datetime import datetime
import uuid

import pytest

from src.models.settings.db_connection_handler import db_connection_handler

from .activities_repository import ActivitiesRepository

db_connection_handler.connect()
TRIP_ID = str(uuid.uuid4())


@pytest.mark.skip(reason="database interaction")
def test_registry_email() -> None:
    """
    A test function that registers an email activity. It initializes a connection,
    creates activity information, and calls the registry_activity function.
    """
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    activity = {
        "id": str(uuid.uuid4()),
        "trip_id": TRIP_ID,
        "title": "atividade",
        "occurs_at": datetime.strptime("30-07-2024", "%d-%m-%Y"),
    }
    activities_repository.registry_activity(activity_infos=activity)


@pytest.mark.skip(reason="database interaction")
def test_find_emails_from_trip() -> None:
    """
    A test case that skips due to database interaction. It initializes connection,
    retrieves activities associated with a specific trip ID, and prints the result.

    Returns:
        None
    """
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    emails_to_invite = activities_repository.find_activities_from_trip(trip_id=TRIP_ID)
    print(emails_to_invite)
