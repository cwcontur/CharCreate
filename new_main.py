from tktooltip import ToolTip
import os
from PIL import Image
import time
from tkinter import ttk
import tkinter
import sv_ttk         
# import definitions    
import new_create

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=7)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        # ! create navigation frame 
        # ! ---------------------------------------------------------------------------------------------------
        self.navigation_frame = ttk.Frame(self, style="Card.TFrame")
        self.navigation_frame.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        self.navigation_frame.rowconfigure(5, weight=1)      
          
        # About button
        # ==================     
        self.about_frame = ttk.Frame(self, style="Card.TFrame")   
        self.about_button = ttk.Button(self.navigation_frame, text="About", command=self.about_button_event)
        self.about_button.grid(row=0, column=0, ipadx=30, ipady=5, padx=10, pady=10, sticky="ew")
        # * ipadx, ipady allows for height and width adjustment that's based on inner pixels of the button
        
        # Create button
        # ==================      
        # self.home_frame = ttk.Frame(self, style="Card.TFrame")  
        self.home_button = ttk.Button(self.navigation_frame, text="Create", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, ipadx=30, ipady=5, padx=10, pady=(0,10), sticky="ew")    
            
        # Characters button
        # ==================       
        self.characters_frame = ttk.Frame(self, style="Card.TFrame") 
        self.characters_button = ttk.Button(self.navigation_frame, text="Characters", command=self.char_button_event)
        self.characters_button.grid(row=2, column=0, ipadx=30, ipady=5, padx=10, pady=(0,10), sticky="ew")
        
        # Save button
        # ==================           
        self.save_button = ttk.Button(self.navigation_frame, text="Save")
        self.save_button.grid(row=3, column=0, ipadx=30, ipady=5, padx=10, pady=(0,10), sticky="ew")
    
        # Separator line
        # ==================                  
        self.separator = ttk.Separator(self.navigation_frame)
        self.separator.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        
        # Toggle theme from light to dark
        # ==================           
        self.theme_toggle = ttk.Checkbutton(self.navigation_frame, text="Dark Theme", style="Switch.TCheckbutton", command=sv_ttk.toggle_theme)
        self.theme_toggle.grid(row=5, column=0, padx=10, pady=(0,10), sticky="s")
        
        # ! ---------------------------------------------------------------------------------------------------
        # ! Create -> Character Create Button
        # ! ---------------------------------------------------------------------------------------------------
        self.initial_create_frame = new_create.Create_Frame(self)
        # self.initial_create_frame.grid_forget()
        # ! ---------------------------------------------------------------------------------------------------
        
    # ? ============================    
    # ? Allows user to change between the different menus available on the sidebar
    # ? ====================================================
    def select_frame_by_name(self, name):
        if name == "about":
            self.about_frame.grid(row=0, column=1, padx=10, pady=10, sticky="se")
        else:
            self.about_frame.grid_forget()
        if name == "create":
            self.initial_create_frame.grid(row=0, padx=10, pady=10, column=1)
        else:
            # self.home_frame.grid_forget()
            print()
        if name == "char":
            self.characters_frame.grid(row=0, column=1, padx=10, pady=10)
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
        self.creation_frame.grid(row=0, column=1, padx=10, pady=10)    
        
        
        
        
# ! Program startup
# ! --------------------------------------
if __name__ == "__main__":
    
    app = tkinter.Tk()
    app.title("Character Creator")
    app.geometry(f"{1200}x{650}")
    app.minsize(800, 500)
    sv_ttk.set_theme("light")
    
    App(app).pack(expand=True, fill="both")
    app.mainloop()
# ! --------------------------------------