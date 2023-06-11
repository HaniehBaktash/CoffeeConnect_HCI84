

# Some sample data about coffe options
coffee_options = [
    {
        'name': 'Cappuccino',
        'type': 'Espresso',
        'description': 'A traditional Italian coffee drink.',
        'rating': 4.5
    },
    {
        'name': 'Latte',
        'type': 'Espresso',
        'description': 'A coffee drink made with espresso and steamed milk.',
        'rating': 4.2
    },
    {
        'name': 'Mocha',
        'type': 'Espresso',
        'description': 'A chocolate-flavored coffee drink.',
        'rating': 4.0
    }
]

import tkinter as tk

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

    def explore_coffee(self):
        # exploring coffee options
        
        print("Exploring coffee options...")

    def create_account(self):
        # creating a user account
        print("Creating a new account...")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeConnectApp(root)
    root.mainloop()


    


