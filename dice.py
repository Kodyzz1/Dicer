import random
import re

def roll_dice(dice_string):
    """Simulates rolling multiple types of dice."""
    dice_rolls = {}
    dice_patterns = re.findall(r'(\d+)d(\d+)', dice_string.lower())

    if not dice_patterns:
        return "Invalid dice string."

    for num_rolls, dice_type in dice_patterns:
        num_rolls = int(num_rolls)
        dice_type = int(dice_type)

        if dice_type not in [2, 3, 4, 6, 8, 10, 12, 20, 100]:
            return f"Invalid dice type: d{dice_type}"

        results = []
        for _ in range(num_rolls):
            roll = random.randint(1, dice_type)
            results.append(roll)
        dice_rolls[f"{num_rolls}d{dice_type}"] = results

    return dice_rolls

def get_user_input():
    """Gets user input for dice rolls."""
    while True:
        dice_string = input("Enter dice rolls (e.g., 2d20 10d6 4d4) or type 'exit': ").lower()
        if dice_string == 'exit':
            return None
        if re.match(r'^(\d+d\d+\s*)+$', dice_string):
            return dice_string
        else:
            print("Invalid input. Please use the format 'NdM' (e.g., 2d20) separated by spaces.")

def format_number(number):
    """Formats a number with commas for thousands."""
    return "{:,}".format(number)

def main():
    """Main function to run the dice roller."""
    while True:
        dice_string = get_user_input()
        if dice_string is None:
            break

        results = roll_dice(dice_string)

        if isinstance(results, str):
            print(results)
            continue

        total_sum = 0
        dice_category_totals = {}  # Store totals for each dice category

        for dice_type, rolls in results.items():
            print(f"{dice_type}: {rolls}")
            category_total = sum(rolls)
            dice_category_totals[dice_type] = category_total
            total_sum += category_total

        for category, category_total in dice_category_totals.items():
            print(f"{category} Total: {format_number(category_total)}")

        print(f"Grand Total: {format_number(total_sum)}")

if __name__ == "__main__":
    main()