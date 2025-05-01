from app.fizz_buzz import FizzBuzz


def test_fizzbuzz_object():
    """
    Test will check that object is a valid FizzBuzz object
    """
    fizz_buzz = FizzBuzz()

    assert isinstance(fizz_buzz, FizzBuzz)


def test_check_valid_entries(valid_entries):
    """
    Test will check that entries can be converted to valid integers
    """
    fizz_buzz = FizzBuzz()
    result = fizz_buzz.check_entries_are_integers(
        first_entry=valid_entries[0], second_entry=valid_entries[1]
    )

    assert result
    assert isinstance(result, list)
    assert len(result) == 2


def test_check_invalid_entries(invalid_entries):
    """
    Test will check if entries are valid
    """
    fizz_buzz = FizzBuzz()
    result = fizz_buzz.check_entries_are_integers(
        first_entry=invalid_entries[0], second_entry=invalid_entries[1]
    )

    assert result is False


def test_check_entries_are_btw_one_and_hundred(valid_entries):
    """
    Test will check that both entries are between 1 and 100
    """

    int_one = int(valid_entries[0])
    int_two = int(valid_entries[1])

    fizz_buzz = FizzBuzz()
    result = fizz_buzz.check_entries_are_btw_one_and_hundred(
        integer_one=int_one, integer_two=int_two
    )

    assert result
    assert isinstance(result, list)
    assert len(result) == 2


def test_check_entries_that_are_not_btw_one_and_hundred(valid_entries):
    """
    Test will return false if entries are not within 1 and 100
    """

    valid_entries[1] = 150

    int_one = int(valid_entries[0])
    int_two = valid_entries[1]

    fizz_buzz = FizzBuzz()
    result = fizz_buzz.check_entries_are_btw_one_and_hundred(
        integer_one=int_one, integer_two=int_two
    )

    assert result is False


def test_check_second_entry_gt_first_entry():
    """
    Test will check that second entry is greater than the first
    """
    fizz_buzz = FizzBuzz()
    result = fizz_buzz.check_second_entry_gt_first_entry()

    assert result
