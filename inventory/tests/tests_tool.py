import pytest

from inventory.tests.fixtures import fixture_tools
from staff.tests.fixtures import fixture_staff
from util.config_test import create_user, get


@pytest.mark.django_db
def test_get_tool(fixture_tools):
    usuario = create_user(username='admin')

    response = get(url="/api/v1/tools/", user_logged=usuario)
    json_data = response.json()
    count = json_data['count']

    assert response.status_code == 200
    assert count == 3


@pytest.mark.django_db
def test_filter_name_tool(fixture_tools):
    usuario = create_user(username='admin')
    pala, picota, machete = fixture_tools

    response = get(url=f"/api/v1/tools/?name={pala.name}", user_logged=usuario)
    json_data = response.json()
    count = json_data['count']
    results = json_data['results']

    assert response.status_code == 200
    assert count == 1
    assert results[0].get('name') == pala.name
    assert results[0].get('codigo') == pala.codigo


@pytest.mark.django_db
def test_filter_codigo_tool(fixture_tools):
    usuario = create_user(username='admin')
    pala, picota, machete = fixture_tools

    response = get(url=f"/api/v1/tools/?codigo={picota.codigo}", user_logged=usuario)
    json_data = response.json()
    count = json_data['count']
    results = json_data['results']

    assert response.status_code == 200
    assert count == 1
    assert results[0].get('name') == picota.name
    assert results[0].get('codigo') == picota.codigo


@pytest.mark.django_db
def test_filter_state_tool(fixture_tools):
    usuario = create_user(username='admin')
    pala, picota, machete = fixture_tools

    picota.state = False
    picota.save()

    response = get(url=f"/api/v1/tools/?state=false", user_logged=usuario)
    json_data = response.json()
    count = json_data['count']
    results = json_data['results']

    assert response.status_code == 200
    assert count == 1
    assert results[0].get('name') == picota.name
    assert results[0].get('codigo') == picota.codigo
    assert results[0].get('state') == picota.state
