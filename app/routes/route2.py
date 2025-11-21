from flask import Blueprint, jsonify, request, current_app

route2 = Blueprint("route2", __name__)

# Main APIs
@route2.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    return jsonify({"result": data["a"] + data["b"]}), 200


@route2.route("/multiply", methods=["POST"])
def multiply_numbers():
    data = request.get_json()
    return jsonify({"result": data["a"] * data["b"]}), 200


@route2.route("/divide", methods=["POST"])
def divide_numbers():
    data = request.get_json()
    if data["b"] == 0:
        return jsonify({"error": "Cannot divide"}), 400
    return jsonify({"result": data["a"] / data["b"]}), 200


# Reverse communication
# 3️⃣ Route2 calls Route1’s add → route1 will handle /route1-internal-add
@route2.route("/route2-call-add", methods=["GET"])
def route2_call_add():
    with current_app.test_client() as client:
        response = client.get("/route1-internal-add")
        data = response.get_json()

    return jsonify({
        "message": "Route2 called Route1 internal route",
        "add_result": data["value"]
    }), 200
