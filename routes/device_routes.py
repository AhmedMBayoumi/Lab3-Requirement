from flask import Blueprint, jsonify, request
from middleware.middleware import authenticate_token

devices = [
    {"id": 1, "name": "Samsung Galaxy S24 Ultra", "category": "phone", "price": 1299.99},
    {"id": 2, "name": "Samsung Galaxy S24 Plus", "category": "phone", "price": 999.99},
    {"id": 3, "name": "Samsung Galaxy S24", "category": "phone", "price": 799.99},
    {"id": 4, "name": "Samsung Galaxy Tab S9", "category": "tablet", "price": 649.99},
]
device_routes = Blueprint('device_routes', __name__)

@device_routes.before_request
def before_request():
    authenticate_token()

@device_routes.route('/devices', methods=['GET'])
def get_devices():
    return jsonify({"devices": devices})

@device_routes.route('/devices/<int:id>', methods=['GET'])
def get_device(id):
    device = next((d for d in devices if d['id'] == id), None)
    if device:
        return jsonify(device)
    return jsonify({"error": "Device not found"}), 404

@device_routes.route('/devices', methods=['POST'])
def add_device():
    new_device = request.json
    new_device['id'] = len(devices) + 1
    devices.append(new_device)
    return jsonify(new_device), 201

@device_routes.route('/devices/<int:id>', methods=['PUT'])
def update_device(id):
    device = next((d for d in devices if d['id'] == id), None)
    if device:
        data = request.json
        device.update(data)
        return jsonify(device)
    return jsonify({"error": "Device not found"}), 404

@device_routes.route('/devices/<int:id>', methods=['DELETE'])
def delete_device(id):
    global devices
    devices = [d for d in devices if d['id'] != id]
    return jsonify({"message": "Device deleted"}), 200