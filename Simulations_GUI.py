import random
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simulations")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

class Birthday:
    def __init__(self):
        self.num_people = 23
        self.num_rolls = 10
        self.days = 365
        self.include_29_feb = tk.IntVar()

    def simulation(self):
        t = 0
        all_rolls = 0

        for _ in range(self.num_rolls):
            all_rolls += 1
            birthdays = [random.randint(1, self.days) for _ in range(self.num_people)]

            if len(set(birthdays)) < len(birthdays):
                t += 1
        sim_results.config(text=f"Chance: {(t / all_rolls) * 100:.2f}%")

    def change_people(self, event=None):
        num = set_people.get().strip()
        if num.isdigit():
            self.num_people = int(num)
            people.config(text=f"People: {self.num_people}")
            set_people.delete(0, tk.END)

    def change_rolls(self, event=None):
        num = set_rolls.get().strip()
        if num.isdigit():
            self.num_rolls = int(num)
            rolls.config(text=f"Rolls: {self.num_rolls}")
            set_rolls.delete(0, tk.END)

    def include29feb(self):
        self.days = 366 if self.include_29_feb.get() else 365

class Monkey:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.word = "a"
        self.tries = 0
        self.process = tk.IntVar()

    def simulation(self):
        self.tries = 1
        monkey_typing = ''.join(random.choices(self.alphabet, k=len(self.word)))
        monkey_typing_history.delete(0, tk.END)

        while monkey_typing != self.word:
            if self.process.get():
                monkey_typing_history.insert(tk.END, f"{monkey_typing}   |   Try #{self.tries}")
            monkey_typing = ''.join(random.choices(self.alphabet, k=len(self.word)))
            self.tries += 1

        monkey_typing_history.insert(tk.END, f"{monkey_typing}   |   Try #{self.tries}")
        self.tries = 0

    def new_word(self, event=None):
        new_word = set_new_word.get()
        if new_word.isalpha():
            self.word = new_word
            percentage = 100 / pow(len(self.alphabet), len(self.word))
            percentage_of_typing.config(text=f"{percentage}%")

birthday = Birthday()
monkey = Monkey()

birthday_frame = ttk.Frame(root)
birthday_frame.grid(column=0, row=0, sticky="nsew", padx=15, pady=15)

birthday_frame.columnconfigure(0, weight=1)
birthday_frame.rowconfigure(0, weight=1)

monkey_frame = ttk.Frame(root)
monkey_frame.grid(column=0, row=1, sticky="nsew", padx=15, pady=15)

monkey_frame.columnconfigure(0, weight=1)
monkey_frame.rowconfigure(1, weight=1)

# Birthday widgets
bd_title = ttk.Label(birthday_frame, text="Birthday Paradox")
bd_title.grid(row=0, column=0, columnspan=2)

simulation_birthday_button = ttk.Button(birthday_frame, text="Simulation", command=birthday.simulation)
simulation_birthday_button.grid(row=1, column=1, sticky="ew")

sim_results = ttk.Label(birthday_frame, text="Chance: 0%")
sim_results.grid(row=1, column=0, sticky="ew")

people = ttk.Label(birthday_frame, text=f"People: {birthday.num_people}")
people.grid(row=2, column=0, sticky="ew")

rolls = ttk.Label(birthday_frame, text=f"Rolls: {birthday.num_rolls}")
rolls.grid(row=3, column=0, sticky="ew")

set_people = ttk.Entry(birthday_frame, width=5)
set_people.grid(row=2, column=1)
set_people.bind("<Return>", birthday.change_people)

set_rolls = ttk.Entry(birthday_frame, width=5)
set_rolls.grid(row=3, column=1)
set_rolls.bind("<Return>", birthday.change_rolls)

february_checkbox = ttk.Checkbutton(birthday_frame, text="Include 29th February", variable=birthday.include_29_feb, command=birthday.include29feb)
february_checkbox.grid(row=4, column=0, sticky="ew")

# Infinite Monkey Theorem widgets
imt_title = ttk.Label(monkey_frame, text="Infinite Monkey Theorem")
imt_title.grid(row=0, column=0, columnspan=2)

monkey_simulation_button = ttk.Button(monkey_frame, text="Simulation", command=monkey.simulation)
monkey_simulation_button.grid(row=1, column=1, sticky="ew")

show_process_checkbox = ttk.Checkbutton(monkey_frame, text="Show process", variable=monkey.process)
show_process_checkbox.grid(row=1, column=0, sticky="ew")

monkey_typing_history = tk.Listbox(monkey_frame)
monkey_typing_history.grid(row=2, column=0, sticky="nsew", columnspan=2, rowspan=2)

a_percentage = 100 / pow(len(monkey.alphabet), len(monkey.word))
percentage_of_typing = ttk.Label(text=f"{a_percentage}%")
percentage_of_typing.grid(row=3, column=0, sticky="ew")

set_new_word = tk.Entry()
set_new_word.grid(row=4, column=0, sticky="ew")
set_new_word.bind("<Return>", monkey.new_word)

root.mainloop()
