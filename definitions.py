# import customtkinter
# from tktooltip import ToolTip
# import os
# from PIL import Image
# import time
# import tkinter as tk

# class Definition(customtkinter.CTk):      
#     def __init__(self, parent):
#         super().__init__(parent)
#         image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "p_icons")
#         # ! ---------------------------------------------------------------------------------------------------
#         # ! Create -> Character Create Button
#         # ! ---------------------------------------------------------------------------------------------------
#         self.initial_create_frame = customtkinter.CTkFrame(self.parent, corner_radius=20, fg_color="transparent")
#         self.initial_create_frame.grid(row=0, column=1, sticky="nsew")
#         self.initial_create_frame.grid_columnconfigure(0, weight=0)
#         self.initial_create_frame.grid_rowconfigure(0, weight=0)
        
#         self.plus_icon = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "w_plus.png")), size=(25,25))
        
#         self.create_character_button = customtkinter.CTkButton(self.initial_create_frame, 
#                                                                corner_radius=10, width=100, height=40, 
#                                                                text="Create Character", font=customtkinter.CTkFont(size=18), 
#                                                                image=self.plus_icon, command=self.show_character_creation)
#         self.create_character_button.grid(row=0, column=0, sticky="nsew")
#         # ! ---------------------------------------------------------------------------------------------------
#         # ! Character Create Button -> Creation
#         # ! ---------------------------------------------------------------------------------------------------
#         # ! Frame to display the 'Create' menu screen
#         # ! ====================================================
#         self.creation_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent") # grid() initializer is included in show_character_creation()
#         self.creation_frame.grid_columnconfigure(0, weight=1)
#         self.creation_frame.grid_columnconfigure(1, weight=0)
#         self.creation_frame.grid_columnconfigure(2, weight=0)
#         self.creation_frame.grid_rowconfigure(0, weight=0)
#         self.creation_frame.grid_rowconfigure(1, weight=0)
#         self.creation_frame.grid_rowconfigure(2, weight=0)
#         self.creation_frame.grid_rowconfigure(3, weight=1)
#         self.creation_frame.grid_rowconfigure(4, weight=1)
#         # ! ====================================================
#         # ! Segmented button to change between the different pieces of the character creation process
#         # ! ====================================================
#         self.character_aspects_var = customtkinter.StringVar(value="Definitions") # Variable to set the default segmented button selection
#         self.character_aspects = customtkinter.CTkSegmentedButton(self.creation_frame, 
#                                                                     height=40, corner_radius=10, 
#                                                                     values=["Definitions", "Long Description", "Short Description", "Greeting"], 
#                                                                     font=customtkinter.CTkFont(size=16, family="<SF pro display>"), 
#                                                                     command=self.seg_butt_test, variable=self.character_aspects_var)
#         self.character_aspects.grid(row=0, column=0, columnspan=2, padx=20, pady=(20,5), stick="nwes")
#         # ! ==================================================== 
#         # ! Frame to display character counting information
#         # ! ====================================================
#         self.count_frame = customtkinter.CTkFrame(self.creation_frame, fg_color="transparent")
#         self.count_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=(5,7), sticky="nsew")
#         self.count_frame.grid_columnconfigure(0, weight=0)
#         self.count_frame.grid_columnconfigure(1, weight=1)

#         # * Number counter to keep track of the number of typed characters
#         self.char_def_counter = customtkinter.CTkLabel(self.count_frame, height=1, text="Character Count: 0 / 3200", anchor="w")
#         self.char_def_counter.grid(row=2, column=0, padx=5, pady=0, sticky="nsew")

#         # * Progressbar to visually show how many characters out of the total limit have been used
#         self.char_count_progress = customtkinter.CTkProgressBar(self.count_frame, 
#                                                                 corner_radius=10, width=1000, height=15, 
#                                                                 fg_color="white", progress_color="#91eb38")
#         self.char_count_progress.set(0) # Range from 0 to 1 for bar fill
#         self.char_count_progress.grid(row=2, column=1, padx=5, pady=0, sticky="nw")

#         # ? Colors for the progress bar as it becomes full
#         self.bar_colors = ["#91eb38", "#adeb38", "#caeb38", "#e6eb38", "#ebd338", "#ebd338", "#e8b132", "#e68e2c", "#e36927", "#e04421"]
#         # ! ====================================================
#         # ! Frame for definition management buttons above scrollable frame and character counter
#         # ! ====================================================
#         self.definition_frame_buttons = customtkinter.CTkFrame(self.creation_frame, fg_color="transparent")
#         self.definition_frame_buttons.grid(row=1, column=0, columnspan=2, padx=20, pady=10, stick="nw")
#         self.definition_frame_buttons.grid_columnconfigure(0, weight=0)

