import pytest

from inventory.tests.fixtures import fixture_supplies
from util.config_test import create_user, get


@pytest.mark.django_db
def test_get_supplies(fixture_supplies):
    usuario = create_user(username='admin')

    response = get(url="/api/v1/supplies/", user_logged=usuario)
    json_data = response.json()
    count = json_data['count']

    assert response.status_code == 200
    assert count == 3


@pytest.mark.django_db
def test_filter_name_supplies(fixture_supplies):
    usuario = create_user(username='admin')
    fertilizante, abono, insecticida = fixture_supplies

    response = get(url=f"/api/v1/supplies/?name={insecticida.name}", user_logged=usuario)
    json_data = response.json()
    count = json_data['count']
    results = json_data['results']

    assert response.status_code == 200
    assert count == 1
    assert results[0].get('name') == insecticida.name
    assert results[0].get('codigo') == insecticida.codigo


@pytest.mark.django_db
def test_filter_codigo_supplies(fixture_supplies):
    usuario = create_user(username='admin')
    fertilizante, abono, insecticida = fixture_supplies

    response = get(url=f"/api/v1/supplies/?codigo={fertilizante.codigo}", user_logged=usuario)
    json_data = response.json()
    count = json_data['count']
    results = json_data['results']

    assert response.status_code == 200
    assert count == 1
    assert results[0].get('name') == fertilizante.name
    assert results[0].get('codigo') == fertilizante.codigo
