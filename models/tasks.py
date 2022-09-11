from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class tasks(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    modification_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    completed = db.Column(db.Integer, default=0)

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        

    def __str__(self):
        return "\nNombre: {}. Description: {}. Completed: {}. Modification date: {}. \n".format(
            self.name,
            self.description,
            self.completed,
            self.modification_date
        )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "modification_date": self.modification_date,
            "completed": self.completed
        }