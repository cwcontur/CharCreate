import customtkinter
from tktooltip import ToolTip
import os
from PIL import Image
import time
import tkinter as tk         
# import definitions    
import create
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Configure window
        self.title("Character Creator")
        self.geometry(f"{1200}x{650}")
        # Min window size
        self.minsize(800, 500)
        # Set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # ! create navigation frame 
        # ! ---------------------------------------------------------------------------------------------------
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        
        # About button
        # ==================
        self.about_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, 
                                                   height=40, border_spacing=10, text="About",font=customtkinter.CTkFont(size=18),
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
                                                   width=100, anchor="w", command=self.about_button_event)
        self.about_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ToolTip(self.about_button, msg="Learn about character creation here!")   
             
        # Create button
        # ==================
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, 
                                                   height=40, border_spacing=10, text="Create",font=customtkinter.CTkFont(size=18),
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
                                                   width=100, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        ToolTip(self.home_button, msg="Everything you need to create your character!")
                
        # Characters button
        # ==================
        self.characters_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.characters_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, 
                                                      height=40, border_spacing=10, 
                                                      text="Characters",font=customtkinter.CTkFont(size=18),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
                                                      width=100, anchor="w", command=self.char_button_event)
        self.characters_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        ToolTip(self.characters_button, msg="View your created characters here!")
        
        # Save button
        # ==================
        self.save_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, 
                                                      height=40, border_spacing=10, 
                                                      text="Save",font=customtkinter.CTkFont(size=18),
                                                      fg_color="transparent", 
                                                      text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
                                                      width=100, anchor="w")
        self.save_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
        # Navigation frame and UI color scheme selection
        # ==================       
        self.appearance_mode_label = customtkinter.CTkLabel(self.navigation_frame, 
                                                            text="Color Mode:", 
                                                            anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=(10, 0))
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, 
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event, 
                                                                width=90, state="disabled")
        self.appearance_mode_menu.grid(row=6, column=0, padx=5, pady=5, sticky="s")
        # ! ---------------------------------------------------------------------------------------------------
        # ! Create -> Character Create Button
        # ! ---------------------------------------------------------------------------------------------------
        self.initial_create_frame = create.Create_Frame(self.home_frame)
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
        customtkinter.set_appearance_mode(new_appearance_mode)  
    # ! =================================================== 
# ! Program startup
# ! --------------------------------------
customtkinter.set_appearance_mode("Light")      
customtkinter.set_default_color_theme("custom-theme.json")
if __name__ == "__main__":
    app = App()
    app.mainloop()
# ! --------------------------------------