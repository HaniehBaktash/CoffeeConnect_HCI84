import tkinter as tk
from tkinter import Tk, Canvas, Frame, Entry, Scrollbar, Button, Label, DoubleVar, StringVar
from tkinter import VERTICAL, BOTH, NSEW, NW
from PIL import Image, ImageTk
from PIL.Image import Resampling
import csv

# Create a Scrollable image app
class CoffeeConnect:

    def __init__(self, path_to_csv_file, image_folder="./image", width=200, height=200):

        self.description_dict = self.read_csv_to_dictionary(path_to_csv_file)
        self.image_folder = image_folder
        self.width = width
        self.height = height
        self.root = Tk()

        self.show_welcome_page()

    def show_welcome_page(self):
        welcome_image = Image.open('./image/header.jpg')  # replace with your welcome image path
        welcome_image = welcome_image.resize((300, 300), Image.ANTIALIAS)
        welcome_photo = ImageTk.PhotoImage(welcome_image)
        self.welcome_image_label = Label(self.root, image=welcome_photo)
        self.welcome_image_label.image = welcome_photo
        self.welcome_image_label.pack()
        self.welcome_message_label = Label(self.root, text="Welcome to Coffee Connect!", font=("Helvetica", 16))
        self.welcome_message_label.pack()
        self.start_button = Button(self.root, text="Start", command=self.show_main_app)
        self.start_button.pack()

    def show_main_app(self):
        self.welcome_image_label.pack_forget()
        self.welcome_message_label.pack_forget()
        self.start_button.pack_forget()
        # the rest of your main app initializations
        # some filters
        self.filter_frame = Frame(self.root)
        self.minimum_rating_value = DoubleVar(value=0)
        self.minimum_rating_label = Label(self.filter_frame, text="Min. rating").grid(row=0, column=0)
        self.minimum_rating_entry = Entry(self.filter_frame, textvariable=self.minimum_rating_value).grid(row=0, column=1)
        self.name_value = StringVar(value="Any")
        self.name_label = Label(self.filter_frame, text="Name").grid(row=1, column=0)
        self.name_entry = Entry(self.filter_frame, textvariable=self.name_value).grid(row=1, column=1)
        self.filter_frame.grid(row=0, column=0, columnspan=2)
        self.load_button = Button(self.root, text="Run filter", command=self.show_coffee_Options)
        self.load_button.grid(row=1, column=0, columnspan=2) 
        # Create a Canvas widget with a scrollbar
        self.canvas = Canvas(self.root)
        self.canvas.grid(row=2, column=0, sticky=NSEW)
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(row=2, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        # Add a Frame to the Canvas
        self.frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor=NW)
        self.img_paths = self.description_dict['image']
        self.descriptions = [dict(zip(self.description_dict, col)) for col in zip(*self.description_dict.values())]
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.show_coffee_Options()

    def run(self):
        self.root.mainloop()

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
    # the rest of your class methods remain unchanged

    def show_coffee_Options(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for img_path, description_dict in zip(self.img_paths, self.descriptions):

            # apply filter: skip this entry if it's rating is not high enough
            if float(description_dict['rating']) < self.minimum_rating_value.get():
                continue

            if self.name_value.get()!= "Any":
                if self.name_value.get().lower() not in description_dict['name'].lower():
                    continue

            img_path = self.image_folder + "/" + img_path
            img = Image.open(img_path)
            img = img.resize((self.width, self.height), Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            label = Label(self.frame, image=photo)
            label.image = photo
            label.pack(anchor='center', pady=10)

        # Convert the dictionary to a string and display it in a label
            desc_text = '\n'.join([f'{k}: {v}' for k, v in description_dict.items()])
            desc_label = Label(self.frame, text=desc_text, justify='center')
            desc_label.pack(anchor='center', pady=10)

        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))     

app = CoffeeConnect('coffee_data.csv')
app.run()
