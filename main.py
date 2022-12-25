import modules.termtek as ttk
import sys

def testone():
    print(ttk.build_fancy_font("Test one"))
    print()

def testtwo():
    print(ttk.build_fancy_font("Test two"))
    print()

def settings_testone():
    print(ttk.build_fancy_font("Settings test one"))
    print()

def settings_testtwo():
    print(ttk.build_fancy_font("Settings test two"))
    print()

def exit():
    sys.exit()

all_menus = []

root_menu = {
    "menu_name": "root_menu",
    "banner": ttk.build_fancy_font("Main Menu"),
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
    "banner": ttk.build_fancy_font("Openai Api Menu"),
    "menu_options": [
        ["test1", "Test openai function one", testone],
        ["test2", "Test openai funtion two", testtwo],
        ["aisettings", "Change settings for openai", {"goto": "openai_api_settings_menu"}]
    ]
}
all_menus.append(openai_api_menu)

settings_menu = {
    "menu_name": "settings_menu",
    "banner": ttk.build_fancy_font("Settings Menu"),
    "menu_options": [
        ["password", "Change your account password", settings_testone],
        ["email", "Change your account email", settings_testtwo]
    ]
}
all_menus.append(settings_menu)

openai_api_settings_menu = {
    "menu_name": "openai_api_settings_menu",
    "banner": ttk.build_fancy_font("Openai Api Settings Menu"),
    "menu_options": [
        ["test1", "Test openai settings function one", settings_testone],
        ["test2", "Test openai settings funtion two", settings_testtwo]
    ]
}
all_menus.append(openai_api_settings_menu)

# If this module is the main module being run (not imported by another script)
if __name__ == "__main__":

    ttk.build_console_menu_objects(all_menus)

    for menu in all_menus:
        if menu["menu_name"] == "root_menu":
            menu["console_menu_object"].show_full()
