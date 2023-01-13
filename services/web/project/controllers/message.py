from flask import jsonify, make_response, request

from project.models.contact import Contact
from project.models.message import Message
from project.models.person import Person
from project.settings.constants import MESSAGE_FIELDS


def send_message():
    """
    Send message
    """
    data = request.get_json()
    # check all mandatory fields are present
    if list(data.keys()).sort() == MESSAGE_FIELDS.sort():
        sender_id = data.get('from_person_id')
        min_trust_level = data.get('min_trust_level')
        # get contacts by trust level
        contact_objs = Contact.query.filter(
            Contact.person_id == sender_id,
            Contact.trust_level >= min_trust_level
        ).all()
        recipient_contacts = []
        for c in contact_objs:
            # get contact info: topics, received messages
            c_obj = Person.query.filter_by(id=c.contact_id).first()
            c_topics = [t.id for t in c_obj.person_topic_xref]
            c_messages = [m.text for m in c_obj.messages_received]
            # filter contacts by topic and received messages
            recipient_contacts.extend(
                [c.contact_id
                 for t in data.get('topics')
                 if t in c_topics
                 and data.get('text') not in c_messages]
            )
        # create message
        for recipient_id in recipient_contacts:
            Message.create(
                text=data.get('text'),
                sender_id=sender_id,
                recipient_id=recipient_id
            )
        # create response body
        trust_connection = {sender_id: recipient_contacts}
        return make_response(jsonify(trust_connection), 201)

    else:
        err = 'All required fields should be specified'
        return make_response(jsonify(error=err), 400)
