from project.core import db
from project.models.base import Model


class Contact(Model, db.Model):
    __tablename__ = 'contact'

    person_id = db.Column(db.String, db.ForeignKey('person.id'), primary_key=True, nullable=False)
    contact_id = db.Column(db.String, db.ForeignKey('person.id'), primary_key=True, nullable=False)
    trust_level = db.Column(db.Integer)
