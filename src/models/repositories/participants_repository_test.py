import uuid

import pytest

from src.models.settings.db_connection_handler import db_connection_handler

from .participants_repository import ParticipantsRepository


db_connection_handler.connect()
TRIP_ID = str(uuid.uuid4())
EMAIL_ID = str(uuid.uuid4())
PARTICIPANT_ID = str(uuid.uuid4())


@pytest.mark.skip(reason="database interaction")
def test_registry_participant() -> None:
    """
    A test case that skips due to database interaction. It initializes connection,
    creates participant information, and calls the registry_participant function.
    """
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    participant_infos = {
        "id": PARTICIPANT_ID,
        "trip_id": TRIP_ID,
        "emails_to_invite_id": EMAIL_ID,
        "name": "John Doe",
    }
    participants_repository.registry_participant(participant_infos=participant_infos)


@pytest.mark.skip(reason="database interaction")
def test_find_participants_from_trip() -> None:
    """
    A test case that skips due to database interaction. It initializes connection,
    retrieves participants associated with a specific trip ID, and prints the result.
    """
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    participants = participants_repository.find_participants_from_trip(trip_id=TRIP_ID)
    print(participants)


@pytest.mark.skip(reason="database interaction")
def test_update_participant_status() -> None:
    """
    A test case that updates the status of a participant in the database.
    It initializes connection, creates an instance of the ParticipantsRepository
    class, and calls the update_participant_status method with the provided participant_id.
    """
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    participants_repository.update_participant_status(participant_id=PARTICIPANT_ID)
