from flask import Flask
from flask_cors import CORS
from routers.auth_routes import auth_bp
from routers.user_routes import user_bp

app = Flask(__name__)
CORS(app)

# register routes
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(user_bp, url_prefix="/api/users")

if __name__ == "__main__":
    app.run(debug=True, port=5000)