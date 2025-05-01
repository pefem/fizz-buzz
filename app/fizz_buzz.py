import logging
from typing import List

from app.enums.output_enums import OutputEnums

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

    @staticmethod
    def check_entries_are_btw_one_and_hundred(
        integer_one: int, integer_two: int
    ) -> List[int] | bool:
        """
        Function will take in two integers and confirm if they are between 1 and 100
        """

        integer_entries = []

        for integer in [integer_one, integer_two]:
            if 1 < integer < 100:
                integer_entries.append(integer)
            else:
                logging.error("integer: %s is not within the expected range", integer)
                return False

        return integer_entries

    @staticmethod
    def check_second_int_gt_first_int(
        integer_one: int, integer_two: int
    ) -> List[int] | bool:
        """
        Function will check if the second integer is less than the first
        """
        # perhaps this does not need to be fixed integers can be sorted in ascending order to ensure the first is always smaller

        if integer_one >= integer_two:
            logging.error("Second integer must be greater than the first")
            return False

        return [integer_one, integer_two]

    def process_integers(self, integer_one: int, integer_two: int) -> List[str]:
        """
        Function processes integers and prints out the required output if the condition is met
        """

        results = []

        for integer in range(integer_one, integer_two + 1):
            logging.info(integer)

            if integer % 3 == 0:
                output = f"{integer}, {OutputEnums.FIZZ}"
                print(output)
                results.append(output)

            if integer % 5 == 0:
                output = f"{integer}, {OutputEnums.BUZZ}"
                print(output)
                results.append(output)

        logging.info("Process Completed")
        return results
