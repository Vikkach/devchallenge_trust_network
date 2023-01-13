from datetime import datetime

from project.core import db
from project.models.base import Model


class Message(Model, db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    sender_id = db.Column(db.String, db.ForeignKey('person.id'), nullable=False)
    recipient_id = db.Column(db.String, db.ForeignKey('person.id'), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.text)
