from project.core import db
from project.models.base import Model


class Topic(Model, db.Model):
    __tablename__ = 'topic'

    id = db.Column(db.String, unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return '<Topic {}>'.format(self.id)
