from app.enums.output_enums import OutputEnums
from app.fizz_buzz import FizzBuzz


def test_process_integers():
    fizz_buzz = FizzBuzz()
    result = fizz_buzz.process_integers(integer_one=2, integer_two=6)

    expected_output = [
        f"3, {OutputEnums.FIZZ}",
        f"5, {OutputEnums.BUZZ}",
        f"6, {OutputEnums.FIZZ}",
    ]

    assert result == expected_output
