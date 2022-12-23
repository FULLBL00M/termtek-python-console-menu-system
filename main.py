import pprint
import modules.termtek as ttk
from typing import List, Callable, Dict, Any
import modules.termtek.consolemenu as cm

def pp(arr):
    pprint.pprint(arr)
# _________________________________________________________________________________________________________________________________

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
#         "child_menu": [] # <=======| list of ConsoleMenuOption python objects
#     }
# ]

console_menus = [{
    "menu_name": "root_menu",
    "banner": "Main Menu",
    "menu_options": [
                [ "test1", "Test function one", testone ],
                [ "test2", "Test funtion two", testtwo ],
                [ "settings", "Change settings for the program", "settings_menu" ],
                [ "exit", "Exit the program", sys.exit ]
    ],
    "previous_menu": None,
    "child_menu": [
        {
            "menu_name": "openai_api_menu",
            "banner": "Openai Api Menu",
            "menu_options": [
                        [ "test1", "Test openai function one", testone ],
                        [ "test2", "Test openai funtion two", testtwo ],
                        [ "settings", "Change settings for openai", "openai_api_settings_menu" ],
                        [ "back", "Go back to main menu", "root_menu" ]
            ],
            "previous_menu": "root_menu",
            "child_menu": [
                {
                    "menu_name": "openai_api_settings_menu",
                    "banner": "Openai Api Settings Menu",
                    "menu_options": [
                                [ "test1", "Test openai settings function one", settings_testone ],
                                [ "test2", "Test openai settings funtion two", settings_testtwo ],
                                [ "back", "Go back to main menu", "openai_api_menu" ]
                    ],
                    "previous_menu": "openai_api_menu",
                    "child_menu": []
                }
            ]
        },
        {
            "menu_name": "settings_menu",
            "banner": "Settings Menu",
            "menu_options": [
                        [ "password", "Change your account password", settings_testone ],
                        [ "email", "Change your account email", settings_testtwo ],
                        [ "back", "Go back to main menu", "root_menu" ]
            ],
            "previous_menu": "root_menu",
            "child_menu": []
        }
    ]
}]

# _________________________________________________________________________________________________________________________________

# def create_main_menu(settings_root=None):
#     main_banner = ttk.build_fancy_font("[ Main Menu ]")
#     main_menu_options = [
#         ttk.ConsoleMenuOption("test1", "Test function one", testone),
#         ttk.ConsoleMenuOption("test2", "Test funtion two", testtwo),
#         ttk.ConsoleMenuOption("settings", "Change settings for the program", settings_root),
#         ttk.ConsoleMenuOption("exit", "Exit the program", sys.exit)
#     ]
#     return ttk.ConsoleMenu(main_banner, main_menu_options)

# def create_settings_menu(main_menu_root):
#     settings_banner = ttk.build_fancy_font("[ Settings Menu ]")
#     settings_menu_options = [
#         ttk.ConsoleMenuOption("password", "Change your account password", settings_testone),
#         ttk.ConsoleMenuOption("email", "Change your account email", settings_testtwo),
#         ttk.ConsoleMenuOption("back", "Go back to main menu", main_menu_root)
#     ]
#     return ttk.ConsoleMenu(settings_banner, settings_menu_options, main_menu_root)

# def create_all_menus():
#     menu_objects = []
#     main_menu_root = create_main_menu()
#     settings_root = create_settings_menu(main_menu_root)

#     menu_objects.append({
#         "main_menu_object": main_menu_root
#     })
#     menu_objects.append({
#         "settings_menu_object": settings_root
#     })

#     return menu_objects

# _________________________________________________________________________________________________________________________________

# def show_main_menu(menu_objects):
#     menu_objects[0].get("main_menu_object").show_full()

if __name__ == "__main__":

    def build_menus(menus: List[dict]) -> 'consoleMenu':
        def build_menu(menu: dict, parent_menu: 'consoleMenu' = None) -> 'consoleMenu':
            menu_options = []
            for option in menu['menu_options']:
                key, label, func = option
                menu_option = cm.consoleMenu.consoleMenuOption(key, label, func)
                menu_options.append(menu_option)

            # Insert "back" option if parent menu is not None
            if parent_menu is not None:
                menu_options.append(cm.consoleMenu.consoleMenuOption("back", f"Go back to {parent_menu.banner}", parent_menu.show_full))

            current_menu = cm.consoleMenu(menu['banner'], menu_options, menu['previous_menu'])
            for child in menu['child_menu']:
                child_menu = build_menu(child, current_menu)  # <-- Pass current menu as parent_menu for each child
                child_menu.set_previous_menu(current_menu)
                current_menu.menu_options.append(cm.consoleMenu.consoleMenuOption(child['menu_name'], child['banner'], child_menu.show_full))
            return current_menu

        root_menu = build_menu(menus[0])
        return root_menu

