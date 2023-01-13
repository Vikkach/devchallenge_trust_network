from datetime import datetime

from project.core import db
from project.models.base import Model
from project.models.message import Message
from project.models.relations import person_topic_xref


class Person(Model, db.Model):
    __tablename__ = 'person'

    id = db.Column(db.String, primary_key=True, unique=True, nullable=False)

    person_topic_xref = db.relationship(
        'Topic',
        secondary=person_topic_xref,
        backref='person_topic_xref'
    )

    messages_received = db.relationship(
        'Message',
        foreign_keys='Message.recipient_id',
        backref='recipient', lazy='dynamic'
    )

    def __repr__(self):
        return '<Person {}>'.format(self.id)

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()
