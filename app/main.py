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


if __name__ == "__main__":
    main()
