import os

class ConsoleMenu:
    # Console Menu Option Subclass
    class ConsoleMenuOption:
        def __init__(self, key, label, func):
            self.key = key
            self.label = label
            self.func = func

        def get_key(self):
            return self.key

        def set_key(self, key):
            self.key = key

        def get_label(self):
            return self.label

        def set_label(self, label):
            self.label = label

        def get_func(self):
            return self.func

        def set_func(self, func):
            self.func = func

    # Console Menu Base Class Methods and Functions
    def __init__(self, menu_name, banner, menu_options=[], previous_menu=[], child_menu=[]):
        self.menu_name = menu_name
        self.banner = banner
        self.menu_options = menu_options
        self.previous_menu = previous_menu
        self.child_menu = child_menu

    # self.menu_name methods
    def get_menu_name(self):
        return self.menu_name
    def set_menu_name(self, menu_name):
        self.menu_name = menu_name

    # self.banner methods
    def get_banner(self):
        return self.banner
    def set_banner(self, banner):
        self.banner = banner
    def show_banner(self):
        print(f"\n{self.banner}\n")

    # self.menu_options methods
    def get_menu_options(self):
        return self.menu_options
    def set_menu_options(self, menu_options):
        self.menu_options = menu_options
    def show_menu_options(self):
        for option in self.menu_options:
            print(f"[ {option.key} ]: {option.label}\n")

    # self.previous_menu methods
    def get_previous_menu(self):
        return self.previous_menu
    def set_previous_menu(self, previous_menu):
        self.previous_menu = previous_menu

    # self.child_menu methods
    def get_child_menu(self):
        return self.child_menu
    def set_child_menu(self, child_menu):
        self.child_menu = child_menu

    # Misc functions
    def go_back(self):
        self.previous_menu.show_full()

    def show_full(self):
        """
        Shows the full menu and returns the user's selection.
        """
        while True:
            print(f"\n{self.banner}\n")
            for option in self.menu_options:
                print(f"[ {option.key} ]: {option.label}")
            print()
            choice = input("Enter your choice: ")

            # find the menu option with the matching key
            selected_option = next(
                (x for x in self.menu_options if x.key == choice), None)

            # if a matching option was found, perform the corresponding action
            if selected_option is not None:
                print()
                selected_option.func()
            # if no matching option was found, exit the main loop
            else:
                print("Invalid selection. Please try again.")
                self.show_full()


"""
************************************************************************************************************************************
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


"""
************************************************************************************************************************************
"""


def print_columns(data, keys, max_width=30):
    print()
    # Calculate the width of each column
    column_widths = {}
    for key in keys:
        column_widths[key] = max(max_width, max(
            [len(str(row[key])) for row in data]))

    # Print the column names
    row_str = ''
    for key in keys:
        key_str = str(format_simple_heading_spaced(key))[:column_widths[key]]
        row_str += f"{key_str}{' '*(column_widths[key]-len(key_str))}\t"
    print(row_str)

    # Print the rows of data
    for row in data:
        row_str = ''
        for key in keys:
            value_str = str(row[key])[:column_widths[key]]
            row_str += f"{value_str}{' '*(column_widths[key]-len(value_str))}\t"
        print(row_str)
    print()


"""
************************************************************************************************************************************
"""


def format_simple_heading_spaced(text):
    """
    Format the given text by adding brackets, padding characters, and separating each letter with a space.

    Parameters:
    text (str): The text to format.

    Returns:
    str: The formatted text.
    """
    # Separate each letter in the text with a space
    spaced_text = ' '.join(list(text))

    # Add the brackets and padding characters
    formatted_text = f"[  {spaced_text}  ]"

    return formatted_text
