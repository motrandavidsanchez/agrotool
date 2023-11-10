import pytest

from util.config_test import create_user, post, get
from staff.tests.fixtures import fixture_staff


@pytest.mark.django_db
def test_post_and_get_staff(fixture_staff):
    usuario = create_user(username='admin')

    data = {
        "name": "Charly",
        "last_name": "Garcia",
        "dni": "16253456",
    }

    response_post = post(url=f"/api/v1/staff/", data=data, user_logged=usuario)
    json_data_post = response_post.json()

    assert response_post.status_code == 201
    assert json_data_post.get('name') == data.get("name")
    assert json_data_post.get('last_name') == data.get("last_name")
    assert json_data_post.get('dni') == data.get("dni")

    response_get = get(url=f"/api/v1/staff/", user_logged=usuario)
    json_data_get = response_get.json()
    count = json_data_get['count']

    assert response_get.status_code == 200
    assert count == 4
