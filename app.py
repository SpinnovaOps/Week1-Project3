from datetime import timedelta, datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from io import BytesIO
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = b"qwiuf8427348cy4tyc3ty32!&$#*@("
app.permanent_session_lifetime = timedelta(seconds=30)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Initialize SQLAlchemy after app configuration
db = SQLAlchemy(app)

# Define models (unchanged)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    messages = db.relationship('Message', backref='receiver', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(200), nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(150), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)

# ----- Routes (unchanged except for removing the db.create_all() from here) -----
# ... (rest of your routes remain the same) ...

# ----- Session Timeout (unchanged) -----
# ... (session timeout code remains the same) ...

# Create database tables *after* model definitions.  This is crucial!
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
