import customtkinter
from tktooltip import ToolTip
import os
from PIL import Image
import time
import tkinter as tk             
# import tkinter.ttk as ttk
# import queue
# import multiprocessing as mp
from multiprocessing import Pool
import re

class App(customtkinter.CTk):

    
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Character Creator")
        self.geometry(f"{1100}x{580}")
        # Min window size
        self.minsize(800, 500)
        # Set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Path for icon images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "p_icons")
        
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
                                                      width=100, anchor="w", command=self.dumb)
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
                                                                width=90)
        self.appearance_mode_menu.grid(row=6, column=0, padx=5, pady=5, sticky="s")
        # ! ---------------------------------------------------------------------------------------------------
        
        # ! Create -> Character Create Button
        # ! ---------------------------------------------------------------------------------------------------

        self.initial_create_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=20, fg_color="transparent")
        self.initial_create_frame.grid(row=0, column=1, sticky="nsew")
        self.initial_create_frame.grid_columnconfigure(0, weight=0)
        self.initial_create_frame.grid_rowconfigure(0, weight=0)
        
        self.plus_icon = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "w_plus.png")), size=(25,25))
        
        self.create_character_button = customtkinter.CTkButton(self.initial_create_frame, corner_radius=10, width=100, height=40, text="Create Character", font=customtkinter.CTkFont(size=18), image=self.plus_icon, command=self.show_character_creation)
        self.create_character_button.grid(row=0, column=0, sticky="nsew")
        # ! ---------------------------------------------------------------------------------------------------
        
        #! Character Create Button -> Creation
        # ! ---------------------------------------------------------------------------------------------------

        # ! Frame to display the 'Create' menu screen
        # ! ====================================================
        self.creation_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent") # grid() initializer is included in show_character_creation()
        self.creation_frame.grid_columnconfigure(0, weight=1)
        self.creation_frame.grid_columnconfigure(1, weight=0)
        self.creation_frame.grid_columnconfigure(2, weight=0)
        self.creation_frame.grid_rowconfigure(0, weight=0)
        self.creation_frame.grid_rowconfigure(1, weight=0)
        self.creation_frame.grid_rowconfigure(2, weight=0)
        self.creation_frame.grid_rowconfigure(3, weight=1)
        # ! ==================================================== 
        
        # TODO: DEVELOP AND DEPLOY MULTIPROCESSING FOR GUI
        self.char_def_counter = customtkinter.CTkLabel(self.creation_frame, height=1, text="Character Count: 0 / 3200", anchor="w")# ! THIS WILL REQUIRE MULTIPROCESSING
        self.char_def_counter.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")
        
        # ! Frame for definition management buttons above scrollable frame and character counter
        self.definition_frame_buttons = customtkinter.CTkFrame(self.creation_frame, fg_color="transparent")
        self.definition_frame_buttons.grid(row=1, column=0, columnspan=2, padx=20, pady=10, stick="nw")
        self.definition_frame_buttons.grid_columnconfigure(0, weight=0)
        
        # * Button to create a new definition
        self.add_button = customtkinter.CTkButton(self.definition_frame_buttons, width=120, height=40, corner_radius=10, font=customtkinter.CTkFont(size=16), text="Definition", image=self.plus_icon, command=self.add_definition) 
        self.add_button.grid(row=0, column=0, pady=5, sticky="e")
        
        # * Button to select definitions
        self.select_button = customtkinter.CTkButton(self.definition_frame_buttons, width=120, height=40, corner_radius=10, font=customtkinter.CTkFont(size=16), text="Select", command=self.select_definitions)
        self.select_button.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # * Button to delete definitions
        self.delete_def_butt = customtkinter.CTkButton(self.definition_frame_buttons, width=120, height=40, corner_radius=10, font=customtkinter.CTkFont(size=16), text="Delete", command=self.delete_definition_selection)
        
        # * Segmented button to change between the different pieces of the character creation process
        self.character_aspects_var = customtkinter.StringVar(value="Definitions") # Variable to set the default segmented button selection
        self.character_aspects = customtkinter.CTkSegmentedButton(self.creation_frame, height=40, corner_radius=10, values=["Definitions", "Long Description", "Short Description", "Greeting"], font=customtkinter.CTkFont(size=15, family="<SF pro light>"), command=self.seg_butt_test, variable=self.character_aspects_var)
        self.character_aspects.grid(row=0, column=0, columnspan=2, padx=20, pady=(20,5), stick="nwes")
            
        # ! Scrollable frame for definitions
        self.my_frame = customtkinter.CTkScrollableFrame(self.creation_frame, width=1920, height=1080, corner_radius=10)
        self.my_frame.grid(row=3, column=0, columnspan=2, rowspan=4, padx=20, pady=(5,20), sticky="se")
        self.my_frame.grid_columnconfigure(0, weight=1)

        # * Textbox to type definition in        
        self.textbox = customtkinter.CTkTextbox(self.creation_frame, wrap="word", corner_radius=10, width=300)
        self.textbox.grid(row=0, rowspan=4, column=2, padx=(10,20), pady=(20,10), sticky="ne")
        self.textbox.insert("0.0", "Type definition here..." )
        self.textbox.configure(state="disabled")
        self.textbox.bind("<FocusIn>", self.focus_test)

        # TODO: Will use on long description tab instead of definition tab
        # # * Tabview to show grammar stuff
        # self.tabview_def = customtkinter.CTkTabview(self.creation_frame, width=300, height=230, corner_radius=10)
        # self.tabview_def.grid(row=3, column=2, padx=20, pady=(10,20), sticky="nw")
        
        # self.tabview_def.add("Definition")
        # self.tabview_def.add("Synonyms")
        # self.tabview_def.add("Antonyms")
        
        # ! Save, Edit, Delete buttons for definition functionality
        self.textbox_buttons = customtkinter.CTkFrame(self.creation_frame, corner_radius=10)
        self.textbox_buttons.grid(row=4, column=2, padx=(10,20), pady=(10,20), sticky="se")
        
        self.def_save_butt = customtkinter.CTkButton(self.textbox_buttons, corner_radius=10, width=92, height=40, text="Save", command=self.check_curr_def)
        self.def_save_butt.grid(row=0, column=0, padx=(7,2), pady=7, sticky="w")
        self.def_edit_butt = customtkinter.CTkButton(self.textbox_buttons, corner_radius=10, width=92, height=40, text="Edit")
        self.def_edit_butt.grid(row=0, column=1, padx=5, pady=7)
        # TODO: <<<<<<<<<<<<< Will most likely remove this delete button since selection button has been added to allow deletion of definitions >>>>>>>>>>>>
        self.def_delete_butt = customtkinter.CTkButton(self.textbox_buttons, corner_radius=10, width=92, height=40, text="Delete")
        self.def_delete_butt.grid(row=0, column=2, padx=(2,7), pady=7, sticky="e")
        
        # ! Currently selected definition so that save, edit, delete buttons function only on selected definition
        # ! ===================
        self.selected_definitions = []
        # ! ===================
        
        # ! EXTREMELY IMPORTANT: This allows radio buttons to only have one selected at a time
        # ! ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        self.variable = tk.IntVar()      
        # ! ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
          
        # ! Adding definitions
        # ! ===================================
        self.my_definitions = []
        self.frame_definitions = []
        self.button_definitions = []  
        # ! ===================================
    
    # TODO: Figure out how to remove definitions from stored lists in an elegant manner
    def delete_definition_selection(self):
        print()
        # count = len(self.selected_definitions)
        y = 0
        # global temp_pos
        # temp_pos = None

        # for x in self.selected_definitions:
        #     # global temp_pos
        #     # temp_pos = None
        #     print(x)
        #     self.temp_pos = []
        #     for g in self.my_definitions:
        #         print(g)
        #         if g == x:
        #             self.temp_pos[0] = g
        #             print(g)
        #             break
        #     # temp = self.selected_definitions[y]
        #     # def_pos = [int(i) for i in temp.split() if i.isdigit()]
        #     print(self.temp_pos[0])
        #     self.frame_definitions[self.temp_pos[0]].grid_remove()
        #     self.my_definitions.pop(self.temp_pos[0])
        #     self.frame_definitions.pop(self.temp_pos[0])
        #     self.button_definitions.pop(self.temp_pos[0])
        #     y += 1
            
    # ? Allows selection of multiple definitions by showing checkboxes next to each definition
    # ? ======================================================================================
    def select_definitions(self):
        self.delete_def_butt.grid(row=0, column=2, pady=5, sticky="e")
        
        count = len(self.my_definitions)
        for x in range(count):
            self.my_definitions[x].grid(row=x, column=0, padx=(7,1), pady=7, sticky="nwes")    
            self.button_definitions[x].grid_configure(padx=(1,7))

    # ? ======================================================================================
          
    def check_curr_def(self):
        print(self.selected_def)
        
    # ? Removes placeholder text from textbox
    # ? =====================================        
    def focus_test(self):
        self.textbox.delete("0.0", "end")     
    # ? =====================================                
    # ? Adding definitions
    # ? ===================================        
    def add_definition(self):  
        count = len(self.my_definitions)
        
        if count != 0:
            self.delete_def_butt.grid_forget()
            for x in range(count):
                self.my_definitions[x].grid_forget()
                self.button_definitions[x].grid_configure(padx=7)
        
        # TODO: Change this so that the button name is not based on the length of the list of current buttons; this will prevent buttons from having the same name
        def_num = str(count)
        def_name = "Definition"+def_num
        frame_name = "Frame"+def_num
        def_button_name = "Button"+def_num
        
        self.my_definitions.append(def_name)
        self.frame_definitions.append(frame_name)
        self.button_definitions.append(def_button_name)
        
        self.frame_definitions[count] = customtkinter.CTkFrame(self.my_frame, corner_radius=10, fg_color="gray70")
        self.frame_definitions[count].grid(row=count, column=0, padx=5, pady=5, sticky="news")
        self.frame_definitions[count].columnconfigure(1, weight=1)
        self.frame_definitions[count].columnconfigure(0, weight=0)
        
        self.my_definitions[count] = customtkinter.CTkCheckBox(master=self.frame_definitions[count], width=1, height=1, text="", command=lambda widget=self.my_definitions[count]: self.check_b(widget))
        # self.my_definitions[count].grid(row=count, column=0, padx=(5,2.5), pady=5, sticky="news")
        # * <<<< Unused radio buttons, keeping for when I need them again so I know the format >>>>
        # self.my_definitions[count] = customtkinter.CTkRadioButton(master=self.frame_definitions[count], border_color="gray95", radiobutton_width=35, radiobutton_height=35, border_width_unchecked=10, border_width_checked=10, width=1, height=1, text="", variable=self.variable, value=count, command=lambda widget=self.my_definitions[count]: self.check_b(widget))
        # self.my_definitions[count].grid(row=count, column=0, padx=(7,1), pady=7, sticky="news")
        
        self.button_definitions[count] = customtkinter.CTkButton(master=self.frame_definitions[count], height=35, corner_radius=10, text="This is a story all about how my life got flip turned upside down and I had a little", fg_color="gray95", command=lambda widget=self.button_definitions[count]: self.check_b(widget))
        self.button_definitions[count].grid(row=count, column=1, padx=7, pady=7, sticky="news")
        

    # * Little tester for buttons   
    def check_b(self, val):
        
        
        for x in len(self.my_definitions):
            if self.button_definitions[x] == val:
                temp = self.button_definitions[x].get()
                if temp == 1:
                    print(val, " button selected!")
                elif temp == 0:
                    print(val, " button deselected!")
        # print(self.selected_def)
        self.selected_definitions.append(val)
        
        # self.selected_def=val
        # print(val)
    # ? ===================================

    def seg_butt_test(self, value):
        print(value)
        
    # ? Enables the character definition textbox
    # ? ============================    
    def textbox_init(self):
        self.textbox.configure(state="normal")
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
    # ? ============================================================

    # ? Button tester
    def dumb(self):
        print("Dumb")

    # ! Functionality of optionmenu to change UI color mode
    # ! ===================================================
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)  
    # ! ===================================================        



# ! Program startup
# ! --------------------------------------
customtkinter.set_appearance_mode("Light")      
customtkinter.set_default_color_theme("dark-blue.json")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
# ! --------------------------------------