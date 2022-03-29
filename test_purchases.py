import pytest
# implementation of setUp in pytest
@pytest.fixture()
def setUp():

    print("Setup started")
    yield
    print("Exited!")


def test_AddItemtoCart(setUp):
    print("Added successfully")


def test_RemoveItemfromCart(setUp):
    print("Removed successfully")


