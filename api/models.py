from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PatientModel(db.Model)