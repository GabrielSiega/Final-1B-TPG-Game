import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import ttk  # Add this line for importing ttk






def Button_1_command():
    print("Basic Attack command", f"deals:-{Swordsman.dp} Damage to")  # "damage to enemy character name "

def Button_2_command():
    print("User pressed Defend Button")

def Button_3_command():
    print("User pressed HP potion Button")

def Button_4_command():
    print("User pressed Special Skill Button")

def Button_5_command():
    print("User pressed Settings button Button")
    

def button6_command():
    global game_window, selected_character, selected_enemy
    
    print("User pressed Restart Button")
    
    # Destroy the current game window, if exists
    if game_window:
        game_window.destroy()
        
    selected_character = None
    selected_enemy = None
    
    create_character_selection_buttons()
    
    
def Button_7_command():
    print("User pressed Exit")
    print()
    print("Game Closed")
    

def create_button(root, text, x, y, command):
    button = tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Times', size=10), fg="#000000", justify="center", text=text, command=command)
    button.place(x=x, y=y, width=120, height=34)

def create_text(root, text, x, y):
    label = tk.Label(root, font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center", text=text)
    label.place(x=x, y=y, width=85, height=25)

def create_message(root, text, x, y):
    message = tk.Message(root, font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center", text=text)
    message.place(x=x, y=y, width=80, height=25)

class Character():
    def __init__(self, name, hp, ap, dp, sp, mp):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.dp = dp
        self.sp = sp
        self.mp = mp

def chosen_character():
    characters = {
        '1': Character('Swordsman', 75, 14, 61, 15, 3),
        '2': Character('Rizzard', 100, 10, 90, 10, 7),
        '3': Character('Knight', 110, 12, 88, 5, 3),
        '4': Character('Thief', 90, 15, 75, 15, 3)
    }
    return characters

def choose_enemy():
    enemies = {
        '1': Character('Swordsman', 75, 14, 61, 15, 3),
        '2': Character('Rizzard', 100, 10, 90, 10, 7),
        '3': Character('Knight', 110, 12, 88, 5, 3),
        '4': Character('Thief', 90, 15, 75, 15, 3)
    }
    return enemies

Swordsman = chosen_character()['1']
Rizzard = chosen_character()['2']
Knight = chosen_character()['3']
Thief = chosen_character()['4']






#selected_character = '1' #Swordsman
#selected_enemy = '3'  # For example, assuming the enemy is 'Knight'


class Character():
    def __init__(self, name, hp, ap, dp, sp, mp):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.dp = dp
        self.sp = sp
        self.mp = mp

    def get_character_info(self):
        print("Character Info for:", self.name)
        print("Hp:", self.hp)
        print("Ap:", self.ap)
        print("Dp:", self.dp)
        print("Sp:", self.sp)
        print("Mp:", self.mp)

    def display_character_info(self, x, y):
        print("Displaying Character Info on Game Window:")
        print("Character:", self.name)
        print("Hp:", self.hp)
        print("Ap:", self.ap)
        print("Dp:", self.dp)
        print("Sp:", self.sp)
        print("Mp:", self.mp)

    def display_enemy_info(self, x, y):  # Add this method for enemies
        print("Displaying Enemy Info on Game Window:")
        print("Enemy:", self.name)
        print("Hp:", self.hp)
        print("Ap:", self.ap)
        print("Dp:", self.dp)
        print("Sp:", self.sp)
        print("Mp:", self.mp)

characters = {
    '1': Character('Swordsman', 75, 14, 61, 15, 3),
    '2': Character('Rizzard', 100, 10, 90, 10, 7),
    '3': Character('Knight', 110, 12, 88, 5, 3),
    '4': Character('Thief', 90, 15, 75, 15, 3)
}

def get_selected_character(selected):
    return characters.get(selected, None)




next_window= None


image1 = None
image2 = None
bg_photo = None  # Declare bg_photo as a global variable


selected_character = None
selected_enemy = None
character_selection_window = None
enemy_selection_window = None
game_window = None
selected_character_label = None

selected_character = None  # Variable to store the user's selected character
selected_enemy = None  # Variable to store the user's selected enemy
character_selection_window = None  # Global variable for character selection window
enemy_selection_window = None  # Global variable for enemy selection window
game_window = None  # Global variable for the game window
selected_character_label = None  # Global variable for the label displaying the selected character

def enter_game():
    name = name_entry.get().strip()
    
    #If my name: Gabriel (print "Welcome Creator!" & If Mr Tan (print "Welcome Teacher"))
    if name == 'Gabriel' and name.isalpha():
        print("True")
        messagebox.showinfo(title="Login Success", message=f"Welcome Creator!")
        window.withdraw() #hide login window
        create_character_selection_buttons() #Show char. selection buttons
        
    elif name == 'Mrtan' and name.isalpha():
        print("True")
        messagebox.showinfo(title="Login Success", message=f"Welcome Teacher!")
        window.withdraw() #hide login window
        create_character_selection_buttons() #Show char. selection buttons
    
    
    #if name and name.isalpha():
    #    messagebox.showinfo(title="Login Success", message=f"Welcome, {name}!")
    #    window.withdraw()  # Hide the login window
    #    create_character_selection_buttons()  # Show character selection buttons
    else:
        messagebox.showerror(title="Error", message="Please enter a valid name containing only alphabetic characters.")
        
        

def create_character_selection_buttons():  # Character Choice Window
    global character_selection_window, selected_character_label  # Declare selected_character_label as global

    # Destroy the previous character selection window, if exists
    if character_selection_window:
        character_selection_window.destroy()

    # Create character selection window as a Toplevel window
    character_selection_window = tk.Toplevel(window)
    character_selection_window.title("Character Selection Window")

    # Set the window size and position it at the center of the screen
    window_width = 800
    window_height = 600
    screen_width = character_selection_window.winfo_screenwidth()
    screen_height = character_selection_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    character_selection_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Create character selection buttons
    character_names = ["Swordsman", "Rizzard", "Knight", "Thief"]

    # Create a heading label for character choice
    character_heading = tk.Label(character_selection_window, text="Choose your character:", font=("Arial", 20))
    character_heading.pack(pady=20)

    for i, character_name in enumerate(character_names):
        character_button = tk.Button(character_selection_window, text=character_name, font=("Arial", 16), command=lambda name=character_name: character_selected(name))
        character_button.pack(pady=10)

    # Add a label to display the selected character
    selected_character_label = tk.Label(character_selection_window, text="Selected Character: None", font=("Arial", 16))
    selected_character_label.pack(pady=10)

    # Add a return button to go back to the main login window
    return_button = tk.Button(character_selection_window, text="Return to Login", font=("Arial", 16), command=return_to_login, bg="black", fg="white")
    return_button.pack(pady=10)

def return_to_login():
    global character_selection_window, selected_character, game_window  # Declare game_window as global

    if game_window:
        game_window.destroy()  # Destroy the game window, if exists

    if character_selection_window:
        character_selection_window.destroy()  # Destroy the character selection window

    selected_character = None  # Reset the selected character
    print("User went back to the login window")
    window.deiconify()  # Show the main login window again

def return_to_character_selection():
    global game_window

    if game_window:
        game_window.destroy()  # Destroy the game window, if exists

    create_character_selection_buttons()  # Show the character selection window again

def character_selected(character_name):
    global selected_character, character_selection_window, selected_character_label  # Declare selected_character_label as global

    if selected_character is None:
        selected_character = character_name
        selected_character_label.config(text=f"Selected Character: {selected_character}")
        messagebox.showinfo(title="Character Selected", message=f"You have chosen {character_name}!")
        if character_selection_window:
            character_selection_window.destroy()  # Destroy the character selection window
        create_enemy_choice_window()
    else:
        messagebox.showinfo(title="Character Already Chosen", message="You have already chosen a character! Return To the Home Page to Restart")





def create_enemy_choice_window():
    global enemy_selection_window

    # Destroy the previous enemy selection window, if exists
    if enemy_selection_window:
        enemy_selection_window.destroy()

    # Create the enemy choice window as a Toplevel window
    enemy_selection_window = tk.Toplevel(window)
    enemy_selection_window.title("Enemy Choice Window")

    # Set the window size and position it at the center of the screen
    window_width = 800
    window_height = 600
    screen_width = enemy_selection_window.winfo_screenwidth()
    screen_height = enemy_selection_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    enemy_selection_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Create enemy selection buttons
    enemy_names = ["Swordsman", "Rizzard", "Knight", "Thief"]

    # Create a heading label for enemy choice
    enemy_heading = tk.Label(enemy_selection_window, text="Choose your enemy:", font=("Arial", 20))
    enemy_heading.pack(pady=20)

    for i, enemy_name in enumerate(enemy_names):
        enemy_button = tk.Button(enemy_selection_window, text=enemy_name, font=("Arial", 16), command=lambda name=enemy_name: enemy_selected(name))
        enemy_button.pack(pady=10)

    # Add a label to display the selected character
    selected_enemy_label = tk.Label(enemy_selection_window, text="Selected Enemy: None", font=("Arial", 16))
    selected_enemy_label.pack(pady=10)

    # Add a return button to go back to the character selection window
    return_button = tk.Button(enemy_selection_window, text="Return to Character Selection", font=("Arial", 16), command=return_to_character_selection, bg="black", fg="white")
    return_button.pack(pady=10)

def enemy_selected(enemy_name):
    global selected_enemy, enemy_selection_window

    selected_enemy = enemy_name
    messagebox.showinfo(title="Enemy Selected", message=f"You are now facing {enemy_name} as your enemy!")
    if enemy_selection_window:
        enemy_selection_window.destroy()  # Destroy the enemy selection window
    create_game_page()

def create_game_page():
    global selected_enemy

    # Create the game page as a Toplevel window
    game_page = tk.Toplevel(window)
    game_page.title("User's Character and Enemy Choice")

    # Set the window size and position it at the center of the screen
    window_width = 800
    window_height = 600
    screen_width = game_page.winfo_screenwidth()
    screen_height = game_page.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    game_page.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Create a label to display the selected enemy
    selected_enemy_label = tk.Label(game_page, text=f"Selected Enemy: {selected_enemy}", font=("Arial", 20))
    selected_enemy_label.pack(pady=50)
    
    selected_character_label = tk.Label(game_page, text=f"Vs", font=("Arial", 20))
    selected_character_label.pack(pady=80)
    
    selected_character_label = tk.Label(game_page, text=f"Selected Character: {selected_character}", font=("Arial", 20))
    selected_character_label.pack(pady=50)
    
     # Create a "Next" button
    next_button = tk.Button(game_page, text="Next", font=("Arial", 16), command=next_button_command)
    next_button.pack(pady=20)

## selected_enemy
## selected_character
#test print



def next_button_command():
    print("User clicked 'next' button")
    print()
    if game_window:
        game_window.destroy()
    create_game_window()

round_counter = 0



def create_game_window():
    global maingamewindow
    

    # Create the next window as a Toplevel window
    next_window = tk.Toplevel(window)
    next_window.title("TPG User's Choice")

    # Set the window size and position it at the center of the screen
    window_width = 800
    window_height = 600
    screen_width = next_window.winfo_screenwidth()
    screen_height = next_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    next_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    
    print(f"Selected Character: {selected_character}")
    print(f"Selected Enemy: {selected_enemy}")
    
    

    # Create content for the next window
    next_label = tk.Label(next_window, text="Start Game", font=("Arial", 20))
    next_label.place(x=350,y=100)
    
     # Create a "Next" button
    next_button = tk.Button( next_window, text="Start", font=("Arial", 16), command=next_button_command_next)
    next_button.place(x=350,y=200)
    
def next_button_command_next():
    
    print("User clicked 'Start' button")
    print()
    if game_window:  # Use the actual Toplevel window variable
        game_window.destroy()
    create_tpg_game_window()




def button1_command():
    print("Presed Basic Attack Button")
    
    
def button2_command():
    print("Presed Defend Button")
    
def button3_command():
    print("Presed Hp potion Button")
    
def button4_command():
    print("Presed Special Skill Button")
    
def button5_command():
    print("Presed Settings Button")
    
def button6_command():
    global game_window, selected_character, selected_enemy
    
    print("User pressed Restart Button")
    
    # Destroy the current game window, if exists
    if game_window:
        game_window.destroy()
        
    selected_character = None
    selected_enemy = None
    
    create_character_selection_buttons()
    
def button7_command():
    print("Presed Exit Button")
    print()
    print("Game Closed")
    window.destroy()



#Character Photo Path
character_1_swordsman_path = "C:/TPG Game Zip Files/Game Design/LightBandit_Idle_0.png" 
character_2_rizzard_path = "C:/TPG Game Zip Files/Game Design/LightBandit_Idle_0.png" 
character_3_knight_path = "C:/TPG Game Zip Files/Game Design/HeroKnight_Idle_0.png" 
character_4_thief_path = "C:/TPG Game Zip Files/Game Design/HeavyBandit_Idle_0.png" 




def create_tpg_game_window():
    global game_window, bg_photo, user_character_photo, user_enemy_photo,selected_character, selected_enemy



    if game_window:
        game_window.destroy()

    game_window = tk.Toplevel(window)
    game_window.title("TPG Game")

    window_width = 800
    window_height = 600
    screen_width = game_window.winfo_screenwidth()
    screen_height = game_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    game_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    character_image_path = None
    enemy_image_path = None

    if selected_character == '1':
        character_image_path = character_1_swordsman_path
    elif selected_character == '2':
        character_image_path = character_2_rizzard_path
    elif selected_character == '3':
        character_image_path = character_3_knight_path
    elif selected_character == '4':
        character_image_path = character_4_thief_path

    if selected_enemy == '1':
        enemy_image_path = character_1_swordsman_path
    elif selected_enemy == '2':
        enemy_image_path = character_2_rizzard_path
    elif selected_enemy == '3':
        enemy_image_path = character_3_knight_path
    elif selected_enemy == '4':
        enemy_image_path = character_4_thief_path

    bg_image_path = "C:/TPG Game Zip Files/Game Design/background2.png"
    bg_image = Image.open(bg_image_path)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(game_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    

    if character_image_path:
        character_image = Image.open(character_image_path)
        character_image = character_image.resize((100, 100), Image.LANCZOS)
        user_character_photo = ImageTk.PhotoImage(character_image)
        character_image_label = tk.Label(game_window, image=user_character_photo)
        character_image_label.place(x=300, y=95)

    if enemy_image_path:
        enemy_image = Image.open(enemy_image_path)
        enemy_image = enemy_image.resize((100, 100), Image.LANCZOS)
        user_enemy_photo = ImageTk.PhotoImage(enemy_image)
        enemy_image_label = tk.Label(game_window, image=user_enemy_photo)
        enemy_image_label.place(x=520, y=95)
        
        
    print()
    
    
    print(f"{selected_character}") #swordsman
    print(f"{selected_enemy}") #swordsman


    #create_message(game_window, f"Hp:{}", 70, 300)
    #create_message(game_window, f"Ap:{}", 180, 300)
    #create_message(game_window, f"Dp:{enemy_game_window_dp}", 290, 300)  # Row 2
    #create_message(game_window, f"Sp:{enemy_game_window_sp}", 410, 300)  # Row 2
    #create_message(game_window, f"Mp:{enemy_game_window_mp}", 520, 300)  # Row 2
    
    ##
    #YOUR CHARACTER STATS

    if selected_character == 'Swordsman':
     print("You are using a Swordsman")
     print("hp:",Swordsman.hp)
     create_message(game_window, f"Hp:{Swordsman.hp}", 70, 300)
     create_message(game_window, f"Ap:{Swordsman.ap}", 180, 300)
     create_message(game_window, f"Dp:{Swordsman.dp}", 290, 300)
     create_message(game_window, f"Sp:{Swordsman.sp}", 410, 300) 
     create_message(game_window, f"Mp:{Swordsman.mp}", 520, 300)
    
    elif selected_character == 'Rizzard':
     print("You are using a Rizzard")
     print("hp:",Rizzard.hp)
     create_message(game_window, f"Hp:{Rizzard.hp}", 70, 300)
     create_message(game_window, f"Ap:{Rizzard.ap}", 180, 300)
     create_message(game_window, f"Dp:{Rizzard.dp}", 290, 300)
     create_message(game_window, f"Sp:{Rizzard.sp}", 410, 300) 
     create_message(game_window, f"Mp:{Rizzard.mp}", 520, 300)
    
    elif selected_character == 'Knight':
     print("You are using a Knight")
     print("hp:",Knight.hp)
     create_message(game_window, f"Hp:{Knight.hp}", 70, 300)
     create_message(game_window, f"Ap:{Knight.ap}", 180, 300)
     create_message(game_window, f"Dp:{Knight.dp}", 290, 300)
     create_message(game_window, f"Sp:{Knight.sp}", 410, 300) 
     create_message(game_window, f"Mp:{Knight.mp}", 520, 300)
    
    elif selected_character == 'Thief':
     print("You are using a Thief")
     print("hp:",Thief.hp)
     create_message(game_window, f"Hp:{Thief.hp}", 70, 300)
     create_message(game_window, f"Ap:{Thief.ap}", 180, 300)
     create_message(game_window, f"Dp:{Thief.dp}", 290, 300)
     create_message(game_window, f"Sp:{Thief.sp}", 410, 300) 
     create_message(game_window, f"Mp:{Thief.mp}", 520, 300)
     
    ##
    ##ENEMY STATS
    
    if selected_enemy == 'Swordsman':
     print("You are using a Swordsman")
     print("hp:",Swordsman.hp)
     create_message(game_window, f"Hp:{Swordsman.hp}", 70, 240)
     create_message(game_window, f"Ap:{Swordsman.ap}", 180, 240)
     create_message(game_window, f"Dp:{Swordsman.dp}", 290, 240)
     create_message(game_window, f"Sp:{Swordsman.sp}", 410, 240) 
     create_message(game_window, f"Mp:{Swordsman.mp}", 520, 240)
    
    elif selected_enemy == 'Rizzard':
     print("You are using a Rizzard")
     print("hp:",Rizzard.hp)
     create_message(game_window, f"Hp:{Rizzard.hp}", 70, 240)
     create_message(game_window, f"Ap:{Rizzard.ap}", 180, 240)
     create_message(game_window, f"Dp:{Rizzard.dp}", 290, 240)
     create_message(game_window, f"Sp:{Rizzard.sp}", 410, 240) 
     create_message(game_window, f"Mp:{Rizzard.mp}", 520, 240)
    
    elif selected_enemy == 'Knight':
     print("You are using a Knight")
     print("hp:",Knight.hp)
     create_message(game_window, f"Hp:{Knight.hp}", 70, 240)
     create_message(game_window, f"Ap:{Knight.ap}", 180, 240)
     create_message(game_window, f"Dp:{Knight.dp}", 290, 240)
     create_message(game_window, f"Sp:{Knight.sp}", 410, 240) 
     create_message(game_window, f"Mp:{Knight.mp}", 520, 240)
    
    elif selected_enemy == 'Thief':
     print("You are using a Thief")
     print("hp:",Thief.hp)
     create_message(game_window, f"Hp:{Thief.hp}",  70, 240)
     create_message(game_window, f"Ap:{Thief.ap}", 180, 240)
     create_message(game_window, f"Dp:{Thief.dp}", 290, 240)
     create_message(game_window, f"Sp:{Thief.sp}", 410, 240) 
     create_message(game_window, f"Mp:{Thief.mp}", 520, 240)
    
    
    #sm vs sm
    if selected_character == 'Swordsman' and selected_enemy == 'Swordsman':
     print()
     print("sm vs sm")
     create_message(game_window, f"Your Character Starts first")
     
     play_game()    
    
    
    def play_game():
        global round_counter
        remaining_heals = 7  # Number of remaining heals for Health Potion
        remaining_special_skills = 7  # Number of remaining special skills (self-healing using MP)
        remaining_special_skill_harden = 3  # Number of remaining Harden skills
        remaining_special_skill_buff = 3  # Number of remaining HP Buff skills
        remaining_special_skill_knife_stab = 3  # Number of remaining Knife Stab skills
        
        if button1_command == 1:
            print("Button is true")
            print(f"attacks:{Swordsman.ap} to {Swordsman.name}")
        Swordsman.hp -= Swordsman.ap
        
    
    
    
    
    
    
      # if sp_stat_s > sp_stat_s_e:
   #     print()
   #     print("Your Character has more SP")
   #     print("Character STARTS first")
   # elif sp_stat_s_e > sp_stat_s:
   #     print()
   #     print("Character has lesser SP")
   #     print("Enemy STARTS first!")
   #     print()
   #     print("Enemy uses basic attack")
   #     print(f"Attacks: {ap_stat_s_e} AP to {selected_character}")
   #     hp_stat_s -= ap_stat_s_e
   #     print()
   #     print(f"Enemy HP: {hp_stat_s_e}  Your HP: {hp_stat_s}")
   #     round_counter += 1
   #     print(f"End of Round {round_counter}")
    
    
    
    
    #
    #
    #
    
    
    
    #
    #
    #
    #
    
    
    
    #
    #
    #
    #
        
    
    # Create message labels for enemy character stats
    #create_message(game_window, f"Hp:{game_window_hp}", 70, 240)  # Row 1
    #create_message(game_window, f"Ap:{game_window_ap}", 180, 240)  # Row 1
    #create_message(game_window, f"Dp:{game_window_dp}", 290, 240)  # Row 1
    #create_message(game_window, f"Sp:{game_window_sp}", 410, 240)  # Row 1
    #create_message(game_window, f"Mp:{game_window_mp}", 520, 240)  # Row 1

    # Create message labels for user character stats
    #create_message(game_window, f"Hp:{}", 70, 300)
    #create_message(game_window, f"Ap:{}", 180, 300)
    #create_message(game_window, f"Dp:{enemy_game_window_dp}", 290, 300)  # Row 2
    #create_message(game_window, f"Sp:{enemy_game_window_sp}", 410, 300)  # Row 2
    #create_message(game_window, f"Mp:{enemy_game_window_mp}", 520, 300)  # Row 2
    
    
       
       
       
       
       
       
       
    print()
    global round_counter
    round_counter = 0
    
    
    #SP and HP
    #your stat (hp)
   # sp_stat_s = sp_stat_s_e
   # sp_stat_r = sp_stat_r_e
   # sp_stat_k = sp_stat_k_e
   # sp_stat_t = sp_stat_t_e
    
    
    #your stat (sp)
   # hp_stat_s = hp_stat_s_e
   # hp_stat_r = hp_stat_r_e
   # hp_stat_k = hp_stat_k_e
   # hp_stat_t = hp_stat_t_e
    
    
    
    
    
    
    #qty. for skills and potion use
    
    remaining_heals = 7  # Number of remaining heals for Health Potion
    remaining_special_skills = 7  # Number of remaining special skills (self-healing using MP)
    remaining_special_skill_harden = 3  # Number of remaining Harden skills
    remaining_special_skill_buff = 3  # Number of remaining HP Buff skills
    remaining_special_skill_knife_stab = 3  # Number of remaining Knife Stab skills
    
    
    
    
        
    
        
    
       
        
        
 
    
    

    




       
       
       
       
       
       
       
       
       
       
       
   # print()
  #  global round_counter
   # round_counter = 0
    
    
    #SP and HP
    #your stat (hp)
   # sp_stat_s = sp_stat_s_e
   # sp_stat_r = sp_stat_r_e
   # sp_stat_k = sp_stat_k_e
   # sp_stat_t = sp_stat_t_e
    
    
    #your stat (sp)
   # hp_stat_s = hp_stat_s_e
   # hp_stat_r = hp_stat_r_e
   # hp_stat_k = hp_stat_k_e
   # hp_stat_t = hp_stat_t_e
    
    
 
        
    
       
        
        
 
    
    
    
    # Create text labels to display character actions
    #create_text(game_window, f"- {game_window_ap} Damage", 230, 360)
    #create_text(game_window, f"Defends: +{game_window_dp} hp", 230, 410)
    #create_text(game_window, "Use Potion", 230, 460)
    #create_text(game_window, "Special Skill", 230, 510)

    # Create message labels for character and enemy descriptions
    create_message(game_window, f"Enemy:{selected_enemy}", 120, 200)
    create_message(game_window, f"You:{selected_character}", 120, 270)  # Between Row 1 & 2
    create_message(game_window, "VS", 420, 140)

    # Create message labels for enemy character stats
    #create_message(game_window, f"Hp:{game_window_hp}", 70, 240)  # Row 1
    #create_message(game_window, f"Ap:{game_window_ap}", 180, 240)  # Row 1
    #create_message(game_window, f"Dp:{game_window_dp}", 290, 240)  # Row 1
    #create_message(game_window, f"Sp:{game_window_sp}", 410, 240)  # Row 1
    #create_message(game_window, f"Mp:{game_window_mp}", 520, 240)  # Row 1

    # Create message labels for user character stats
    #create_message(game_window, f"Hp:{}", 70, 300)
    #create_message(game_window, f"Ap:{}", 180, 300)
    #create_message(game_window, f"Dp:{enemy_game_window_dp}", 290, 300)  # Row 2
    #create_message(game_window, f"Sp:{enemy_game_window_sp}", 410, 300)  # Row 2
    #create_message(game_window, f"Mp:{enemy_game_window_mp}", 520, 300)  # Row 2



        
        
        
        

# Create buttons in the game window
    button1 = tk.Button(game_window, text="Basic Attack", font=("Arial", 10), command = button1_command)
    button1.place(x=100, y=350)

    button2 = tk.Button(game_window, text="Defend", font=("Arial", 10), command = button2_command)
    button2.place(x=100, y=400)

    button3 = tk.Button(game_window, text="Hp Potion", font=("Arial", 10), command = button3_command)
    button3.place(x=100, y=450)

    button4 = tk.Button(game_window, text="Special Skill", font=("Arial", 10), command = button4_command)
    button4.place(x=100, y=500)
    
    button5 = tk.Button(game_window, text="Settings", font=("Arial", 10),command=open_settings_window )
    button5.place(x=400, y=400)
    
    button6 = tk.Button(game_window, text="Restart", font=("Arial", 10),command = button6_command)
    button6.place(x=400, y=440)
    
    button7 = tk.Button(game_window, text="Exit", font=("Arial", 10), command= button7_command)
    button7.place(x=400, y=480)
    
    
    
    
    
  
def create_audio_controls(root, audio_on):
    audio_label = tk.Label(root, text="Audio:", font=("Arial", 12))
    audio_label.place(x=20, y=20)

    audio_on_button = tk.Radiobutton(root, text="On", variable=audio_on, value=True)
    audio_on_button.place(x=80, y=20)

    audio_off_button = tk.Radiobutton(root, text="Off", variable=audio_on, value=False)
    audio_off_button.place(x=120, y=20)

def create_language_dropdown(root, language):
    language_label = tk.Label(root, text="Language:", font=("Arial", 12))
    language_label.place(x=20, y=60)

    languages = ["English", "Spanish", "French", "German"]
    language_dropdown = ttk.Combobox(root, textvariable=language, values=languages)
    language_dropdown.place(x=120, y=60)

def create_difficulty_slider(root, difficulty_level):
    difficulty_label = tk.Label(root, text="Difficulty Level:", font=("Arial", 12))
    difficulty_label.place(x=20, y=100)

    difficulty_slider = tk.Scale(root, variable=difficulty_level, from_=1, to=10, orient="horizontal")
    difficulty_slider.place(x=150, y=100)

    difficulty_value_label = tk.Label(root, textvariable=difficulty_level)
    difficulty_value_label.place(x=300, y=100)

def load_and_display_image(root):
    image_path = "C:/TPG Game Zip Files/Game Design/background3.png"  # Replace with the path to your image
    image = Image.open(image_path)
    image = image.resize((200, 200))  # Resize the image if needed
    image_tk = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=image_tk)
    image_label.place(x=400, y=20)  # Adjust the x and y values as needed

def create_buttons(root):
    button_6 = tk.Button(root, text="Restart", font=("Arial", 12), command=button6_command)
    button_6.place(x=20, y=160, width=100, height=30)

    button_7 = tk.Button(root, text="Quit", font=("Arial", 12), command=button7_command)
    button_7.place(x=130, y=160, width=100, height=30)

    
    
    
def open_settings_window():
    
    settings_window = tk.Toplevel(window)
    settings_window.title("Settings")

    # Set the window size and position it at the center of the screen
    window_width = 800
    window_height = 600
    screen_width = settings_window.winfo_screenwidth()
    screen_height = settings_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    settings_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Add settings options
    #label = tk.Label(settings_window, text="Settings", font=("Arial", 20))
    #label.pack(pady=20)

    # Add more settings widgets as needed

   
    # Add an "Audio" label
    audio_label = tk.Label(settings_window, text="Audio", font=("Arial", 20))
    audio_label.pack(pady=20)
    
    audio_control_var = tk.BooleanVar(value=True)
    audio_on_button = tk.Radiobutton(settings_window, text="On", variable=audio_control_var, value=True)
    audio_on_button.pack()

    audio_off_button = tk.Radiobutton(settings_window, text="Off", variable=audio_control_var, value=False)
    audio_off_button.pack()
   
    
    
    
    
    # Add a "Language" label
    language_label = tk.Label(settings_window, text="Language", font=("Arial", 20))
    language_label.pack(pady=20)
    
    # Language options for the dropdown
    language_options = ["English", "Spanish", "Japanese", "Chinese"]
    selected_language = tk.StringVar(value="English")
    
    # Create the language dropdown
    language_dropdown = tk.OptionMenu(settings_window, selected_language, *language_options)
    language_dropdown.pack()
    
    
    
    
    # Add a "Difficulty Level" label
    difficulty_label = tk.Label(settings_window, text="Difficulty Level", font=("Arial", 20))
    difficulty_label.pack(pady=20)
    
    # Difficulty slider with a range from 1 to 5
    difficulty_var = tk.IntVar(value=1)
    difficulty_slider = tk.Scale(settings_window, variable=difficulty_var, from_=1, to=5, orient="horizontal")
    difficulty_slider.pack()

    
    
    
    
    
 # Close the settings window and return to the game window
    close_button = tk.Button(settings_window, text="Close", font=("Arial", 16), command=settings_window.destroy)
    close_button.pack(pady=20)
    
    
    
    
    

    
    

 
## here?##

    
    




# Create the main login window
window = tk.Tk()
window.title("Login Window")
window.geometry('800x600')
window.configure(bg='#333333')

# Load the background image for the login page
bg_image_path = "C:/TPG Game Zip Files/Game Design/background3.png"  # Replace with your own image path
bg_image = Image.open(bg_image_path)
bg_photo = ImageTk.PhotoImage(bg_image)

login_frame = tk.Label(window, image=bg_photo, bg='#333333')  # Set the background image for login_frame
login_frame.pack(fill=tk.BOTH, expand=tk.YES)

# Rest of the login page code
name_label = tk.Label(login_frame, text="Welcome to the game!", fg="#000000", font=("Brush Script MT", 30), bg='#333333')
name_label.pack(pady=40)

name_entry = tk.Entry(login_frame, font=("Arial", 16))
name_entry.pack(pady=20)

login_button = tk.Button(login_frame, text="Enter Game", bg="#000000", fg="#FFFFFF", font=("Arial", 16), command=enter_game)
login_button.pack(pady=30)

# Set the window size and position to be the same as the game window
window_width = 800
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")





# Start the Tkinter event loop for the main login window
window.mainloop()
