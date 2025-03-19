# Dicer

This Python script simulates rolling various types of dice and calculates the totals. It allows users to input dice roll commands in a simple format and displays the results with formatted numbers for easy reading.

## Features

* **Multiple Dice Types:** Supports standard dice types: d2, d3, d4, d6, d8, d10, d12, d20, and d100.
* **Multiple Rolls:** Allows rolling multiple dice of different types in a single command.
* **Input Validation:** Checks for valid dice types and input formats.
* **Clear Output:** Displays individual roll results, category totals, and a grand total.
* **Number Formatting:** Large numbers are formatted with commas for easy readability (e.g., 1,000,000).
* **Exit Functionality:** Type `exit` to end the program.

## Usage

1.  **Run the script:**
    ```bash
    python dicer.py
    ```
2.  **Enter dice roll commands:**
    * Use the format `NdM`, where `N` is the number of dice to roll and `M` is the type of dice (e.g., `2d20` for two 20-sided dice).
    * Separate multiple dice roll commands with spaces (e.g., `2d20 10d6 4d4`).
3.  **View the results:**
    * The script will display the individual roll results for each dice type, the total for each dice category, and the grand total.
4.  **Exit the program:**
    * Type `exit` and press Enter.

## Example
Enter dice rolls (e.g., 2d20 10d6 4d4) or type 'exit': 2d20 3d6
2d20: [15, 8]
3d6: [6, 2, 4]
2d20 Total: 23
3d6 Total: 12
Grand Total: 35

Enter dice rolls (e.g., 2d20 10d6 4d4) or type 'exit': 1000d100
1000d100: [ ... (1000 random numbers between 1 and 100) ... ]
1000d100 Total: 50,450
Grand Total: 50,450

Enter dice rolls (e.g., 2d20 10d6 4d4) or type 'exit': exit

## Code Explanation

* **`roll_dice(dice_string)`:**
    * Parses the input string to extract dice roll commands.
    * Validates dice types and performs the dice rolls using `random.randint()`.
    * Returns a dictionary containing the results of each dice roll.
* **`get_user_input()`:**
    * Prompts the user to enter dice roll commands.
    * Validates the input format using regular expressions.
    * returns None if the user types exit.
* **`format_number(number)`:**
    * Takes an integer and returns a string with commas for thousands.
* **`main()`:**
    * Manages the main program loop.
    * Calls `get_user_input()` to get user input.
    * Calls `roll_dice()` to perform the dice rolls.
    * Formats and displays the results.

## Requirements

* Python 3.x

## Installation

1.  Save the code as `dicer.py`.
2.  Ensure you have Python 3 installed.

## Author

[Kodyzz1](https://www.github.com/Kodyzz1)

## Link to this project
[Github - Dicer](https://www.github.com/Kodyzz1/Dicer)

## License

This project is licensed under the MIT License.
