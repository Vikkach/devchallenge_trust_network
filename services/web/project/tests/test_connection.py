import pytest
import requests

from models.person import Person

CONNECTION_ROUTE = 'http://127.0.0.1:8080/api/people/Garry/trust_connections'


@pytest.fixture()
def create_person():
    Person.create(id='Garry')


@pytest.mark.parametrize(
    ('body', 'expected_response'),
    [
        (dict(Snape=4, Voldemort=1), 201),
        (dict(Ron=10, Hermione=10), 201)
    ]
)
def test_add_connection(body, expected_response):
    response = requests.post(CONNECTION_ROUTE, json=body)
    assert response.status_code == expected_response, response.text