#         # * Button to create a new definition
#         self.add_button = customtkinter.CTkButton(self.definition_frame_buttons, 
#                                                     width=140, height=40, corner_radius=10, 
#                                                     font=customtkinter.CTkFont(size=16), text="Definition", 
#                                                     image=self.plus_icon, command=self.add_definition) 
#         self.add_button.grid(row=0, column=0, pady=5, sticky="e")

#         # * Button to select definitions
#         self.select_button = customtkinter.CTkButton(self.definition_frame_buttons, 
#                                                         width=120, height=40, corner_radius=10, 
#                                                         font=customtkinter.CTkFont(size=16), text="Select", command=self.select_definitions)
#         self.select_button.grid(row=0, column=1, padx=10, pady=5, sticky="w")

#         # * Button to delete definitions
#         self.delete_def_butt = customtkinter.CTkButton(self.definition_frame_buttons, 
#                                                         width=120, height=40, corner_radius=10, 
#                                                         font=customtkinter.CTkFont(size=16), fg_color="#F14444", hover_color="#B22929", 
#                                                         text="Delete", command=self.delete_definition_selection)
#         # ! ====================================================
#         # ! Scrollable frame for definitions
#         # ! ====================================================
#         self.my_frame = customtkinter.CTkScrollableFrame(self.creation_frame, width=1920, height=1080, corner_radius=10)
#         self.my_frame.grid(row=3, column=0, columnspan=2, rowspan=4, padx=20, pady=(5,20), sticky="se")
#         self.my_frame.grid_columnconfigure(0, weight=1)
#         # ! ====================================================

#         # * Textbox to type definition in        
#         self.textbox = customtkinter.CTkTextbox(self.creation_frame, wrap="word", corner_radius=10, font=customtkinter.CTkFont(size=14), width=300)
#         self.textbox.grid(row=0, rowspan=4, column=2, padx=(10,20), pady=(20,10), sticky="ne")
#         self.textbox.insert("0.0", "Type definition here...")
#         self.textbox.configure(state="disabled")
#         self.textbox.bind("<FocusIn>", self.textbox_focus_disable)

#         # TODO: Will use on long description tab instead of definition tab
#         # # * Tabview to show grammar stuff
#         # self.tabview_def = customtkinter.CTkTabview(self.creation_frame, width=300, height=230, corner_radius=10)
#         # self.tabview_def.grid(row=3, column=2, padx=20, pady=(10,20), sticky="nw")

#         # self.tabview_def.add("Definition")
#         # self.tabview_def.add("Synonyms")
#         # self.tabview_def.add("Antonyms")

#         # ! EXTREMELY IMPORTANT: This allows radio buttons to only have one selected at a time
#         # ! ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#         self.variable = tk.IntVar()      
#         # ! ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#         self.def_type_frame = customtkinter.CTkFrame(self.creation_frame, corner_radius=10)
#         self.def_type_frame.grid(row=4, column=2, padx=(10,20), pady=10, sticky="news")
#         self.def_type_frame.grid_rowconfigure(0, weight=1)
#         self.def_type_frame.grid_rowconfigure(1, weight=1)
#         self.def_type_frame.grid_rowconfigure(2, weight=1)
#         self.def_type_frame.grid_rowconfigure(3, weight=1)
#         self.def_type_frame.grid_columnconfigure(0, weight=1)

#         self.def_type_label = customtkinter.CTkLabel(self.def_type_frame, text="Definition Type", 
#                                                         fg_color="#F9F9FA", corner_radius=10, 
#                                                         font=customtkinter.CTkFont(size=16), anchor="center")
#         self.def_type_label.grid(row=0, column=0, padx=10, pady=10, sticky="news")        

#         self.Hardcoded_rad = customtkinter.CTkRadioButton(master=self.def_type_frame, 
#                                                             radiobutton_width=25, radiobutton_height=25, width=1, height=1, 
#                                                             font=customtkinter.CTkFont(size=15), text="Hardcoded ??? []", variable=self.variable, value=0)
#         self.Hardcoded_rad.grid(row=1, column=0, padx=10, pady=10, sticky="news")       
            
