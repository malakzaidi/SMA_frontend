import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from src.routes.user import user_bp
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 86400  # 24 hours

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
