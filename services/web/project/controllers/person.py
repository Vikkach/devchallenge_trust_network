from flask import jsonify, make_response, request

from project.models.person import Person
from project.models.topic import Topic
from project.settings.constants import PERSON_FIELDS


def add_person():
    """
    Add new person
    """
    data = request.get_json()
    topics = data.get('topics')
    # create person
    if not (person_record := Person.query.filter_by(id=data.get('id')).first()):
        person_record = Person.create(id=data.get('id'))
    # create person's topics
    if topics:
        for topic in topics:
            # create topic
            if not (topic_record := Topic.query.filter_by(id=topic).first()):
                topic_record = Topic.create(id=topic)
            Person.add_person_topic_xref(person_record.id, topic_record)
    # create response body
    new_person = {k: v for k, v in data.items() if k in PERSON_FIELDS}
    return make_response(jsonify(new_person), 201)
