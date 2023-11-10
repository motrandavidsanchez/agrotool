import pytest

from inventory.models import Tool, Supplies
from staff.tests.fixtures import fixture_staff


@pytest.fixture
def fixture_tools(fixture_staff):
    david, messi, biza = fixture_staff

    pala = Tool.objects.create(name='pala', codigo=1283, state=True)
    picota = Tool.objects.create(name='picota', codigo=4858, state=False, owner=david)
    machete = Tool.objects.create(name='machete', codigo=9846, state=True)

    return pala, picota, machete


@pytest.fixture
def fixture_supplies():
    fertilizante = Supplies.objects.create(name='Fertilizante', codigo=1283)
    abono = Supplies.objects.create(name='Abono', codigo=4858)
    insecticida = Supplies.objects.create(name='Insecticida', codigo=9846)

    return fertilizante, abono, insecticida
