import csv
import tkinter as tk
from tkinter import ttk

# Create a Scrollable Frame class
class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

# Read coffee data from a CSV file
def read_coffee_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        coffee_data = list(reader)
        print("Data read from CSV file:", coffee_data)
        return coffee_data

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

        # Load coffee data
        self.coffee_data = read_coffee_data('coffee_data.csv')

    def explore_coffee(self):
        # Creating a new window for displaying coffee options
        window = tk.Toplevel(self.root)
        window.title("Coffee Options")

        scrollable_frame = ScrollableFrame(window)
        scrollable_frame.pack()

        print("Exploring coffee options...")

        # Add coffee options information to the text box
        for data in self.coffee_data:
            print("Current data:", data)
            shop_name = data['shop_name']
            shop_address = data['shop_address']
            name = data['name']
            coffee_type = data['type']
            description = data['description']
            rating = data['rating']
            brand = data['brand']
            ingredient = data['ingredient']
            image_file = data['image']

            # I decided to create a sub frame for each coffee option
            sub_frame = ttk.Frame(scrollable_frame.scrollable_frame)
            sub_frame.pack(pady=10)

            # Display coffee options in a text box
            text_box = tk.Text(sub_frame, height=10, width=50)
            text_box.pack(side="left")

            text_box.insert(tk.END, f"Shop Name: {shop_name}\n")
            text_box.insert(tk.END, f"Shop Address: {shop_address}\n")
            text_box.insert(tk.END, f"Name: {name}\n")
            text_box.insert(tk.END, f"Type: {coffee_type}\n")
            text_box.insert(tk.END, f"Description: {description}\n")
            text_box.insert(tk.END, f"Rating: {rating}\n")
            text_box.insert(tk.END, f"Brand: {brand}\n")  
            text_box.insert(tk.END, f"Ingredient: {ingredient}\n")
            text_box.insert(tk.END, "----------------\n")

            # Disable editing in the text box
            text_box.configure(state='disabled')

            # Display the image I am trying to display an image for each coffee, i couldnt so far!
            image = tk.PhotoImage(file=image_file)
            image_label = tk.Label(sub_frame, image=image)
            image_label.image = image  # Keep a reference to the image object to prevent it from being garbage collected
            image_label.pack(side="right")

    def create_account(self):
        # Creating a user account I will work on this part more.
        print("Creating a new account...")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeConnectApp(root)
    app.run()
