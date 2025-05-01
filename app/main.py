from fizz_buzz import FizzBuzz


def main():
    """
    Program entry point
    """

    first_entry = input("Enter first integer: ")
    second_entry = input("Enter second integer: ")

    fizz_buzz = FizzBuzz()

    values = fizz_buzz.check_entries_are_integers(
        first_entry=first_entry, second_entry=second_entry
    )
    values = fizz_buzz.check_entries_are_btw_one_and_hundred(
        integer_one=values[0], integer_two=values[1]
    )
    input(values)


if __name__ == "__main__":
    main()
