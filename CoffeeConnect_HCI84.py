

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
        # exploring coffee options by  creating a new window for displaying coffee options
        window = tk.Toplevel(self.root)
        window.title("Coffee Options")

        # Display coffee options in a text box
        text_box = tk.Text(window, height=10, width=50)
        text_box.pack()
        print("Exploring coffee options...")

        # add coffee options information to the text box

        for option in coffee_options:
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
        # creating a user account
        print("Creating a new account...")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeConnectApp(root)
    root.mainloop()


    


