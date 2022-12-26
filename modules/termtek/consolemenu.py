import os
import pprint
import time
import random
import modules.termtek as ttk

debug = False

class ConsoleMenuOption:
    def __init__(self, key, label, func):
        self.key = key
        self.label = label
        self.func = func

    def get_all(self):
        return [self.key, self.label, self.func]

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

class ConsoleMenu:

    # Console Menu Base Class Methods and Functions
    def __init__(self, menu_name, banner, menu_options=[], previous_menu=[], child_menus=[]):
        self.menu_name = menu_name
        self.banner = banner
        self.menu_options = menu_options
        self.previous_menu = previous_menu

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
    def append_menu_option(self, option):
        self.menu_options.append(option)
    def show_menu_options(self):
        for option in self.menu_options:
            print(f"[ {option.key} ]: {option.label}\n")

    # self.previous_menu methods
    def get_previous_menu(self):
        return self.previous_menu
    def set_previous_menu(self, previous_menu):
        self.previous_menu = previous_menu

    # Misc functions

    def go_back(self):
        self.previous_menu.show_full()

    def show_full(self):
        """
        Shows the full menu and returns the user's selection.
        """
        while True:
            self.show_banner()
            options = self.get_menu_options()
            for option in options:
                key = option.get_key()
                label = option.get_label()
                print(f"[ {key} ]: {label}")
            print()
            choice = input("Please select an option: ").lower()

            # find the menu option with the matching key
            selected_option = next( (x for x in self.menu_options if x.key == choice), None)

            # if a matching option was found, perform the corresponding action
            if selected_option is not None:
                print()
                selected_option.func()
            # if no matching option was found, exit the main loop
            else:
                print("Invalid selection. Please try again.")
                self.show_full()


