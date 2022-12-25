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

root_menu = {
    "menu_name": "root_menu",
    "banner": "Main Menu",
    "menu_options": [
        ["test1", "Test function one", testone],
        ["test2", "Test funtion two", testtwo],
        ["openai", "Play with Openai API", {"goto": "openai_api_menu"}],
        ["settings", "Change settings for the program", {"goto": "settings_menu"}],
        ["exit", "Exit the program", exit]
    ]
}
all_menus.append(root_menu)

openai_api_menu = {
    "menu_name": "openai_api_menu",
    "banner": "Openai Api Menu",
    "menu_options": [
        ["test1", "Test openai function one", testone],
        ["test2", "Test openai funtion two", testtwo],
        ["aisettings", "Change settings for openai", {"goto": "openai_api_settings_menu"}]
    ]
}
all_menus.append(openai_api_menu)

settings_menu = {
    "menu_name": "settings_menu",
    "banner": "Settings Menu",
    "menu_options": [
        ["password", "Change your account password", settings_testone],
        ["email", "Change your account email", settings_testtwo]
    ]
}
all_menus.append(settings_menu)

openai_api_settings_menu = {
    "menu_name": "openai_api_settings_menu",
    "banner": "Openai Api Settings Menu",
    "menu_options": [
        ["test1", "Test openai settings function one", settings_testone],
        ["test2", "Test openai settings funtion two", settings_testtwo]
    ]
}
all_menus.append(openai_api_settings_menu)



###
# DONT FORGET TO MAKE THE child_menus AUTOMATICALLY POPULATE BASED ON THE GOTOS IN THE MENU OPTIONS
# DONT FORGET TO AUTOMATICALLY ADD A BACK OPTION TO THE PREVIOUS MENU
# DONT FORGET TO MAKE THE previous_menu AUTOMATICALLY POPULATE BASED ON THE GOTOS IN THE MENU OPTIONS
###


def build_console_menu_objects(all_menus):

    def init_menus(all_menus):
        print(ttk.colorize("\n[ INITIALIZING MENUS ]\n", "blue"))
        for menu in all_menus:
            # menu["previous_menu_object"] = []
            # menu["child_menu_objects"] = []
            menu["console_menu_object"] = cm.ConsoleMenu(menu["menu_name"], menu["banner"])
            if debug:
                create_str = ttk.colorize("    [ CREATED ]", "green")
                str = create_str + f' {menu["menu_name"]} ------ {menu["console_menu_object"]}'
                print(ttk.colorize(str, "green"))

    def set_previous_menus(all_menus):
        print(ttk.colorize("\n[ SETTING PREVIOUS MENUS ]\n", "blue"))
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
        print(ttk.colorize("\n[ SWAPPING GOTO WITH FUNCTIONS ]", "blue"))
        found_goto_count = 0
        found_goto = False
        for menu in all_menus:
            print(ttk.colorize("\n[ MENU ]", "cyan") + f" {menu['menu_name']}")
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
                    print(ttk.colorize("\n    [ FOUND GOTO ]", "green"))
                    print(f"        goto_menu_name: {goto_menu_name}")
                    print(f"        called_menu_object: {called_menu_object}")
                    print(f"        called_menu_object.get_menu_name(): {called_menu_object.get_menu_name()}")
                    print(f"        called_menu_object.show_full: {called_menu_object.show_full}")
                    debug_action = ttk.colorize("    [ GOTO SWAP ]", "green")
                    print(f"\n{debug_action}\n        og menu_option:\n        {option}")

                    option[2] = called_menu_object.show_full
                    print(f"        new menu_option:\n        {option}")

                if not found_goto:
                    debug_action = ttk.colorize("    [ NO GOTO FOUND ]", "yellow")
                    print(f"\n{debug_action}\n        menu_option:\n        {option}")
                found_goto = False
    
    def add_back_button_options(all_menus):
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

    def add_final_menu_options(all_menus):
        print(ttk.colorize("\n[ ADDING FINAL MENU OPTIONS ]", "blue"))
        for menu in all_menus:
            print(ttk.colorize("\n[ MENU ]", "cyan") + ttk.colorize(f" {menu['menu_name']}", "green"))
            
            new_option_objects = []

            for option in menu["menu_options"]:
                new_object = cm.ConsoleMenuOption(option[0], option[1], option[2])
                new_option_objects.append(new_object)
                print(ttk.colorize("\n    [ NEW CONSOLE MENU OPTION OBJECT ]", "green"))
                print(f"        new_object: {new_object}")

            menu["console_menu_object"].set_menu_options(new_option_objects)
            
            check = []
            option_objects = menu["console_menu_object"].get_menu_options()
            for obj in option_objects:
                check.append(obj.get_all())

            # print(f'CHECK: {check}')
            # print(f'MENU OPTIONS: {menu["menu_options"]}')

            if check == menu["menu_options"]:
                print(ttk.colorize("[ FINAL OPTIONS SET SUCCESSFULLY ]", "green"))
    
    def debug_menu_info(all_menus):
        print(ttk.colorize("\n[ DEBUG MENU INFO ]\n", "blue"))
        for menu in all_menus:
            print(ttk.colorize("[ MENU ]", "cyan") + f" {menu['menu_name']}")
            print(f'all_menus["menu_name"] => {menu["menu_name"]}')
            print(f'all_menus["banner"] => {menu["banner"]}')
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
    debug_menu_info(all_menus)

build_console_menu_objects(all_menus)

for menu in all_menus:
    if menu["menu_name"] == "root_menu":
        menu["console_menu_object"].show_full()

    


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
