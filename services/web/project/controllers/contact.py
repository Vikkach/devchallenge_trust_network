from collections import defaultdict
from flask import make_response, request, jsonify

from project.models.contact import Contact
from project.models.person import Person
from project.models.message import Message


def add_contact(person):
    """
    Add new person's contact
    """
    data = request.get_json()
    for c, tl in data.items():
        if tl < 1 or tl > 10:
            err = 'Trust level should be between 1 and 10'
            return make_response(jsonify(error=err), 400)
        if not Person.query.filter_by(id=c).first():
            err = 'Person is not exists'
            return make_response(jsonify(error=err), 400)
        if not (contact_r := Contact.query.filter_by(person_id=person, contact_id=c).first()):
            Contact.create(person_id=person, contact_id=c, trust_level=tl)
    return make_response({}, 201)


def find_path():
    """
    Find the shortest path
    """
    data = request.get_json()
    text = data.get('text')
    topics = data.get('topics')
    min_trust_level = data.get('min_trust_level')
    sender_id = data.get('from_person_id')

    filtered_contacts = filter_contacts(min_trust_level)
    # Breadth First Search
    visited = []
    queue = []
    path = []

    def bfs(visited, graph, node):
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            path.append(s)

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    bfs(visited, filtered_contacts, sender_id)
    final_path = []
    # filter path results
    for i, p_id in enumerate(path):
        if p_id == sender_id:
            continue
        else:
            person = Person.query.filter_by(id=p_id).first()
            p_topics = set([t.id for t in person.person_topic_xref])
            messages_received = [m.text for m in person.messages_received]
            if set(topics).issubset(p_topics) and text not in messages_received:
                final_path = path[1:i + 1]
                Message.create(
                    text=data.get('text'),
                    sender_id=sender_id,
                    recipient_id=p_id
                )
                break
    body = {
        'from': sender_id,
        'path': final_path
    }
    return make_response(jsonify(body), 201)


def filter_contacts(min_trust_level):
    hash_t = defaultdict(list)
    trusted_contacts = Contact.query.filter(
        Contact.trust_level >= min_trust_level
    ).all()
    for c in trusted_contacts:
        if not hash_t.get(c.person_id):
            hash_t[c.person_id] = []
        hash_t[c.person_id].append(c.contact_id)
    return hash_t