#         self.Context_rad = customtkinter.CTkRadioButton(master=self.def_type_frame, 
#                                                         radiobutton_width=25, radiobutton_height=25, width=1, height=1, 
#                                                         font=customtkinter.CTkFont(size=15), text="Context ??? (())", variable=self.variable, value=1)
#         self.Context_rad.grid(row=2, column=0, padx=10, pady=10, sticky="news")

#         self.Variable_rad = customtkinter.CTkRadioButton(master=self.def_type_frame, 
#                                                             radiobutton_width=25, radiobutton_height=25, width=1, height=1, 
#                                                             font=customtkinter.CTkFont(size=15), text="Variable ??? {}", variable=self.variable, value=2)
#         self.Variable_rad.grid(row=3, column=0, padx=10, pady=10, sticky="news")

#         # ! Save, Edit buttons for textbox definition functionality
#         # ! ====================================================
#         # TODO: Add edit and cancel buttons so that textbox can be disabled and definitions won't accidentally be modified
#         self.textbox_buttons = customtkinter.CTkFrame(self.creation_frame, corner_radius=10)
#         self.textbox_buttons.grid(row=5, column=2, padx=(10,20), pady=(10,20), sticky="se")

#         self.def_save_butt = customtkinter.CTkButton(self.textbox_buttons, 
#                                                         corner_radius=10, width=286, height=40, 
#                                                         text="Save", font=customtkinter.CTkFont(size=16), 
#                                                         state="disabled", command=self.save_text_to)
#         self.def_save_butt.grid(row=0, column=0, padx=(7,7), pady=7, sticky="news")
#         # * <<<<<<<< Original edit button, use to make new one >>>>>>>>>
#         # self.def_edit_butt = customtkinter.CTkButton(self.textbox_buttons, corner_radius=10, width=92, height=40, text="Edit")
#         # self.def_edit_butt.grid(row=0, column=1, padx=5, pady=7)
#         # ! ====================================================        
#         # ! Variables for program and button functionality
#         # ! ===================================
#         self.current_definition = ""
#         self.definition_name = [] # List of readable button names for comparison purposes
#         self.my_definitions = [] # List of the checkboxes that are used for def selection
#         self.frame_definitions = [] # List of frames that are used for the def buttons and the checkbox
#         self.button_definitions = [] # List of names for buttons that display the definition
#         # ! ===================================
#         self.butt_num = 0 # Keeps track of how many buttons there are for definitions    
#         self.select_state = False # Tracks select button state to see if it has been pressed
#         # ! ===================================
#         # ? Allows deletion of definitions that are selected
#         # ? ================================================
#         def delete_definition_selection(self):
#             self.removed_count = 0
#             y = 0
#             # Iterates through all button names for defs
#             for x in self.definition_name:
#                 # Makes sure that only selected definitions are removed  
#                 if self.my_definitions[y].get() == 1:
#                     self.frame_definitions[y].grid_remove()
#                     self.removed_count += 1 # Keeps track of how many definitions were removed
#                 y+=1 # List position tracker   
#             self.butt_num -= self.removed_count # Makes sure current count of the def buttons is correct
#     # ? ================================================
#     # ? Allows selection of multiple definitions by showing checkboxes next to each definition
#     # ? Switches to cancel button that also makes all checkboxes disappear and delete button to be removed
#     # ? ======================================================================================
#     def select_definitions(self):
#         # self.count = len(self.my_definitions)
#         # * Checks button state to see if it has been pressed
#         if self.select_state == True:
#             self.delete_def_butt.grid_forget()
#             self.select_button.configure(text="Select")
#             self.select_state = False
#             for x in range(self.butt_num):
#                 # print(x)
#                 # print(self.my_definitions[x])
#                 self.my_definitions[x].grid_forget()
#                 self.button_definitions[x].grid_configure(padx=5)
#         else:   
#             self.select_state = True
#             self.delete_def_butt.grid(row=0, column=2, pady=5, sticky="e")
#             self.select_button.configure(text="Cancel")
#             for x in range(self.butt_num):
#                 self.my_definitions[x].grid(row=x, column=0, padx=(5,0), pady=5, sticky="nwes")    
#                 self.button_definitions[x].grid_configure(padx=(0,5))
#     # ? ======================================================================================                      
#     # ? Adding definitions
#     # ? ===================================        
#     def add_definition(self):          
#         if self.select_state == True:
#             self.select_button.configure(text="Select")
#             self.delete_def_butt.grid_forget()
#             for x in range(self.butt_num):
#                 self.my_definitions[x].grid_forget()
#                 self.button_definitions[x].grid_configure(padx=5)
        
