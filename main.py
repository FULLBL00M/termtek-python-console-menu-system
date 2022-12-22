import os
import sys
import pprint
import modules.termtek as ttk

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

# _________________________________________________________________________________________________________________________________

def create_main_menu(settings_root=None):
    main_banner = ttk.build_fancy_font("[ Main Menu ]")
    main_menu_options = [
        ttk.ConsoleMenuOption("test1", "Test function one", testone),
        ttk.ConsoleMenuOption("test2", "Test funtion two", testtwo),
        ttk.ConsoleMenuOption("settings", "Change settings for the program", settings_root),
        ttk.ConsoleMenuOption("exit", "Exit the program", sys.exit)
    ]
    return ttk.ConsoleMenu(main_banner, main_menu_options)

def create_settings_menu(main_menu_root):
    settings_banner = ttk.build_fancy_font("[ Settings Menu ]")
    settings_menu_options = [
        ttk.ConsoleMenuOption("password", "Change your account password", settings_testone),
        ttk.ConsoleMenuOption("email", "Change your account email", settings_testtwo),
        ttk.ConsoleMenuOption("back", "Go back to main menu", main_menu_root)
    ]
    return ttk.ConsoleMenu(settings_banner, settings_menu_options, main_menu_root)

def create_all_menus():
    menu_objects = []
    main_menu_root = create_main_menu()
    settings_root = create_settings_menu(main_menu_root)

    menu_objects.append({
        "main_menu_object": main_menu_root
    })
    menu_objects.append({
        "settings_menu_object": settings_root
    })

    for option in menu_objects[0].get("main_menu_object").menu_options:
        if option.label == "Change settings for the program":
            option.func = settings_root.show_full
    return menu_objects

# _________________________________________________________________________________________________________________________________

def show_main_menu(menu_objects):
    menu_objects[0].get("main_menu_object").show_full()

if __name__ == "__main__":
    menu_objects = create_all_menus()
    show_main_menu(menu_objects)