def build_console_menu_objects(all_menus):

    def init_menus(all_menus):
        print(ttk.colorize("\n[ INITIALIZING MENUS ]\n", "blue")) if debug else None

        for menu in all_menus:

            menu["console_menu_object"] = ConsoleMenu(menu["menu_name"], menu["banner"])
            if debug:
                create_str = ttk.colorize("    [ CREATED ]", "green")
                str = create_str + f' {menu["menu_name"]} ------ {menu["console_menu_object"]}'
                print(ttk.colorize(str, "green"))

    def set_previous_menus(all_menus):
        print(ttk.colorize("\n[ SETTING PREVIOUS MENUS ]\n", "blue")) if debug else None
        
        for menu in all_menus:
            for option in menu["menu_options"]:
                if isinstance(option[2], dict) and "goto" in option[2]:
                    # get the goto menu name
                    goto_menu_name = option[2]["goto"]

                    # Find the menu being called
                    called_menu = None
                    for m in all_menus:
                        if m["menu_name"] == goto_menu_name:
                            called_menu = m
                            break

                    # Set the previous menu for the called menu
                    called_menu["console_menu_object"].set_previous_menu(menu["console_menu_object"])
                    if debug:
                        set_str = ttk.colorize("    [ SET ]", "green")
                        str = set_str + f' {called_menu["menu_name"]}`s previous_menu to == {menu["console_menu_object"]}'
                        print(ttk.colorize(str, "green"))

    def swap_goto_with_function(all_menus):
        print(ttk.colorize("\n[ SWAPPING GOTO WITH FUNCTIONS ]", "blue")) if debug else None
        
        found_goto_count = 0
        found_goto = False
        for menu in all_menus:
            print(ttk.colorize("\n[ MENU ]", "cyan") + f" {menu['menu_name']}") if debug else None
            
            for option in menu["menu_options"]:
                if isinstance(option[2], dict) and "goto" in option[2]:
                    found_goto = True
                    found_goto_count += 1
                    # get the goto menu name
                    goto_menu_name = option[2]["goto"]

                    # Find the menu being called
                    called_menu_object = None
                    for m in all_menus:
                        if m["menu_name"] == goto_menu_name:
                            called_menu_object = m["console_menu_object"]
                            break

                    if debug:
                        print(ttk.colorize("\n    [ FOUND GOTO ]", "green"))
                        print(f"        goto_menu_name: {goto_menu_name}")
                        print(f"        called_menu_object: {called_menu_object}")
                        print(f"        called_menu_object.get_menu_name(): {called_menu_object.get_menu_name()}")
                        print(f"        called_menu_object.show_full: {called_menu_object.show_full}")
                        debug_action = ttk.colorize("    [ GOTO SWAP ]", "green")
                        print(f"\n{debug_action}\n        og menu_option:\n        {option}")

                    option[2] = called_menu_object.show_full
                    
                    print(f"        new menu_option:\n        {option}") if debug else None

                if debug and not found_goto:
                    debug_action = ttk.colorize("    [ NO GOTO FOUND ]", "yellow")
                    print(f"\n{debug_action}\n        menu_option:\n        {option}")
                found_goto = False
    
    def add_back_button_options(all_menus):
        if debug:
            print(ttk.colorize("\n[ ADDING BACK BUTTON OPTIONS ]", "blue"))
            for menu in all_menus:
                print(ttk.colorize("\n[ MENU ]", "cyan") + f" {menu['menu_name']}")
                print(ttk.colorize("\n    [ ADDING BACK BUTTON OPTION ]", "green"))

                print(f"        Original Options:")
                for option in menu["menu_options"]:
                    print(f"        menu_option: {option}")

                print("\n        Is there a previous menu?")
                if menu["console_menu_object"].get_previous_menu():
                    print(ttk.colorize("        [ YES ]\n", "green"))
                    m = menu["console_menu_object"].get_previous_menu()
                    print(f"        Previous menu name: {m.get_menu_name()}")
                    print(f"        Previous menu object: {m}")
                    debug_action = ttk.colorize("        [ SET ]", "green")
                    print(f"\n{debug_action}\n        New menu_option:\n        ['back', 'Go back', {m.show_full}]")
                    menu["menu_options"].append(["back", "Go back", m.show_full])
                else:
                    print(ttk.colorize("        [ NO ]", "red"))
                
                debug_action = "\n        FINAL OPTIONS for " + menu["menu_name"]
                print(ttk.colorize(debug_action, "white"))
                for option in menu["menu_options"]:
                    print(f"        menu_option: {option}")
        else:
            for menu in all_menus:
                if menu["console_menu_object"].get_previous_menu():
                    m = menu["console_menu_object"].get_previous_menu()
                    menu["menu_options"].append(["back", "Go back", m.show_full])

    def add_final_menu_options(all_menus):
        print(ttk.colorize("\n[ ADDING FINAL MENU OPTIONS ]", "blue")) if debug else None
        
        for menu in all_menus:
            print(ttk.colorize("\n[ MENU ]", "cyan") + ttk.colorize(f" {menu['menu_name']}", "green")) if debug else None
            
            new_option_objects = []

            for option in menu["menu_options"]:
                new_object = ConsoleMenuOption(option[0], option[1], option[2])
                new_option_objects.append(new_object)
                if debug:
                    print(ttk.colorize("\n    [ NEW CONSOLE MENU OPTION OBJECT ]", "green"))
                    print(f"        new_object: {new_object}")

            menu["console_menu_object"].set_menu_options(new_option_objects)
            
            check = []
            option_objects = menu["console_menu_object"].get_menu_options()
            for obj in option_objects:
                check.append(obj.get_all())

            if debug:
                #print(f'CHECK: {check}')
                #print(f'MENU OPTIONS: {menu["menu_options"]}')

                if check == menu["menu_options"]:
                    print(ttk.colorize("\n    [ FINAL OPTIONS SET SUCCESSFULLY ]", "green"))
    
    def debug_menu_info(all_menus):
        print(ttk.colorize("\n[ DEBUG MENU INFO ]\n", "blue"))
        for menu in all_menus:
            print(ttk.colorize("[ MENU ]", "cyan") + f" {menu['menu_name']}")
            print(f'all_menus["menu_name"] => {menu["menu_name"]}')
            print(f'all_menus["banner"] => \n{menu["banner"]}')
            print(f'all_menus["console_menu_object"].get_previous_menu() => {menu["console_menu_object"].get_previous_menu()}')
            print()

            for option in menu["menu_options"]:
                print(f"Pre-Build Menu option => {option}")
            print()

            if menu["console_menu_object"].get_menu_options():
                for object in menu["console_menu_object"].get_menu_options():
                    print(f"Post-Build Menu option object => {object}")
                    options = object.get_all()
                    print(f"Post-Build Menu option object.get_all() =>")
                    print(options)
                    print()
                print()
            else:
                print(ttk.colorize("menu['console_menu_object'].get_menu_options() contains no menu objects", "red"))
                print("It is possible that you are debugging right now and they are not set to build yet")
                print("Otherwise you better get in there and figure out why they are not building lol")
                print("Hint: Check the build_console_menu_objects() -> add_final_menu_options() functions :D\n")

        build_success = True
        for menu in all_menus:
            check = []
            option_objects = menu["console_menu_object"].get_menu_options()

            for obj in option_objects:
                check.append(obj.get_all())

            if check == menu["menu_options"]:
                pass
            else:
                build_success = False
                break
            
        if build_success:
            print(ttk.colorize("[ BUILD SUCCESS ]", "green"))
            print(ttk.colorize("[ WOOOOOOO YEAAAAAAAAA LETSSSS GOOOO BAYYY BEEEEEEEEE ]\n", "white"))
        else:
            print(ttk.colorize("[ BUILD FAILURE ]", "red"))
            print(ttk.colorize("YOU GOT SOME FIXIN TO DO LOL", "white"))

    init_menus(all_menus)
    set_previous_menus(all_menus)
    swap_goto_with_function(all_menus)
    add_back_button_options(all_menus)
    add_final_menu_options(all_menus)
    debug_menu_info(all_menus) if debug else None
    

"""
************************************************************************************************************************************
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pp(arr):
    pprint.pprint(arr)

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
        key_str = str(return_simple_heading_spaced(key))[:column_widths[key]]
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

def return_simple_heading_spaced(text):
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

def print_text_humanistic(text: str):
    """Print text character by character with humanistic variations in speed."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(random.uniform(0.01, 0.025))
    print()

