import random

class Birthday:
    # Setting default variables
    num_people = 23
    num_rolls = 10
    days = 365
    include_29_feb = False

    def simulation(self):
        t = 0
        all_rolls = 0

        # Rolling num_rolls times and checking for common birthdays
        for _ in range(self.num_rolls):
            all_rolls += 1
            birthdays = [random.randint(1, self.days) for _ in range(self.num_people)]

            if len(set(birthdays)) < len(birthdays):
                t += 1
        return f"Chance of at least two people sharing a birthday: {t * 100 / all_rolls}%"

    # Changing default variables
    def change_people(self, num_people):
        self.num_people = num_people

    def change_rolls(self, num_rolls):
        self.num_rolls = num_rolls

    # Getting info and command list
    @property
    def info(self):
        return f"People: {self.num_people}\nRolls: {self.num_rolls}\n29th February included: {self.include_29_feb}"

    @property
    def list_of_commands(self):
        return ("COMMANDS:\n"
                "- 29Feb\n"
                "- change_people\n"
                "- change_rolls\n"
                "- exit\n"
                "- help\n"
                "- info\n"
                "- sim")
    # Additional features
    @property
    def include29feb(self):
        self.include_29_feb = not self.include_29_feb
        if self.include_29_feb:
            self.days = 366
        else:
            self.days = 365
        return self.include_29_feb

# Class for Infinite Monkey Theorem
class Monkey:
    # Default variables
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = "a"
    tries = 0

    def simulation(self):
        monkey_typing = ''.join(random.choices(self.alphabet, k=len(self.word)))
        percentage = 1 / pow(len(self.alphabet), len(self.word)) * 100
        while monkey_typing != self.word:
            print(f"{monkey_typing}   |   Try #{self.tries}   |   Percentage {percentage}")
            monkey_typing = ''.join(random.choices(self.alphabet, k=len(self.word)))
            self.tries += 1
        print(f"{monkey_typing}   |   Try #{self.tries}   |   Percentage {percentage}")
        self.tries = 0

    @property
    def list_of_commands(self):
        return f"\n-    help\n-    new_word\n-    sim"

    def new_word(self, w):
        self.word = w.lower().strip()


birthday = Birthday()
monkey = Monkey()

# Main
while True:
    sim = ""
    com = ""
    try:
        command = input("Command: ").split()
        sim, com = command
    except ValueError:
        print("Invalid input.")

    try:
        if sim in ["birthday", "b"] and com in ["sim", ""]:
            print(birthday.simulation())
        elif sim in ["birthday", "b"] and com == "change_people":
            change = int(input("People: "))
            birthday.change_people(change)
        elif sim in ["birthday", "b"] and com == "change_rolls":
            change = int(input("Rolls: "))
            birthday.change_rolls(change)
        elif sim in ["birthday", "b"] and com == "info":
            print(birthday.info)
        elif sim in ["birthday", "b"] and com == "help":
            print(birthday.list_of_commands)
        elif sim in ["birthday", "b"] and com == "29Feb":
            print(birthday.include29feb)

        elif sim in ["monkey", "m"] and com == "sim":
            monkey.simulation()
        elif sim in ["monkey", "m"] and com == "help":
            print(monkey.list_of_commands)
        elif sim in ["monkey", "m"] and com == "new_word":
            word = ""
            while not word.isalpha():
                word = str(input("Word: "))
            monkey.new_word(word)

        elif sim == "" and com == "exit":
            break
        print()
    except ValueError:
        print(f"Invalid input.\n{birthday.list_of_commands}\n")
