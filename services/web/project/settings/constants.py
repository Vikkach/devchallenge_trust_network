import os

DATABASE_URL = os.environ['DATABASE_URL']
FLASK_HOST = os.environ['FLASK_HOST']
FLASK_PORT = os.environ['FLASK_PORT']
# entities properties
PERSON_FIELDS = ['id', 'topics']
TOPIC_FIELDS = ['id']
MESSAGE_FIELDS = ['text', 'topics', 'from_person_id', 'min_trust_level']