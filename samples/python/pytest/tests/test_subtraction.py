def test_subtract_two_numbers(record_property):
    # Adding a subid for the test case
    record_property("subid", "sub-101")
    assert 1 - 1 == 0
