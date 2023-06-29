import tkinter as tk
from tkinter import Tk, Canvas, Frame, Scrollbar, Button, Label, VERTICAL, BOTH, NSEW, NW
from PIL import Image, ImageTk
import csv

# Create a Scrollable image app
class CoffeeConnect:
    # def __init__(self, img_paths, descriptions, width=500, height=500):
   
    def __init__(self, description_dict, width=200, height=200):
        self.root = Tk()

        self.load_button = Button(self.root, text="Load Images", command=self.Coffee_Options)
        self.load_button.grid(row=0, column=0, columnspan=2)  

        self.create_account_button = Button(self.root, text="Create Account", command=self.create_account)
        self.create_account_button.grid(row=1, column=0, columnspan=2)  

        
        # Create a Canvas widget with a scrollbar
        self.canvas = Canvas(self.root)
        self.canvas.grid(row=2, column=0, sticky=NSEW)  # Canvas moved below the button

        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(row=2, column=1, sticky='ns')  # Scrollbar moved below the button

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Add a Frame to the Canvas
        self.frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor=NW)

        self.img_paths = description_dict['image']
        # For the descriptions, I create a list of dictionaries for each row
        self.descriptions = [dict(zip(description_dict, col)) for col in zip(*description_dict.values())]
    
        self.width = width
        self.height = height

        self.root.grid_rowconfigure(2, weight=1)  # Now the Canvas expands instead of the button
        self.root.grid_columnconfigure(0, weight=1)

        self.root.mainloop()
    def create_account(self):
        # Creating a user account I will work on this part more.
        for widget in self.frame.winfo_children():
            widget.destroy()

        tk.Label(self.frame, text="Email").grid(row=0, column=0)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Password").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        submit_button = tk.Button(self.frame, text="Submit", command=self.submit_new_account)
        submit_button.grid(row=2, column=0, columnspan=2)

        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def submit_new_account(self):
        entered_email = self.email_entry.get()
        entered_password = self.password_entry.get()
        print(f"Entered email: {entered_email}, entered password: {entered_password}")

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


    def run(self):
        self.root.mainloop()

    def Coffee_Options(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for img_path, description_dict in zip(self.img_paths, self.descriptions):
            img = Image.open(img_path)
            img = img.resize((self.width, self.height), Image.ANTIALIAS)
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

#read csv file
def read_csv_to_dictionary(csv_file_path):
    data_dict = {}

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            for column, value in row.items():
                if column not in data_dict:
                    data_dict[column] = []

                data_dict[column].append(value)

    return data_dict

data_dict = read_csv_to_dictionary('coffee_data.csv')
app = CoffeeConnect(data_dict)
app.run()


           
    
