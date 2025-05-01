import logging
from typing import List

logging.basicConfig(level=logging.INFO)


class FizzBuzz:
    def __init__(
        self,
    ) -> None:
        pass

    @staticmethod
    def check_entries_are_integers(
        first_entry: str, second_entry: str
    ) -> List[int] | bool:
        """
        This function takes in both entries are tries to convert them to integers
        """

        integer_entries = []

        for entry in [first_entry, second_entry]:
            try:
                value = int(entry)
                integer_entries.append(value)
            except ValueError:
                logging.error("invalid entry %s", entry)
                return False

        return integer_entries
