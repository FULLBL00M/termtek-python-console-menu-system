# Termtek Python Module

```
fullbl00m@bl00mb0x:~/Desktop/golden-ai$ python3 main.py 

█▀▄▀█ ▄▀█ █ █▄░█    █▀▄▀█ █▀▀ █▄░█ █░█
█░▀░█ █▀█ █ █░▀█    █░▀░█ ██▄ █░▀█ █▄█

[ test1 ]: Test function one
[ test2 ]: Test funtion two
[ openai ]: Play with Openai API
[ settings ]: Change settings for the program
[ exit ]: Exit the program

Please select an option: exit

```


This is a simple diagram of the test menu structure that is currently in main.py

```
root_menu
|
|--- test1 (Test function one)
|--- test2 (Test function two)
|--- openai (Play with Openai API)
|     |--- test1 (Test openai function one)
|     |--- test2 (Test openai function two)
|     |--- aisettings (Change settings for openai)
|     |--- Go Back (Return to previous menu)
|           |--- test1 (Test openai settings function one)
|           |--- test2 (Test openai settings function two)
|           |--- Go Back (Return to previous menu)
|--- settings (Change settings for the program)
|     |--- password (Change your account password)
|     |--- email (Change your account email)
|     |--- Go Back (Return to previous menu)
|--- exit (Exit the program)

```

The goal of this project is to provide a simple to use menu system to inexperienced coders, while providing a dependable foundation for experienced developers to utilize aswell. 

The inspiration for this project was to simplify creation and maintenance of interconnected console menu programs.

Quality of life features:<br>
The back buttons will automatically map to the menu that called it so you don't have to worry about that.<br>
There is a verbose debugger that I built for myself but you can use it if you want to modify the module.
If you want just set Debug to True in modules/consolemodule.py or override it in main.py

The secret to its magic revolves around the fact that the menu_options you supply it can point to...

<ul>
    <li><b>Any Function Reference</b></li>
    <li><b>Any Menu Name</b></li>
</ul>

The menu_option is a List that is comprised of: [ <b>key</b>, <b>label</b>, <b>func</b> ]
<ul>
    <li>key: This is the keyword that the user will type to activate a menu_option in your program</li>
    <li>label: This is the text that will describe the action of your menu option</li>
    <li>func: This is the most important part of the project. This points to either a function to run or the name of another menu_name that you want to reference.</li>
</ul>

Below is an example of a menu block that you will supply the program in the main.py file.

```
root_menu = {
    "menu_name": "root_menu",                                                           # REQUIRED STRING
    "banner": ttk.build_fancy_font("Main Menu"),                                        # REQUIRED STRING
    "menu_options": [                                                                   # REQUIRED LIST
        ["test1", "Test function one", testone],
        ["test2", "Test funtion two", testtwo],
        ["openai", "Play with Openai API", {"goto": "openai_api_menu"}],
        ["settings", "Change settings for the program", {"goto": "settings_menu"}],
        ["exit", "Exit the program", exit]
    ]
}
```
As you can see in the example above the "menu_options" can point to either a python function as the 3rd argument, or you can use a goto that just points to another menu_name of your choosing and it will automatically handle the rest.

Another interesting thing to note is that I am using the ttk.build_fancy_font() function of the termtek module to return an ascii font of the string. Feel free to use it. I made it for you :p

# How to run
```
git clone git@github.com:FULLBL00M/termtek-python-console-menu-system.git
cd golden-ai/
python3 main.py
```

# How to edit
You should be able to figure out whats going on in the main.py file if you read these docs.
But the required steps are...

1) Create your menu blocks in main.py
2) Ensure they match the template structure
3) add all menu block vars to a list in the way you prefer
4) submit the List to the ttk.build_console_menu_objects(all_menus) function
5) set your default menu in the __main__ function

If you are looking at this for somereason and want to know more hit me up on discord.

<br>
Created by @fullbl00m#1224 on discord
           <br>@FULLBL00M on github

