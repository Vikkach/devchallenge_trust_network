import pytest
import requests

PEOPLE_ROUTE = 'http://127.0.0.1:8080/api/people'


@pytest.mark.parametrize(
    ('body', 'expected_response'),
    [
        (dict(id='Garry'), 201),
    ]
)
def test_add_person(body, expected_response):
    response = requests.post(PEOPLE_ROUTE, json=body)
    assert response.status_code == expected_response, response.text
