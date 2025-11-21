from flask import Blueprint, jsonify, current_app, request

route1 = Blueprint("route1", __name__)

# 1️⃣ Route1 calls Route2 /multiply
@route1.route("/route1-call-multiply", methods=["GET"])
def route1_call_multiply():
    with current_app.test_client() as client:
        response = client.post("/multiply", json={"a": 5, "b": 6})
        data = response.get_json()

    return jsonify({
        "message": "Route1 called Route2 Multiply API",
        "multiply_result": data["result"]
    }), 200


# 2️⃣ Route1 calls Route2 /add
@route1.route("/route1-call-add", methods=["GET"])
def route1_call_add():
    with current_app.test_client() as client:
        response = client.post("/add", json={"a": 3, "b": 4})
        data = response.get_json()

    return jsonify({
        "message": "Route1 called Route2 Add API",
        "add_result": data["result"]
    }), 200
# Route1 internal route (used by Route2)
@route1.route("/route1-internal-add", methods=["GET"])
def route1_internal_add():
    a = 10
    b = 15
    result = a + b
    return jsonify({"value": result})
