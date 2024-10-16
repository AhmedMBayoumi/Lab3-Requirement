from flask import Flask
from routes.device_routes import device_routes

app = Flask(__name__)
# Register blueprints (routes)
app.register_blueprint(device_routes)
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
