import tkinter as tk
from tkinter import Tk, Canvas, Frame, Entry, Scrollbar, Button, Label, DoubleVar, StringVar, OptionMenu
from tkinter import VERTICAL, NSEW, NW
from PIL import Image, ImageTk
from PIL.Image import Resampling
import csv

class CoffeeConnect:
    def __init__(self, path_to_csv_file, image_folder="./image", width=200, height=200):
        # Initialize the CoffeeConnect object with CSV file path, image folder path, and image dimensions
        self.description_dict = self.read_csv_to_dictionary(path_to_csv_file)
        self.image_folder = image_folder
        self.width = width
        self.height = height
        self.root = Tk()  # Create the root Tkinter window
        self.root.title("Coffee Connect")  # Set the title of the window
        self.root.configure(bg="light goldenrod yellow")  # Set the background color for the window
        self.favorite_options = []  # List to store favorite coffee options
        self.show_welcome_page()  # Display the welcome page when the object is created

    def show_welcome_page(self):
        # Display the welcome page with a welcome image and message
        welcome_image = Image.open('./image/Icon.png')
        welcome_image = welcome_image.resize((300, 200), Image.Resampling.LANCZOS)
        welcome_photo = ImageTk.PhotoImage(welcome_image)
        self.welcome_image_label = Label(self.root, image=welcome_photo, bg="light goldenrod yellow")
        self.welcome_image_label.image = welcome_photo
        self.welcome_image_label.pack()

        self.welcome_message_label = Label(self.root, text="Welcome to Coffee Connect!", font=("Helvetica", 18, "bold"), fg="saddle brown", bg="light goldenrod yellow")
        self.welcome_message_label.pack()

        self.start_button = Button(self.root, text="Start", command=self.show_main_app, bg="peru", fg="white", font=("Helvetica", 14), borderwidth=2)
        self.start_button.pack()

    def show_main_app(self):
        # Display the main app page when the "Start" button is clicked
        self.welcome_image_label.pack_forget()
        self.welcome_message_label.pack_forget()
        self.start_button.pack_forget()

        # Create a frame for filtering coffee options
        self.filter_frame = Frame(self.root, bg="light goldenrod yellow")

        # Create entry fields for minimum rating and coffee name filters
        self.minimum_rating_value = DoubleVar(value=0)
        self.minimum_rating_label = Label(self.filter_frame, text="Min. rating", bg="light goldenrod yellow").grid(row=0, column=0)
        self.minimum_rating_entry = Entry(self.filter_frame, textvariable=self.minimum_rating_value).grid(row=0, column=1)
        self.name_value = StringVar(value="Any")
        self.name_label = Label(self.filter_frame, text="Name", bg="light goldenrod yellow").grid(row=1, column=0)
        self.name_entry = Entry(self.filter_frame, textvariable=self.name_value).grid(row=1, column=1)

        # Get unique coffee types from the CSV file for the filter dropdown
        unique_types = list(set(self.description_dict['type']))
        unique_types.insert(0, "Any")
        self.type_value = StringVar(value="Any")
        self.type_label = Label(self.filter_frame, text="Type", bg="light goldenrod yellow").grid(row=2, column=0)
        self.type_dropdown = OptionMenu(self.filter_frame, self.type_value, *unique_types)
        self.type_dropdown.grid(row=2, column=1)

        self.filter_frame.grid(row=0, column=0, columnspan=3)

        # Create "Run filter" button to filter coffee options based on the selected filters
        self.load_button = Button(self.root, text="Run filter", bg="peru", fg="white", command=self.show_coffee_Options, font=("Helvetica", 12), borderwidth=2)
        self.load_button.grid(row=1, column=0, columnspan=3)

        # Create "Favorite Coffee" button to show favorite coffee options
        self.favorite_button = Button(self.root, text="Favorite Coffee", bg="peru", fg="white", font=("Helvetica", 12), command=self.show_favorite_coffee, borderwidth=2)
        self.favorite_button.grid(row=1, column=4)

        # Create canvas and scrollbar for displaying coffee options
        self.canvas = Canvas(self.root, bg="light goldenrod yellow")
        self.canvas.grid(row=2, column=0, columnspan=5, sticky=NSEW)
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview, bg="peru")
        self.scrollbar.grid(row=2, column=5, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas to hold coffee options
        self.frame = Frame(self.canvas, bg="light goldenrod yellow")
        self.canvas.create_window((0, 0), window=self.frame, anchor=NW)

        # Extract image paths and descriptions from the CSV data
        self.img_paths = self.description_dict['image']
        self.descriptions = [dict(zip(self.description_dict, col)) for col in zip(*self.description_dict.values())]
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Display coffee options on the main app page
        self.show_coffee_Options()

    def run(self):
        # Start the Tkinter event loop to display the application
        self.root.mainloop()

    def read_csv_to_dictionary(self, csv_file_path):
        # Read the CSV file into a dictionary
        data_dict = {}
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for column, value in row.items():
                    if column not in data_dict:
                        data_dict[column] = []
                    data_dict[column].append(value)
        return data_dict

    def show_coffee_Options(self):
        # Display the coffee options based on the selected filters
        for widget in self.frame.winfo_children():
            widget.destroy()

        displayed_options = []

        for index, (img_path, description_dict) in enumerate(zip(self.img_paths, self.descriptions)):
            if float(description_dict['rating']) < self.minimum_rating_value.get():
                continue
            if self.name_value.get() != "Any" and self.name_value.get().lower() not in description_dict['name'].lower():
                continue
            if self.type_value.get() != "Any" and self.type_value.get() != description_dict['type']:
                continue

            img_path = self.image_folder + "/" + img_path
            img = Image.open(img_path)
            img = img.resize((self.width, self.height), Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            label = Label(self.frame, image=photo, bg="light goldenrod yellow")
            label.image = photo
            label.grid(row=index, column=0, padx=20, pady=10, sticky='nw')

            desc_text = '\n'.join([f'{k}: {v}' for k, v in description_dict.items()])
            desc_label = Label(self.frame, text=desc_text, justify='left', bg="light goldenrod yellow")
            desc_label.grid(row=index, column=1, padx=20, pady=10, sticky='nw')

            order_button = Button(self.frame, text="Order", bg="peru", fg="white", font=("Helvetica", 12), command=lambda i=index: self.order_coffee(i))
            order_button.grid(row=index, column=2, padx=10, pady=10, sticky='nw')

            favorite_button = Button(self.frame, text="Favorite", bg="peru", fg="white", font=("Helvetica", 12), command=lambda i=index: self.mark_favorite(i))
            favorite_button.grid(row=index, column=3, padx=10, pady=10, sticky='nw')

            displayed_options.append(True)

        if not any(displayed_options):
            message_label = Label(self.frame, text="No coffee options found.", font=("Helvetica", 16, "italic"), fg="saddle brown", bg="light goldenrod yellow")
            message_label.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky='nw')

        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def mark_favorite(self, index):
        # Mark or unmark a coffee option as a favorite
        selected_coffee = self.descriptions[index]['name']
        if selected_coffee not in self.favorite_options:
            self.favorite_options.append(selected_coffee)
        else:
            self.favorite_options.remove(selected_coffee)

        # Refresh the current page (main app or favorite coffee page) to reflect the changes
        self.refresh_current_page()

    def refresh_current_page(self):
        # Store the current tab/page (main or favorite) to determine which method to call
        current_page = self.root.focus_get()

        if current_page == self.load_button:
            self.show_coffee_Options()  # Refresh main coffee options page
        elif current_page == self.favorite_button:
            self.show_favorite_coffee()  # Refresh favorite coffee page

    def show_favorite_coffee(self):
        # Display the favorite coffee options
        for widget in self.frame.winfo_children():
            widget.destroy()

        for index, (img_path, description_dict) in enumerate(zip(self.img_paths, self.descriptions)):
            selected_coffee = description_dict['name']
            if selected_coffee in self.favorite_options:
                img_path = self.image_folder + "/" + img_path
                img = Image.open(img_path)
                img = img.resize((self.width, self.height), Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)

                label = Label(self.frame, image=photo, bg="light goldenrod yellow")
                label.image = photo
                label.grid(row=index, column=0, padx=20, pady=10, sticky='nw')

                desc_text = '\n'.join([f'{k}: {v}' for k, v in description_dict.items()])
                desc_label = Label(self.frame, text=desc_text, justify='left', bg="light goldenrod yellow")
                desc_label.grid(row=index, column=1, padx=20, pady=10, sticky='nw')

                order_button = Button(self.frame, text="Order", bg="peru", fg="white", font=("Helvetica", 12), command=lambda i=index: self.order_coffee(i))
                order_button.grid(row=index, column=2, padx=10, pady=10, sticky='nw')

                favorite_button = Button(self.frame, text="Unfavorite", bg="peru", fg="white", font=("Helvetica", 12), command=lambda i=index: self.mark_favorite(i))
                favorite_button.grid(row=index, column=3, padx=10, pady=10, sticky='nw')

        if not self.favorite_options:
            message_label = Label(self.frame, text="No favorite coffee options found.", font=("Helvetica", 16, "italic"), fg="saddle brown", bg="light goldenrod yellow")
            message_label.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky='nw')

        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def order_coffee(self, index):
        # Display a message indicating that a coffee has been ordered
        selected_coffee = self.descriptions[index]['name']
        message_label = Label(self.frame, text=f"{selected_coffee} has been ordered!", font=("Helvetica", 12), fg="green", bg="light goldenrod yellow")
        message_label.grid(row=index, column=1, padx=10, pady=10, sticky='nw')

# Create an instance of the CoffeeConnect class and start the app
app = CoffeeConnect('coffee_data.csv')
app.run()
