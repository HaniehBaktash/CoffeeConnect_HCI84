# Developer's Guide: CoffeeConnect Application

## Overview

CoffeeConnect is a GUI application built in Python using Tkinter. The application allows users to explore a list of coffee options, apply filters based on their preferences, mark favorite coffees, and place orders. This guide provides an overview of the code structure, user interaction, and potential future improvements

## Code Structure

The primary script of the project is `Run Python CoffeeConnect_HCI584.py`, which is the entry point of the application. It contains the main functions for the program:

- `start`: Sets up and runs the application.
- `get_data`: Fetches the coffee data from the CSV file.
- `find_matches`: Filters the coffee data based on user preferences and prints the matching users.
  
1. `CSV_File_Structure`:
The CSV file used in the project follows a specific structure to store coffee data. It consists of columns representing various attributes of each coffee, such as name, rating, type, and image filename. Each row represents a different coffee entry with corresponding attribute values.

2. `Application Startup`:
The application is started by executing the CoffeeConnect_HCI584.py script, which serves as the entry point. This script initializes the CoffeeConnect class, which handles the GUI interface and user interactions.

3. `User Input Data:`
The user can input three main filtering criteria:

- `Minimum Rating`: The user can set a minimum rating, and the application will display only those coffees with ratings greater than or equal to the specified value.
Coffee Name: The user can input a coffee name, and the application will filter and display only those coffees whose names contain the provided input (case-insensitive).
- `Coffee Type`: The user can select a specific coffee type from the dropdown menu, and the application will display only coffees of the selected type. Alternatively, selecting "Any" will display all coffee types.
- `Filtering Mechanism`:
The filtering process is managed by the show_coffee_Options() method. It iterates through the list of coffee entries, checking each entry against the specified filter criteria. Coffee entries that meet the filter conditions are displayed in the GUI, while those that do not are skipped.

## Installation

1. Create a virtual environment using `python -m venv env`.
2. Activate the virtual environment.
3. Install the required libraries using `pip install -r requirements.txt`.

## User Interaction and Code Flow

`Application Startup`:

When the Run Python CoffeeConnect_HCI584.py script is executed, it initializes the CoffeeConnect class, which creates the GUI window with a welcome page. The user is greeted with a welcome message and an option to start the main app.

`Main App Initialization`:
Upon clicking the "Start" button, the show_main_app() method is triggered. This method sets up the filter section, including the rating, name, and type input fields. Additionally, it creates a canvas to display coffee options and a scrollbar for navigation.

`Filtering Process`:
The user can input filtering criteria through the rating, name, and type fields. After clicking the "Run filter" button, the show_coffee_Options() method is called to apply the filters and display the relevant coffee options.

`Displaying Coffee Options`:
The show_coffee_Options() method retrieves coffee data using the description_dict, and the data is filtered based on user input. The matching coffee options are displayed in the canvas with their corresponding images and descriptions.

`Marking Favorite Coffees`:
Users can mark their favorite coffees by clicking the "Favorite" button next to each coffee option. The "Favorite" button turns into "Unfavorite" when a coffee is marked. Users can also access their list of favorite coffee options by clicking the "Favorite Coffee" button.

`Placing Coffee Orders`:
To place an order, users can click the "Order" button next to their desired coffee option. The application confirms the successful coffee order with a message.

## Known Issues and Potential Solutions

- The application currently only supports exact matching based on user inputs. Future implementations could include fuzzy matching or the ability to match based on similar, rather than identical, coffee preferences.

## Future Work

Adding More Data:
To add more data to the application, update the CSV file with new coffee entries and their attributes. The application will dynamically adjust to the new data upon each execution, allowing users to view additional coffee options seamlessly.

Enhanced Matching Algorithms:
Consider using more sophisticated matching algorithms to find users with similar, but not identical, coffee preferences. This would provide more accurate and relevant coffee suggestions.

Transition to Web Application:
Explore transitioning the application into a web application for a more user-friendly and accessible interface. This could increase the reach and usability of CoffeeConnect.

Direct Connection with Users:
Add the ability for users to connect with their coffee matches directly through the application. This could facilitate coffee enthusiasts in sharing recommendations and building a coffee community.

## Ongoing Deployment/Development

 there are a few considerations for the future:

1. Write unit tests for the various functions to ensure that new changes don't break existing functionality.
2. Using version control (e.g., Git) would allow tracking changes and easier collaboration if more developers join the project.
3. Continue to maintain and update the code documentation as new features are added or changes are made.
4. Adding more features such as location for each coffee

## Conclusion

CoffeeConnect is a delightful and user-friendly application that caters to coffee enthusiasts' preferences. With its intuitive interface and efficient filtering mechanism, users can easily find their perfect cup of coffee and connect with like-minded coffee lovers. The ongoing development and future enhancements will ensure that CoffeeConnect remains a go-to platform for coffee enthusiasts worldwide.