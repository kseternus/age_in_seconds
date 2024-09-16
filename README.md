This Python program calculates your exact age in seconds based on the birthdate and time provided by the user.<br />
The program takes input in the format DD-MM-YYYY-HH-MM (Day-Month-Year-Hour-Minute) and uses that to compute the total time that has passed in seconds from your birth until the current moment.<br />
Features:<br />

    Input Format: Users can enter their birthdate and time in a single input using the format DD-MM-YYYY-HH-MM. The program splits this input and extracts the day, month, year, hour, and minute.

    Class Structure: The code is structured using an AgeCalculator class that organizes the logic, making the program modular and easier to maintain or expand.

    Time Calculation:
        The program computes the age by subtracting the birthdate (including time) from the current time, using Python's datetime module.
        It then converts the difference (a timedelta object) into seconds, providing an accurate and detailed result of the user's age down to the exact second.

    Output:
        The program displays the entered birthdate in a readable format (YYYY-MM-DD HH:MM).
        It also displays the current time at the moment of execution.
        Finally, the program calculates and outputs the total number of seconds that have passed since the birthdate.

Example Use Case:<br />

When the user inputs 17-05-1990-12-30, the program will:<br />

    Parse this as 17th May 1990, 12:30 PM.
    Calculate the age in seconds from that time until the current time.
    Display the calculated age, birthdate, and current time.

This is useful for anyone curious about their exact age in seconds or for fun trivia!<br />
![Zrzut ekranu 2024-09-16 132603](https://github.com/user-attachments/assets/8c7419e4-898b-4552-849f-570fe825a48c)
