import pprint
import modules.termtek as ttk
from typing import List, Callable, Dict, Any
import modules.termtek.consolemenu as cm
import sys

debug = True

def pp(arr):
    pprint.pprint(arr)

def exit():
    sys.exit()

def testone():
    print(ttk.build_fancy_font("Test one"))

def testtwo():
    print(ttk.build_fancy_font("Test two"))

def settings_testone():
    print(ttk.build_fancy_font("Settings test one"))

def settings_testtwo():
    print(ttk.build_fancy_font("Settings test two"))

# test_struct = [
#     {
#         "menu_name": "root_menu", # <=======| string
#         "banner": "Main Menu", # <=======| string
#         "menu_options": [
#             ["key", "label", testone] # <=======| list of strings but func is a reference to a function
#         ], # <=======| list of python objects
#         "previous_menu": [], # <=======| string
#         "child_menus": [] # <=======| list of ConsoleMenu python objects
#     }
# ]

def exit():
    sys.exit()

all_menus = []

settings_menu = {
    "menu_name": "settings_menu",
    "banner": "Settings Menu",
    "menu_options": [
        ["password", "Change your account password", settings_testone],
        ["email", "Change your account email", settings_testtwo],
    ],
    "previous_menu": "root_menu",
    "child_menus": [],
    "console_menu_object": None
}
all_menus.append(settings_menu)

openai_api_settings_menu = {
    "menu_name": "openai_api_settings_menu",
    "banner": "Openai Api Settings Menu",
    "menu_options": [
        ["test1", "Test openai settings function one", settings_testone],
        ["test2", "Test openai settings funtion two", settings_testtwo],
    ],
    "previous_menu": "openai_api_menu",
    "child_menus": [],
    "console_menu_object": None
}
all_menus.append(openai_api_settings_menu)

openai_api_menu = {
    "menu_name": "openai_api_menu",
    "banner": "Openai Api Menu",
    "menu_options": [
        ["test1", "Test openai function one", testone],
        ["test2", "Test openai funtion two", testtwo],
        ["aisettings", "Change settings for openai", {"goto": "openai_api_settings_menu"}],
    ],
    "previous_menu": "root_menu",
    "child_menus": [openai_api_settings_menu],
    "console_menu_object": None
}
all_menus.append(openai_api_menu)

root_menu = {
    "menu_name": "root_menu",
    "banner": "Main Menu",
    "menu_options": [
        ["test1", "Test function one", testone],
        ["test2", "Test funtion two", testtwo],
        ["openai", "Play with Openai API", {"goto": "openai_api_menu"}],
        ["settings", "Change settings for the program", {"goto": "settings_menu"}],
        ["exit", "Exit the program", exit]
    ],
    "previous_menu": None,
    "child_menus": [],
    "console_menu_object": None
}
all_menus.append(root_menu)

###
### DONT FORGET TO MAKE THE child_menus AUTOMATICALLY POPULATE BASED ON THE GOTOS IN THE MENU OPTIONS
### DONT FORGET TO AUTOMATICALLY ADD A BACK OPTION TO THE PREVIOUS MENU
### DONT FORGET TO MAKE THE previous_menu AUTOMATICALLY POPULATE BASED ON THE GOTOS IN THE MENU OPTIONS
###
def build_console_menu_objects(all_menus):

    for menu in all_menus:
        # create a new console menu object for each menu
        menu["console_menu_object"] = cm.ConsoleMenu(menu["menu_name"], menu["banner"])
        if debug:
            print(f'CREATED {menu["menu_name"]} ------ {menu["console_menu_object"]}')
        
        # add the menu options to the console menu object
        for option in menu["menu_options"]:
            if debug:
                print(f"OPTION: [ {option[0]} ] {option[1]}, {option[2]}")
        if debug:
            print()

if debug:
    print("ALL MENUS")
    print()
build_console_menu_objects(all_menus)





# console_menus = [{
#     "menu_name": "root_menu",
#     "banner": "Main Menu",
#     "menu_options": [
#                 ["test1", "Test function one", testone],
#                 ["test2", "Test funtion two", testtwo],
#                 ["openai", "Play with Openai API",
#                     {"goto": "openai_api_menu"}],
#                 ["settings", "Change settings for the program",
#                     {"goto": "settings_menu"}],
#                 ["exit", "Exit the program", exit]
#     ],
#     "previous_menu": None,
#     "child_menus": [
#         {
#             "menu_name": "openai_api_menu",
#             "banner": "Openai Api Menu",
#             "menu_options": [
#                 ["test1", "Test openai function one", testone],
#                 ["test2", "Test openai funtion two", testtwo],
#                 ["settings", "Change settings for openai",
#                     {"goto": "open_ai_api_settings_menu"}],
#             ],
#             "previous_menu": "root_menu",
#             "child_menus": [
#                 {
#                     "menu_name": "openai_api_settings_menu",
#                     "banner": "Openai Api Settings Menu",
#                     "menu_options": [
#                         ["test1", "Test openai settings function one", settings_testone],
#                         ["test2", "Test openai settings funtion two", settings_testtwo],
#                     ],
#                     "previous_menu": "openai_api_menu",
#                     "child_menus": []
#                 }
#             ]
#         },
#         {
#             "menu_name": "settings_menu",
#             "banner": "Settings Menu",
#             "menu_options": [
#                 ["password", "Change your account password", settings_testone],
#                 ["email", "Change your account email", settings_testtwo],
#             ],
#             "previous_menu": "root_menu",
#             "child_menus": []
#         }
#     ]
# }]

# If this module is the main module being run (not imported by another script)
# if __name__ == "__main__":

#     def goto_menu(menu_name, built_menus):
#         for menu in built_menus:
#             if menu.menu_name == menu_name:
#                 return menu.show_full()

#     def build_menu(menu_structure, built_menus=[]):
#         menu_name = menu_structure["menu_name"]
#         banner = menu_structure["banner"]
#         menu_options = menu_structure["menu_options"]
#         previous_menu = menu_structure["previous_menu"]
#         child_menus = menu_structure["child_menus"]

#         # Create a new ConsoleMenu object
#         menu = cm.ConsoleMenu(
#             menu_name, banner, previous_menu=previous_menu, child_menus=child_menus)

#         # Add the ConsoleMenu object to the list of built menus
#         built_menus.append(menu)

#         # Iterate through the menu options and add them to the ConsoleMenu object
#         for option in menu_options:
#             key = option[0]
#             label = option[1]
#             func = option[2]

#             # Check the type of func
#             if isinstance(func, dict):
#                 # If func is a dictionary, it should have a "goto" key
#                 # Create a lambda function that calls the goto_menu function with the correct arguments
#                 def func(): return goto_menu(func['goto'], built_menus)
#             else:
#                 # If func is not a dictionary, it should be a callable function
#                 # Create a lambda function that calls the function
#                 def func(): return func()

#             # Create a new ConsoleMenuOption object and add it to the menu
#             # menu_option = cm.ConsoleMenu.ConsoleMenuOption(key, label, func)
#             menu.append_menu_option(key, label, func)

#         # Return the list of built menus
#         return built_menus


# x = build_menu(console_menus[0])
# x[0].show_full()
# for i in x:
#     print(f"Menu Name: {i.get_menu_name()}")
#     print(f"Menu Banner: {i.get_banner()}\n")
#     menu_options = i.get_menu_options()
#     for option in menu_options:
#         print(f"Menu Option: [ {option.get_key()} ] {option.get_label()}")
#         print(f"Menu Option Function: {option.get_func()}\n")
#     print(f"Previous Menu: {i.get_previous_menu()}\n")
#     print()
