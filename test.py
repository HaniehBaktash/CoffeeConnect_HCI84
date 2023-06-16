import csv
import tkinter as tk
from tkinter import ttk

# Read coffee options from a CSV file
def read_coffee_options(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        coffee_options = list(reader)
    return coffee_options

# Read coffee shops and their menus from a CSV file
def read_coffee_shops(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        coffee_shops = list(reader)
    return coffee_shops

class CoffeeConnectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Connect")

        # Create and configure GUI elements
        self.label = tk.Label(self.root, text="Welcome to Coffee Connect!")
        self.label.pack()

        self.button_explore = tk.Button(self.root, text="Explore Coffee Options", command=self.explore_coffee)
        self.button_explore.pack()

        self.button_create_account = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.button_create_account.pack()

        # Load coffee options and coffee shops
        self.coffee_options = read_coffee_options('coffee_options.csv')
        self.coffee_shops = read_coffee_shops('coffee_shops.csv')

    def explore_coffee(self):
        # Creating a new window for displaying coffee options
        window = tk.Toplevel(self.root)
        window.title("Coffee Options")

        # Display coffee options in a text box
        text_box = tk.Text(window, height=10, width=50)
        text_box.pack()
        print("Exploring coffee options...")

        # Add coffee options information to the text box
        for option in self.coffee_options:
            name = option['name']
            coffee_type = option['type']
            description = option['description']
            rating = option['rating']
            text_box.insert(tk.END, f"Name: {name}\n")
            text_box.insert(tk.END, f"Type: {coffee_type}\n")
            text_box.insert(tk.END, f"Description: {description}\n")
            text_box.insert(tk.END, f"Rating: {rating}\n")
            text_box.insert(tk.END, "----------------\n")

        # Disable editing in the text box
        text_box.configure(state='disabled')

    def create_account(self):
        # Creating a user account
        print("Creating a new account...")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeConnectApp(root)
    app.run()
