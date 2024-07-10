from flask import Blueprint, jsonify, request

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivitiesFinder
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinksFinder
from src.controllers.participant_confirmer import ParticipantConfirmer
from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantsFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder

from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    """
    Creates a new trip by receiving a POST request at the '/trips' endpoint.

    This function handles the creation of a new trip by extracting the
    necessary information from the request body. It establishes a database
    connection, creates instances of the `TripsRepository` and
    `EmailsToInviteRepository` classes, and initializes a `TripCreator`
    object with these repositories. The `create` method of the `TripCreator`
    object is then called with the request body as an argument, and the response
    from the controller is stored in the `response` variable.

    Finally, the function returns a JSON response containing the body
    of the response and the status code of the response.

    Parameters:
        None

    Returns:
        A JSON response containing the body of the response and the status code of the response.
    """
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.get_json())

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    """
    Finds a trip by its ID and returns its details.

    Parameters:
        tripId (str): The ID of the trip to find.

    Returns:
        Tuple[Dict, int]: A tuple containing the trip details and the HTTP status code.
            - body (Dict): A dictionary containing the trip details.
                - id (str): The ID of the trip.
                - title (str): The title of the trip.
                - description (str): The description of the trip.
            - status_code (int): The HTTP status code of the response.
    """
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    """
    Confirm a trip with the given trip ID.

    This function is a route handler for the '/trips/<tripId>/confirm' endpoint. It is triggered when a GET request is made to this endpoint.

    Parameters:
        tripId (str): The ID of the trip to confirm.

    Returns:
        Tuple[Dict, int]: A tuple containing the response body and the HTTP status code.
            - body (Dict): A dictionary containing the response body.
            - status_code (int): The HTTP status code of the response.

    Raises:
        None

    Example:
        GET /trips/123456789/confirm
        Returns:
            {
                "body": {},
                "status_code": 204
            }
    """
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_link(tripId):
    """
    Creates a new link for a given trip.

    This function is a route handler for the '/trips/<tripId>/links' endpoint. It is triggered when a POST request is made to this endpoint. The function creates a new link for a given trip by extracting the necessary information from the request body. It establishes a database connection, creates instances of the `LinksRepository` class, and initializes a `LinkCreator` object with the repository. The `create` method of the `LinkCreator` object is then called with the request body and trip ID as arguments, and the response from the controller is stored in the `response` variable. Finally, the function returns a JSON response containing the body of the response and the status code of the response.

    Parameters:
        tripId (str): The ID of the trip for which the link is being created.

    Returns:
        Tuple[Dict, int]: A tuple containing the response body and the HTTP status code.
            - body (Dict): A dictionary containing the response body.
            - status_code (int): The HTTP status code of the response.

    Raises:
        None

    Example:
        POST /trips/123456789/links
        Request Body:
        {
            "url": "https://example.com",
            "title": "Example Link"
        }
        Returns:
            {
                "body": {
                    "linkId": "123456789"
                },
                "status_code": 201
            }
    """
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_link(tripId):
    """
    Finds a link associated with a given trip ID.

    Parameters:
        tripId (str): The ID of the trip to find the link.

    Returns:
        Tuple[Dict, int]: A tuple containing the response body and the HTTP status code.
            - body (Dict): A dictionary containing the response body.
                - linkId (str): The ID of the link.
                - tripId (str): The ID of the trip the link is associated with.
                - link (str): The link URL.
                - title (str): The link title.
            - status_code (int): The HTTP status code of the response.
    """
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinksFinder(links_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/invite", methods=["POST"])
def invite_to_trip(tripId):
    """
    Creates an invitation to a trip.

    Parameters:
        tripId (str): The ID of the trip to which the invitation is being sent.

    Returns:
        Tuple[Dict, int]: A tuple containing the response body and the HTTP status code.
            - body (Dict): A dictionary containing the response body.
            - status_code (int): The HTTP status code of the response.
    """
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)
    email_repository = EmailsToInviteRepository(conn)
    controller = ParticipantCreator(participant_repository, email_repository)

    response = controller.create(request.get_json(), tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def find_participants(tripId):
    """
    Retrieves the participants of a trip.

    Parameters:
        tripId (str): The ID of the trip.

    Returns:
        Tuple[Dict, int]: A tuple containing the response body and the HTTP status code.
            - body (Dict): A dictionary containing the response body.
            - status_code (int): The HTTP status code of the response.
    """
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantsFinder(participants_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route(
    "/trips/<tripId>/participants/<participantId>/confirm", methods=["PATCH"]
)
def confirm_participant(tripId, participantId):
    """
    Confirm the participation of a participant in a trip.

    Args:
        tripId (str): The ID of the trip.
        participantId (str): The ID of the participant.

    Returns:
        Tuple[Dict, int]: A tuple containing the response body and the HTTP status code.
            - body (Dict): A dictionary containing the response body.
            - status_code (int): The HTTP status code of the response.
    """
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmer(participant_repository)

    response = controller.confirm(participantId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    """
    Creates a new activity for a given trip.

    This function is a route handler for the '/trips/<tripId>/activities' endpoint.
    It is triggered when a POST request is made to this endpoint. The function
    initializes a database connection, creates an instance of the `ActivitiesRepository`
    class, and initializes an `ActivityCreator` object with the repository. The `create`
    method of the `ActivityCreator` object is then called with the request body and
    trip ID as arguments, and the response from the controller is stored in the `response`
    variable. Finally, the function returns a JSON response containing the body of the
    response and the status code of the response.

    Parameters:
        tripId (str): The ID of the trip for which the activity is being created.

    Returns:
        Tuple[Dict, int]: A tuple containing the response body and the HTTP status code.
            - body (Dict): A dictionary containing the response body.
            - status_code (int): The HTTP status code of the response.
    """
    conn = db_connection_handler.get_connection()
    activity_repository = ActivitiesRepository(conn)
    controller = ActivityCreator(activity_repository)

    response = controller.create(request.get_json(), tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def find_activities(tripId):
    """
    Finds activities associated with a given trip ID.

    Parameters:
        tripId (str): The ID of the trip to find activities for.

    Returns:
        Tuple[Dict, int]: A tuple containing the response body and the HTTP status code.
            - body (Dict): A dictionary containing the response body.
            - status_code (int): The HTTP status code of the response.
    """
    conn = db_connection_handler.get_connection()
    activity_repository = ActivitiesRepository(conn)
    controller = ActivitiesFinder(activity_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]
