import pytest

@pytest.fixture
def setup_teardown():
    print("Setup")
    yield
    print("Teardown")

def test_example(setup_teardown):
    assert 1 == 1
