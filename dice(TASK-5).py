import random

class DiceRoller:
    def __init__(self):
        self.roll_history = []

    def roll_dice(self, num_dice, num_sides):
        rolls = []
        for _ in range(num_dice):
            roll = random.randint(1, num_sides)
            rolls.append(roll)
        return rolls

    def roll(self, num_dice, num_sides, num_rolls):
        rolls = []
        for i in range(num_rolls):
            result = self.roll_dice(num_dice, num_sides)
            rolls.append(result)
            self.roll_history.append(result)
        return rolls

    def print_roll_history(self):
        print("\nRoll History:")
        for i, roll in enumerate(self.roll_history, start=1):
            print("Roll", i, ":", roll)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    dice_roller = DiceRoller()
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            if num_dice <= 0:
                print("Please enter a positive number of dice.")
                continue
            num_sides = int(input("Enter the number of sides on each die: "))
            if num_sides <= 0:
                print("Please enter a positive number of sides.")
                continue
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls <= 0:
                print("Please enter a positive number of rolls.")
                continue

            rolls = dice_roller.roll(num_dice, num_sides, num_rolls)
            print("\nRolling the dice...\n")
            for i, roll in enumerate(rolls, start=1):
                print("Roll", i, ":", roll)

            choice = input("Do you want to roll again? (yes/no): ").strip().lower()
            if choice != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    dice_roller.print_roll_history()

if __name__ == "__main__":
    main()
