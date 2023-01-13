from flask import current_app as app

from project.controllers.contact import add_contact, find_path
from project.controllers.message import send_message
from project.controllers.person import *


@app.route('/api/people', methods=['POST'])
def people():
    """
    Create person
    """
    return add_person()


@app.route('/api/people/<person>/trust_connections', methods=['POST'])
def trust_connection(person):
    """
    Create person's contact
    """
    return add_contact(person)


@app.route('/api/messages', methods=['POST'])
def messages():
    """
    Send message
    """
    return send_message()


@app.route('/api/path', methods=['POST'])
def path():
    """
    Send message
    """
    return find_path()
