from tktooltip import ToolTip
import os
from PIL import Image
import time
from tkinter import ttk
import tkinter
import sv_ttk         
# import definitions    
import sv_ttk_create

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=15)
        # Configure window
        # self.title("Character Creator")
        # self.geometry(f"{1200}x{650}")
        # Min window size
        # self.minsize(800, 500)
        sv_ttk.set_theme("dark")
        # self =ttkinter.Tk()
        
        # Set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # ! create navigation frame 
        # ! ---------------------------------------------------------------------------------------------------
        self.navigation_frame = ttk.Frame(self)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        
        # About button
        # ==================
        self.about_frame = ttk.Frame(self)
        self.about_button = ttk.Button(self.navigation_frame, text="About", command=self.about_button_event)
        self.about_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        # self.Tool_test = ttk.Tooltip(self.about_button, msg="Learn about character creation here!")
        # ToolTip(self.about_button, msg="Learn about character creation here!")   
             
        # Create button
        # ==================
        self.home_frame = ttk.Frame(self)
        self.home_button =ttk.Button(self.navigation_frame, text="Create", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        # ToolTip(self.home_button, msg="Everything you need to create your character!")
                
        # Characters button
        # ==================
        self.characters_frame = ttk.Frame(self)
        self.characters_button =ttk.Button(self.navigation_frame, text="Characters", command=self.char_button_event)
        self.characters_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        # ToolTip(self.characters_button, msg="View your created characters here!")
        
        # Save button
        # ==================
        self.save_button =ttk.Button(self.navigation_frame, text="Save")
        self.save_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
        # Navigation frame and UI color scheme selection
        # ==================       
        # self.appearance_mode_label = ttk.Label(self.navigation_frame, 
        #                                                     text="Color Mode:", 
        #                                                     anchor="w")
        # self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=(10, 0))
        # self.appearance_mode_menu = ttk.OptionMenu(self.navigation_frame, 
        #                                                         values=["Light", "Dark", "System"],
        #                                                         command=self.change_appearance_mode_event, 
        #                                                         width=90, state="disabled")
        # self.appearance_mode_menu.grid(row=6, column=0, padx=5, pady=5, sticky="s")
        # ! ---------------------------------------------------------------------------------------------------
        # ! Create -> Character Create Button
        # ! ---------------------------------------------------------------------------------------------------
        self.initial_create_frame = sv_ttk_create.Create_Frame(self.home_frame)
        # ! ---------------------------------------------------------------------------------------------------
    # ? ============================    
    # ? Allows user to change between the different menus available on the sidebar
    # ? ====================================================
    def select_frame_by_name(self, name):
        if name == "about":
            self.about_frame.grid(row=0, column=1, padx=20, pady=20, sticky="se")
        else:
            self.about_frame.grid_forget()
        if name == "create":
            self.home_frame.grid(row=0, column=1)
        else:
            self.home_frame.grid_forget()
        if name == "char":
            self.characters_frame.grid(row=0, column=1, padx=20, pady=20)
        else:
            self.characters_frame.grid_forget()
    # ? ====================================================
    # ? Passes user selection of the menu to change the visible frame
    # ? ============================================================
    def about_button_event(self):
        self.select_frame_by_name("about")

    def home_button_event(self):
        self.select_frame_by_name("create")
        
    def char_button_event(self):
        self.select_frame_by_name("char")

    def show_character_creation(self):
        self.initial_create_frame.grid_forget()
        self.creation_frame.grid(row=0, column=1, padx=20, pady=20)
    # ! Functionality of optionmenu to change UI color mode
    # ! ===================================================
    def change_appearance_mode_event(self, new_appearance_mode):
        ttk.set_appearance_mode(new_appearance_mode)  
    # ! =================================================== 
# ! Program startup
# ! --------------------------------------
# ttk.set_appearance_mode("Light")      
# ttk.set_default_color_theme("custom-theme.json")
# ttk.set_default_color_theme("purp-theme.json")

if __name__ == "__main__":
    
    app = tkinter.Tk()
    
    sv_ttk.set_theme("dark")
    
    App(app).pack(expand=True, fill="both")
    app.mainloop()
# ! --------------------------------------