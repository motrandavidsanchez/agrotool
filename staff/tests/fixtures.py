import pytest

from staff.models import Staff


@pytest.fixture
def fixture_staff():
    david = Staff.objects.create(name='David', last_name="Sanchez Motran", dni="39935311")
    messi = Staff.objects.create(name='Lionel', last_name="Messi", dni="37876354")
    biza = Staff.objects.create(name='Biza', last_name="Rap", dni="41345879")

    return david, messi, biza
