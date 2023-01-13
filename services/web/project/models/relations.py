from project.core import db

person_topic_xref = db.Table(
    'person_topic_xref',
    db.Column('person_id', db.String, db.ForeignKey('person.id')),
    db.Column('topic_id', db.String, db.ForeignKey('topic.id'))
)