#         def_num = str(self.butt_num)
#         def_name = "Definition"+def_num
#         frame_name = "Frame"+def_num
#         def_button_name = "Button"+def_num
        
#         self.my_definitions.append(def_name)
#         self.frame_definitions.append(frame_name)
#         self.button_definitions.append(def_button_name)
#         # print(self.button_definitions)
#         self.frame_definitions[self.butt_num] = customtkinter.CTkFrame(self.my_frame, corner_radius=10, fg_color="gray70")
#         self.frame_definitions[self.butt_num].grid(row=self.butt_num, column=0, padx=5, pady=5, sticky="news")
#         self.frame_definitions[self.butt_num].columnconfigure(1, weight=1)
#         self.frame_definitions[self.butt_num].columnconfigure(0, weight=0)
        
#         # TODO: checkbox command not being used, so it has been removed since only button state is important
#         # , command=lambda widget=self.my_definitions[count]: self.check_b(widget) 
#         self.my_definitions[self.butt_num] = customtkinter.CTkCheckBox(master=self.frame_definitions[self.butt_num], width=1, height=1, border_width=4, text="")
        
#         self.button_definitions[self.butt_num] = customtkinter.CTkButton(master=self.frame_definitions[self.butt_num], height=35, corner_radius=10, 
#                                                                             font=customtkinter.CTkFont(size=15), fg_color="#F9F9FA", text_color="gray10", text=str(self.butt_num), anchor="w", 
#                                                                             command= lambda widget=self.butt_num: self.textbox_init(widget))
#         self.button_definitions[self.butt_num].grid(row=self.butt_num, column=1, padx=5, pady=5, sticky="news")
        
#         # ! Allows program to keep track of the number of definitions present and also the proper name of the definitions
#         # ! ===================================================
#         self.definition_name.append(self.my_definitions[self.butt_num])
#         self.butt_num += 1
#         # ! ===================================================
#     # ? ===================================

#     # TODO: Implement other segmented button menus for other character aspects
#     def seg_butt_test(self, value):
#         print(value)
#     # TODO: ====================================    

#     # TODO: Check for radio button selection to auto format text input to the desired type of definition
#     # ? Takes textbox input and saves it to button text so that definition can be stored
#     # ? =================================================
#     def save_text_to(self):
#         b_text = str(self.textbox.get("0.0", "end")) # Gets text from textbox
#         formatted = b_text.rstrip('\r\n') # Removes return inputs and newlines
#         self.button_definitions[self.current_definition].configure(text=formatted,anchor="w") # Saves text to button
#         print(self.button_definitions[self.current_definition])
#     # ? =================================================
#     # ? Enables the character definition textbox
#     # ? ============================    
#     def textbox_focus_disable(self, val): # No idea what the issue is with enabling textbox, so this dummy function stays for now
#         why = None # Press F to pay respects
#     # ? ============================            
#     def textbox_init(self, curr_butt):
#         self.textbox.configure(state="normal") # Makes textbox usable
#         self.textbox.delete("0.0", "end") # Clears placeholder/previous text
#         self.textbox.insert("0.0", self.button_definitions[curr_butt].cget('text'))
#         self.current_definition = curr_butt # Keeps track of current definition
#         self.def_save_butt.configure(state="normal") # Enables save button to save definition
        
#         if self.select_state == True: # Select button logic to keep it from being active or from toggling when it shouldn't
#             self.select_definitions()
#     # ? ============================    
#     # ? Progress bar tester/counter
#     # ? ============================    
#     def progress_color_percentage(self):
#         for i in range(3200):
#             temp = i/3200 # Sets progress bar percentage
            
#             # Sets progress bar color based on percentage
#             if temp == .1:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[0])
#             elif temp == .2:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[1])
#             elif temp == .3:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[2])
#             elif temp == .4:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[3])
#             elif temp == .5:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[4])
#             elif temp == .5:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[5])
#             elif temp == .6:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[6])
#             elif temp == .7:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[7])
#             elif temp == .8:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[8])
#             elif temp == .9:
#                 self.char_count_progress.configure(progress_color=self.bar_colors[9])
                
#             self.char_count_progress.set(temp) # Updates progress bar
#             self.char_def_counter.configure(text=("Character Count: " + str(i+1) + " / 3200")) # Updates label with total character number
#             self.update()
#     # ? ============================        