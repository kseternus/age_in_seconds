from datetime import datetime


class AgeCalculator:
    def __init__(self, day: int, month: int, year: int, hour: int = 0, minute: int = 0):
        """
        Initializes the AgeCalculator with a birthdate and optional time.

        :param day: Day of birth
        :param month: Month of birth
        :param year: Year of birth
        :param hour: Hour of birth (default is 0)
        :param minute: Minute of birth (default is 0)
        """
        self.birthdate = datetime(year, month, day, hour, minute)
        self.current_time = datetime.now()

    def calculate_age_in_seconds(self) -> int:
        """
        Calculates the age in seconds based on the birthdate and the current time.

        :return: Age in seconds
        """
        # Subtracts the birthdate from the current time to get a timedelta object
        age_timedelta = self.current_time - self.birthdate

        # Converts the timedelta to total seconds
        return int(age_timedelta.total_seconds())

    def display_birthdate(self):
        """
        Displays the user's birthdate in a readable format.
        """
        print(f'Your birthdate is: {self.birthdate.strftime("%Y-%m-%d %H:%M")}')

    def display_current_time(self):
        """
        Displays the current date and time.
        """
        print(f'Current time is: {self.current_time.strftime("%Y-%m-%d %H:%M:%S")}')


if __name__ == '__main__':
    # Get user input for the birthdate in the format DD-MM-YYYY-HH-MM
    birthdate_input = input('Enter your birthdate (DD-MM-YYYY-HH-MM): ').split('-')

    # Parse the input into day, month, year, hour, and minute
    day, month, year, hour, minute = map(int, birthdate_input)

    # Initialize the age calculator with the parsed birthdate
    age_calculator = AgeCalculator(day, month, year, hour, minute)

    # Display the birthdate and current time
    age_calculator.display_birthdate()
    age_calculator.display_current_time()

    # Calculate and print the age in seconds
    age_in_seconds = age_calculator.calculate_age_in_seconds()
    print(f'You are {age_in_seconds} seconds old.')
