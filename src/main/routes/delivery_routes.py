from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest
#from src.main.http_types.http_response import HttpResponse


delivery_routs_bp = Blueprint("delivery_routs", __name__)

@delivery_routs_bp.route("/delivery/order", methods=['POST'])
def registry_order():
    print(request.json)
    http_request = HttpRequest(body= request.json)
    #http_response =
    print(http_request)
    return jsonify({"ola": "mundo"}), 200
