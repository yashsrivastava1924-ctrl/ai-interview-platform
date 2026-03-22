from flask import Flask, render_template
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# 👉 MAIN UI ROUTE
@app.route("/")
def home():
    return render_template("index.html")

# other pages
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# APIs
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(user_bp, url_prefix="/api/users")

if __name__ == "__main__":
    app.run(debug=True)