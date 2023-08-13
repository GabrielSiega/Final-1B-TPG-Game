import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as tkFont

game_window = None


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

Swordsman = chosen_character()['1']
Rizzard = chosen_character()['2']
Knight = chosen_character()['3']
Thief = chosen_character()['4']





def Button_6_command():
    print("User pressed Restart")
    
def Button_7_command():
    print("User pressed Exit")
    print()
    print("Game Closed")
    root.destroy()

def Button_7_command():
    print("User pressed Exit")
    
    
def create_text(root, text, x, y):
    label = tk.Label(root, font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center", text=text)
    label.place(x=x, y=y, width=85, height=25)





def open_settings_window():
    global game_window
    if game_window:
        game_window.destroy()

    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    # Create an instance of the SettingsWindow class
    settings = SettingsWindow(settings_window)

class SettingsWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")  # Set the size of the settings window

        self.audio_on = tk.BooleanVar(value=True)
        self.language = tk.StringVar(value="English")
        self.difficulty_level = tk.DoubleVar(value=1.0)

        self.create_audio_controls()
        self.create_language_dropdown()
        self.create_difficulty_slider()
        self.load_and_display_image()
        self.create_buttons()
        
        

    def create_audio_controls(self):
        audio_label = tk.Label(self.root, text="Audio:", font=("Arial", 12))
        audio_label.place(x=20, y=20)

        audio_on_button = tk.Radiobutton(self.root, text="On", variable=self.audio_on, value=True)
        audio_on_button.place(x=80, y=20)

        audio_off_button = tk.Radiobutton(self.root, text="Off", variable=self.audio_on, value=False)
        audio_off_button.place(x=120, y=20)

    def create_language_dropdown(self):
        language_label = tk.Label(self.root, text="Language:", font=("Arial", 12))
        language_label.place(x=20, y=60)

        languages = ["English", "Spanish", "French", "German"]
        language_dropdown = ttk.Combobox(self.root, textvariable=self.language, values=languages)
        language_dropdown.place(x=120, y=60)

    def create_difficulty_slider(self):
        difficulty_label = tk.Label(self.root, text="Difficulty Level:", font=("Arial", 12))
        difficulty_label.place(x=20, y=100)

        difficulty_slider = tk.Scale(self.root, variable=self.difficulty_level, from_=1, to=10, orient="horizontal")
        difficulty_slider.place(x=150, y=100)

        difficulty_value_label = tk.Label(self.root, textvariable=self.difficulty_level)
        difficulty_value_label.place(x=300, y=100)
        
    def load_and_display_image(self):
        image_path = "C:/TPG Game Zip Files/Game Design/background3.png"  # Replace with the path to your image
        image = Image.open(image_path)
        image = image.resize((200, 200))  # Resize the image if needed
        image_tk = ImageTk.PhotoImage(image)

        image_label = tk.Label(self.root, image=image_tk)
        image_label.place(x=400, y=20)  # Adjust the x and y values as needed
        
    def create_buttons(self):
        button_6 = tk.Button(self.root, text="Restart", font=("Arial", 12), command=Button_6_command)
        button_6.place(x=20, y=160, width=100, height=30)

        button_7 = tk.Button(self.root, text="Quit", font=("Arial", 12), command=Button_7_command)
        button_7.place(x=130, y=160, width=100, height=30)
        
    if __name__ == "__main__":
        root = tk.Tk()

    width = 800
    height = 600
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = f'{width}x{height}+{(screenwidth - width) // 2}+{(screenheight - height) // 2}'
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    # Close the main window
    root.destroy()






def create_game_window():
    global blended_photo, game_window, selected_character_label  # Use the global blended_photo, game_window, and selected_character_label variables

    # Destroy the current game window, if exists
    if game_window:
        game_window.destroy()


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
    

def Button_6_command():
    print("User pressed Restart")
    
def Button_7_command():
    print("User pressed Exit")
    print()
    print("Game Closed")
    root.destroy()

def create_button(root, text, x, y, command):
    button = tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Times', size=10), fg="#000000", justify="center", text=text, command=command)
    button.place(x=x, y=y, width=120, height=34)

def create_text(root, text, x, y):
    label = tk.Label(root, font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center", text=text)
    label.place(x=x, y=y, width=85, height=25)

def create_message(root, text, x, y):
    message = tk.Message(root, font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center", text=text)
    message.place(x=x, y=y, width=80, height=25)

if __name__ == "__main__":
    root = tk.Tk()

    width = 800
    height = 600
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = f'{width}x{height}+{(screenwidth - width) // 2}+{(screenheight - height) // 2}'
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    # Load a square image placeholder
    character_image_1_path = "C:/TPG Game Zip Files/Game Design/LightBandit_Idle_0.png" 
    character_image_2_path = "C:/TPG Game Zip Files/Game Design/HeroKnight_Idle_0.png" 
    # Replace with the path to your square image
    image1 = Image.open(character_image_1_path)
    image2 = Image.open(character_image_2_path)
    
    image1 = image1.resize((100, 100), Image.LANCZOS)  # Resize the image to fit
    image1 = ImageTk.PhotoImage(image1)
    image2 = image2.resize((100, 100), Image.LANCZOS)
    image2 = ImageTk.PhotoImage(image2)


    # Create a label to display the image
    image_label = tk.Label(root, image=image1)
    image_label.place(x=300, y=95)  # Adjust the coordinates as needed
    
    # Create a label to display the image
    image_label = tk.Label(root, image=image2)
    image_label.place(x=520, y=95)  # Adjust the coordinates as needed

    create_button(root, "Basic Attack", 100, 350, Button_1_command)
    create_button(root, "Defend", 100, 400, Button_2_command)
    create_button(root, "HP potion", 100, 450, Button_3_command)
    create_button(root, "Special Skill", 100, 500, Button_4_command)
    create_button(root, "Settings", 400, 400, open_settings_window)
    create_button(root,"Restart", 400,440,Button_6_command)
    create_button(root,"Exit", 400,480,Button_7_command)

    create_text(root, f"- {Swordsman.dp} Damage", 230, 360)  # change to user's choice from character choice window
    create_text(root, f"Defends: +{Swordsman.dp} hp", 230, 410)
    create_text(root, "Use Potion", 230, 460)
    create_text(root, "Special Skill", 230, 510)

    create_message(root, "Enemy Character:", 120, 200)
    create_message(root, "Your Character:", 120, 270)  # Between Row 1 &2
    create_message(root, "VS",420,140)

#hp ap dp sp mp

#Enemy Character Stats
    create_message(root, "Hp: ", 70, 240)  # Row 1 
    create_message(root, "Ap: ", 180, 240)  # Row 1
    create_message(root, "Dp: ", 290, 240)  # Row 1
    create_message(root, "Sp: ", 410, 240)  # Row 1
    create_message(root, "Mp: ", 520, 240)  # Row 1

#Character Stats
    create_message(root, "Hp: ", 70, 300)
    create_message(root, "Ap: ", 180, 300)
    create_message(root, "Dp: ", 290, 300)  # Row 2
    create_message(root, "Sp: ", 410, 300)  # Row 2
    create_message(root, "Mp: ", 520, 300)  # Row 2




    root.mainloop()
