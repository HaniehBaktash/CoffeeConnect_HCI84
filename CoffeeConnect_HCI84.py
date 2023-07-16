import tkinter as tk
from tkinter import Tk, Canvas, Frame, Entry, Scrollbar, Button, Label, DoubleVar, StringVar, OptionMenu
from tkinter import VERTICAL, BOTH, NSEW, NW
from PIL import Image, ImageTk
from PIL.Image import Resampling
import csv

# Define the main class CoffeeConnect for the GUI
class CoffeeConnect:
    # Initialize the object with CSV file path, image folder path and image dimensions
    def __init__(self, path_to_csv_file, image_folder="./image", width=200, height=200):
        # Read CSV file into a dictionary and store image folder path and image dimensions
        self.description_dict = self.read_csv_to_dictionary(path_to_csv_file)
        self.image_folder = image_folder
        self.width = width
        self.height = height
        # Create the root Tkinter window
        self.root = Tk()

        # Display the welcome page
        self.show_welcome_page()

    # Define function to display the welcome page
    def show_welcome_page(self):
        # Load and process welcome image
        welcome_image = Image.open('./image/header.jpg')
        welcome_image = welcome_image.resize((300, 200), Image.Resampling.LANCZOS)
        welcome_photo = ImageTk.PhotoImage(welcome_image)
        # Create label to display welcome image and pack it into the root window
        self.welcome_image_label = Label(self.root, image=welcome_photo)
        self.welcome_image_label.image = welcome_photo
        self.welcome_image_label.pack()
        # Create label to display welcome message and pack it into the root window
        self.welcome_message_label = Label(self.root, text="Welcome to Coffee Connect!", font=("Helvetica", 18))
        self.welcome_message_label.pack()
        # Create start button and pack it into the root window. This button will lead to the main app when clicked.
        self.start_button = Button(self.root, text="Start", command=self.show_main_app)
        self.start_button.pack()

    # Define function to display the main app
    def show_main_app(self):
        # Remove the welcome page elements from the root window
        self.welcome_image_label.pack_forget()
        self.welcome_message_label.pack_forget()
        self.start_button.pack_forget()
        # Create a frame for the filter section
        self.filter_frame = Frame(self.root)
        # Create entry fields for minimum rating and coffee name filters
        self.minimum_rating_value = DoubleVar(value=0)
        self.minimum_rating_label = Label(self.filter_frame, text="Min. rating").grid(row=0, column=0)
        self.minimum_rating_entry = Entry(self.filter_frame, textvariable=self.minimum_rating_value).grid(row=0, column=1)
        self.name_value = StringVar(value="Any")
        self.name_label = Label(self.filter_frame, text="Name").grid(row=1, column=0)
        self.name_entry = Entry(self.filter_frame, textvariable=self.name_value).grid(row=1, column=1)
        # Create a dropdown list for the type filter
        unique_types = list(set(self.description_dict['type']))  # Assuming 'type' is the key for types in your csv
        unique_types.insert(0, "Any")
        self.type_value = StringVar(value="Any")
        self.type_label = Label(self.filter_frame, text="Type").grid(row=2, column=0)
        self.type_dropdown = OptionMenu(self.filter_frame, self.type_value, *unique_types)
        self.type_dropdown.grid(row=2, column=1)
        # Pack the filter frame into the root window
        self.filter_frame.grid(row=0, column=0, columnspan=2)
        # Create a button to apply the filters and display the coffee options. Pack this button into the root window.
        self.load_button = Button(self.root, text="Run filter", command=self.show_coffee_Options)
        self.load_button.grid(row=1, column=0, columnspan=2) 
        # Create a canvas to display the coffee options. This canvas will have a vertical scrollbar.
        self.canvas = Canvas(self.root)
        self.canvas.grid(row=2, column=0, sticky=NSEW)
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(row=2, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        # Add a frame to the canvas. This frame will contain the coffee options.
        self.frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor=NW)
        # Get the image paths and descriptions from the dictionary
        self.img_paths = self.description_dict['image']
        self.descriptions = [dict(zip(self.description_dict, col)) for col in zip(*self.description_dict.values())]
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        # Display the coffee options
        self.show_coffee_Options()

    # Define function to start the Tkinter event loop
    def run(self):
        self.root.mainloop()

    # Define function to read the CSV file into a dictionary
    def read_csv_to_dictionary(self, csv_file_path):
        data_dict = {}
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for column, value in row.items():
                    if column not in data_dict:
                        data_dict[column] = []
                    data_dict[column].append(value)
        return data_dict

    # Define function to display the coffee options
    def show_coffee_Options(self):
        # Remove any existing coffee options from the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Loop through each coffee option
        for index, (img_path, description_dict) in enumerate(zip(self.img_paths, self.descriptions)):
            # Apply the filters
            if float(description_dict['rating']) < self.minimum_rating_value.get():
                continue
            if self.name_value.get()!= "Any" and self.name_value.get().lower() not in description_dict['name'].lower():
                continue
            if self.type_value.get()!= "Any" and self.type_value.get() != description_dict['type']:  # Assuming 'type' is the key for types in your csv
                continue
            # Load and process the image for this coffee option
            img_path = self.image_folder + "/" + img_path
            img = Image.open(img_path)
            img = img.resize((self.width, self.height), Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            # Create a label to display the image and pack it into the frame
            label = Label(self.frame, image=photo)
            label.image = photo
            label.grid(row=index, column=0, padx=20, pady=10, sticky='nw')  # Change the anchor point to 'nw' to align image to the top left
            # Create a label to display the description and pack it into the frame
            desc_text = '\n'.join([f'{k}: {v}' for k, v in description_dict.items()])
            desc_label = Label(self.frame, text=desc_text, justify='left') 
            desc_label.grid(row=index, column=1, padx=20, pady=10, sticky='nw')  # Change the anchor point to 'nw' to align text to the top left
        # Update the scrollregion of the canvas to match the bbox of all items
        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))     

# Create an instance of the CoffeeConnect class and start the app
app = CoffeeConnect('coffee_data.csv')
app.run()
