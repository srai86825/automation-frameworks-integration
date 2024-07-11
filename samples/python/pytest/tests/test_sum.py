import pytest

def test_sum_two_numbers(record_property):
    # Adding a subid for the test case
    record_property("subid", "JE21")
    assert 1 + 1 == 2

def test_sum_two_decimals(record_property):
    # Adding a subid for the test case
    record_property("subid", "JE20")
    assert 0.8 + 0.3 == 1.2
    # assert 0.8 + 0.3 == 1.1

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6)])
def test_sum_multiple_numbers(record_property, test_input, expected):
    # Adding a subid for the test case
    record_property("subid", "JE22")
    assert eval(test_input) == expected
