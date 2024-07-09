import uuid

import pytest

from src.models.settings.db_connection_handler import db_connection_handler

from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
TRIP_ID = str(uuid.uuid4())


@pytest.mark.skip(reason="database interaction")
def test_registry_email() -> None:
    """
    A test case that skips due to database interaction. It initializes connection,
    creates email information, and calls the registry_email function.
    """
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    emails_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": TRIP_ID,
        "email": "higorrsc@gmail.com",
    }
    emails_to_invite_repository.registry_email(email_infos=emails_trips_infos)


@pytest.mark.skip(reason="database interaction")
def test_find_emails_from_trip() -> None:
    """
    A test case that skips due to database interaction. It initializes connection,
    retrieves emails associated with a specific trip ID, and prints the result.
    """
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    emails_to_invite = emails_to_invite_repository.find_emails_from_trip(
        trip_id=TRIP_ID
    )
    print(emails_to_invite)
