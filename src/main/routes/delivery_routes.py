from flask import Blueprint, jsonify, request


delivery_routs_bp = Blueprint("delivery_routs", __name__)

@delivery_routs_bp.route("/delivery/order", methods=['POST'])
def registry_order():
    print(request.json)
    return jsonify({"ola": "mundo"}), 200
