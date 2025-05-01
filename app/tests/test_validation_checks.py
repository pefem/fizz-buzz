from app.fizz_buzz import FizzBuzz


def test_fizzbuzz_object():
    """
    Test will check that object is a valid FizzBuzz object
    """
    fizz_buzz = FizzBuzz()

    assert isinstance(fizz_buzz, FizzBuzz)


def test_check_entries_are_integers():
    """
    Test will check that entries are valid integers
    """
    fizz_buzz = FizzBuzz()
    result = fizz_buzz.check_entries_are_integers()

    assert result


def test_check_entries_are_btw_one_and_hundred():
    """
    Test will check that both entries are between 1 and 100
    """
    fizz_buzz = FizzBuzz()
    result = fizz_buzz.check_entries_are_btw_one_and_hundred()

    assert result


def test_check_second_entry_gt_first_entry():
    """
    Test will check that second entry is greater than the first
    """
    fizz_buzz = FizzBuzz()
    result = fizz_buzz.check_second_entry_gt_first_entry()

    assert result
