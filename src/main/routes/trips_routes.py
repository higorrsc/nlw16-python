from flask import Blueprint, jsonify, request

from src.controllers.link_creator import LinkCreator
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
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
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]
