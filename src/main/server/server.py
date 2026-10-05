from flask import Flask
from src.main.routes.delivery_routes import delivery_routs_bp

app = Flask(__name__)
app.register_blueprint(delivery_routs_bp)
