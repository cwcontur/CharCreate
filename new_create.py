from tktooltip import ToolTip
import os
from PIL import Image
import time
from tkinter import ttk
import tkinter
import sv_ttk         
# import definitions    
import new_create
from ttkwidgets.frames import Balloon
from tkinter import *
import PySimpleGUI as sg

class Create_Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style="Card.TFrame",padding=15)
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)
        # ! ---------------------------------------------------------------------------------------------------
        # ! Create -> Character Create Button
        # ! ---------------------------------------------------------------------------------------------------
        self.initial_create_frame = ttk.Frame(self, style="Card.TFrame")
        self.initial_create_frame.grid(row=0, column=0, sticky="nsew")
        # self.initial_create_frame.grid_columnconfigure(0, weight=0)
        # self.initial_create_frame.grid_rowconfigure(0, weight=0)
                
        self.create_character_button = ttk.Button(self.initial_create_frame, text="Create Character", command=self.show_character_creation)
        self.create_character_button.grid(row=0, column=0, sticky="nsew")          
        # ! ---------------------------------------------------------------------------------------------------
        # ! Character Create Button -> Creation
        # ! ---------------------------------------------------------------------------------------------------
        
        self.tabControl = ttk.Notebook(self, height=3000, width=7000)

        # ! Frame to display the 'Create' menu screen
        # ! ====================================================
        self.creation_frame = ttk.Frame(self.tabControl) # grid() initializer is included in show_character_creation()
        self.creation_frame.grid(row=0, column=0, padx=7, pady=7, sticky="news")
        # self.creation_frame.columnconfigure(0, weight=1)
        # self.creation_frame.columnconfigure((1,2), weight=0)
        # self.creation_frame.rowconfigure((0,1,2), weight=0)
        # self.creation_frame.rowconfigure((3,4), weight=1)
        self.creation_frame.columnconfigure(0, weight=1)
        self.creation_frame.columnconfigure((1,2), weight=0)
        self.creation_frame.rowconfigure(0, weight=0)

        self.creation_frame.rowconfigure(1, weight=0)
        self.creation_frame.rowconfigure(2, weight=0)
        self.creation_frame.rowconfigure(3, weight=1)
        # ! ====================================================
        # ! ====================================================
        self.def_buttons = ttk.Frame(self.creation_frame)
        self.def_buttons.grid(row=0, column=0, padx=0, pady=0, sticky="news")
        
        self.add_def = ttk.Button(self.def_buttons, text="Add Definition", style="Toggle.TButton", command=self.add_definition)
        self.add_def.grid(row=0, column=0, padx=15, pady=(15,0), sticky="news")
        
        self.select_def = ttk.Button(self.def_buttons, text="Select", style="Toggle.TButton", command=self.select_definition)
        self.select_def.grid(row=0, column=1, padx=(0,15), pady=(15,0), sticky="w")
        
        self.delete_def = ttk.Button(self.def_buttons, text="Delete", style="Accent.TButton", command=self.delete_definition)
        # self.delete_def.grid(row=0, column=2, padx=(0,15), pady=(15,0), sticky="w")
        
        self.char_def_counter = ttk.Label(self.def_buttons, text="Character Count: 0 / 3200", anchor="w")
        self.char_def_counter.grid(row=1, column=0, columnspan=2, padx=15, pady=(15,0), sticky="sw")
        # ! ====================================================
        # ! ==========================================
        self.scrollbar = ttk.Scrollbar(self.creation_frame)
        self.scrollbar.grid(row=1, rowspan=3, column=1, padx=(0,15), pady=15, sticky="nse")
        
        self.tree = ttk.Treeview(self.creation_frame, columns=1, selectmode="browse", show="headings", yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tree.yview)
        self.tree["columns"] = ("1")
        self.tree.column("1", anchor = "nw")
        self.tree.heading("1", command=self.dumbass, text="Definition")
        self.tree.grid(row=1, rowspan=3, column=0, padx=(15,5), pady=(5,15), sticky="nsew")
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        # * Tree item insertion
        # self.tree.insert("", 'end', text="L1", values=("Testiclesings"))
        # self.tree.insert("", 'end', text="L2", values=("Testiclfdafdasfdasesings"))
        # ! ==========================================
        # ! ==========================================
        self.right_hand_frame = ttk.Frame(self.creation_frame)
        self.right_hand_frame.grid(row=0, rowspan=4, column=2, sticky="news")
        # ! ==========================================
        # ! ==========================================
        self.text_frame = ttk.Frame(self.right_hand_frame, style="Card.TFrame")
        self.text_frame.grid(row=0, rowspan=2, column=0, padx=(0,15), pady=15, sticky="news")
        
        self.textbox = Text(self.text_frame, height=5, width=35, wrap="word", font=("Segoe UI",10),relief="flat")
        self.textbox.grid(row=0, column=0, padx=7, pady=7, sticky="ne")
        self.textbox.insert("0.0", "Type definition here...")
        self.textbox.configure(state="disabled")
        
        self.textbox.bind("<FocusIn>")
        # ! ==========================================
        # ! ==========================================
        self.grammar_frame = ttk.Frame(self.right_hand_frame, style="Card.TFrame")
        self.grammar_frame.grid(row=2, column=0, padx=(0,15), pady=(0,15), sticky="ne")
        self.grammar_box = Text(self.grammar_frame, height=5, width=35, wrap="word", font=("Segoe UI",10),relief="flat")
        self.grammar_box.grid(row=0, column=0, padx=7, pady=7, sticky="ne")
        self.grammar_box.insert("0.0", "Grammar checker stuff will go here...")
        self.grammar_box.configure(state="disabled")
        # ! ==========================================
        # ! ==========================================
        self.variable = tkinter.IntVar()
        
        self.def_type_frame = ttk.LabelFrame(self.right_hand_frame, text="Definition Type", style="Card.TFrame")
        self.def_type_frame.grid(row=3, column=0, padx=(0,15), pady=(0,15), sticky="new")
        self.def_type_frame.grid_rowconfigure(0, weight=1)
        self.def_type_frame.grid_rowconfigure(1, weight=1)
        self.def_type_frame.grid_rowconfigure(2, weight=1)
        self.def_type_frame.grid_rowconfigure(3, weight=1)
        self.def_type_frame.grid_columnconfigure(0, weight=1)
        
        # self.def_type_label = ttk.Label(self.def_type_frame, text="Definition Type", anchor="center")
        # self.def_type_label.grid(row=0, column=0, padx=10, pady=10, sticky="news")         
        
        self.Hardcoded_rad = ttk.Radiobutton(master=self.def_type_frame,  text="Hardcoded ??? []", variable=self.variable, value=0)
        self.Hardcoded_rad.grid(row=0, column=0, padx=10, pady=10, sticky="news")  
    
        self.Context_rad = ttk.Radiobutton(master=self.def_type_frame,  text="Context ??? (())", variable=self.variable, value=1)
        self.Context_rad.grid(row=1, column=0, padx=10, pady=10, sticky="news")  
        
        self.Variable_rad = ttk.Radiobutton(master=self.def_type_frame,  text="Variable ??? {}", variable=self.variable, value=2)
        self.Variable_rad.grid(row=2, column=0, padx=10, pady=10, sticky="news")  
        # ! ==========================================
        # ! ==========================================
        
        self.text_buttons_frame = ttk.Frame(self.right_hand_frame, style="Card.TFrame")
        self.text_buttons_frame.grid(row=4, column=0, padx=(0,15), pady=(0,15), sticky="news")
        self.text_buttons_frame.columnconfigure((0,1,2), weight=1)
        
        
        self.def_save = ttk.Button(self.text_buttons_frame, text="Save", state="normal", command=self.save_textbox)
        self.def_save.grid(row=0, column=0, padx=(7,0), pady=7, sticky="ew")
        
        self.def_edit = ttk.Button(self.text_buttons_frame, text="Edit", state="disabled")
        self.def_edit.grid(row=0, column=1, padx=(7,0), pady=7, sticky="ew")
        
        self.def_cancel = ttk.Button(self.text_buttons_frame, text="Cancel", state="disabled")
        self.def_cancel.grid(row=0, column=2, padx=7, pady=7, sticky="ew")
        
        # TODO: Add definition types, save/edit/cancel buttons for text box
        
                # * Button to create a new definition
        # self.add_button = ttk.Button(self.creation_frame, text="Definition") 
        # self.add_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.longDesc_frame = ttk.Frame(self.tabControl, style="Card.TFrame")
        self.longDesc_frame.grid(row=0, column=0, padx=7, pady=7, sticky="news")
        
        self.shortDesc_frame = ttk.Frame(self.tabControl, style="Card.TFrame")
        self.shortDesc_frame.grid(row=0, column=0, padx=7, pady=7, sticky="news")
        
        self.greet_frame = ttk.Frame(self.tabControl, style="Card.TFrame")
        self.greet_frame.grid(row=0, column=0, padx=7, pady=7, sticky="news")
        
        self.tabControl.add(self.creation_frame, text="Definitions")
        self.tabControl.add(self.longDesc_frame, text="Long Description")
        self.tabControl.add(self.shortDesc_frame, text="Short Description")
        self.tabControl.add(self.greet_frame, text="Greeting")
        # self.tabControl.rowconfigure(0, weight=1)
        # self.tabControl.columnconfigure(0, weight=1)        
            
        # self.stupid = ttk.Button(self.creation_frame, text="Dumbass Fucko")
        # self.stupid.grid(row=0, column=0, padx=7, pady=7, sticky="nsew")      
        
        self.total_character_count = 0
        self.current_def_length = 0
        self.before_edit_def = ""
        self.after_edit_def = ""
        self.current_active_definition = ""
        
        self.deff_num = 0
        self.my_definitions = []
        # self.trVi_pos = []
        self.select_active = False # Keeps track of whether or not select button is being used
    # ! ====================================================================
    # ! Shows main character creation screen after new character button is created and fits menu to screen properly
    # ! ====================================================================
    def show_character_creation(self):
        self.initial_create_frame.grid_forget()
        self.tabControl.pack(fill="both", expand=1)
    # ! ====================================================================      
    def add_definition(self):
        def_num = str(self.deff_num)
        def_name = "Def" + def_num
        tree_view_pos = "Pos" + def_num
        placeholder = "Click here to edit this definition..."
        placeholder = (placeholder.replace(" ", "\ ")) # ! .replace() needed because [values] expects a tuple, this fixes that problem
        # List of treeview item names just in case
        self.my_definitions.append(def_name)
        # Inserts new definition into treeview
        self.tree.insert("", 'end', text=self.my_definitions[self.deff_num], values=placeholder)
        self.deff_num += 1
    
    def select_definition(self):
        if not self.select_active:
            # Changes select button text and style along with treeview mode
            self.delete_def.grid(row=0, column=2, padx=(0,15), pady=(15,0), sticky="w")
            self.tree.configure(selectmode="extended")
            self.select_def.configure(text="Cancel", style="Accent.TButton")
            self.select_active = True
        else:
            # Deselects all treeview items when selection is cancelled
            for item in self.tree.selection():
                self.tree.selection_remove(item)
                
            # Resets select button text and style along with treeview mode
            self.select_def.configure(text="Select", style="Toggle.TButton")
            self.delete_def.grid_remove()
            self.tree.configure(selectmode="browse")
            self.select_active = False
            
    def delete_definition(self):
        for item in self.tree.selection():
            self.tree.delete(item)
    
    # Demo function to test treeview column header as a button
    def dumbass(self):
        print("raviollloi")
        # self.tree.configure(selectmode="none")
       
    # TODO: Treeview item is not updated without being selected again, so character counter increments when item is not reselected
    # Reacts to treeview item being selected
    def selectItem(self, event):
        curItem = self.tree.focus()
        self.current_active_definition = curItem
        temp = self.tree.item(curItem)['values']
        temp = str(temp)
        temp = temp[2:]
        temp = temp[:-2]
        self.before_edit_def = temp
        if "Click here to edit this definition..." in temp:
            self.update()
        elif self.after_edit_def == self.before_edit_def:
            print(self.after_edit_def)
            self.update()
        else:
            self.current_def_length = len(temp)
            self.total_character_count += self.current_def_length
            counted = "Character Count: " + str(self.total_character_count) + " / 3200"
            self.char_def_counter.configure(text=counted)
            self.update()
        # Removes wrapper characters to make editing definitions easier
        temp = str(temp).replace("((", "")
        temp = str(temp).replace("))", "")
        temp = str(temp).replace("[", "")
        temp = str(temp).replace("]", "")
        temp = str(temp).replace("{", "")
        temp = str(temp).replace("}", "")

        # Inserts treeview item text into textbox
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", temp)
        # self.textbox.configure(state="disabled")
        
    def save_textbox(self):
        box_text = str(self.textbox.get("0.0", "end"))
        formatted = box_text.rstrip('\r\n') # Removes return inputs and newlines
        temp_len = len(formatted)
        # Adds formatting for definitions
        # ===========================
        if self.variable.get() == 0:
            formatted = "[" + formatted + "]"
            temp_len += 2
        elif self.variable.get() == 1:
            formatted = "((" + formatted + "))"
            temp_len += 4
        elif self.variable.get() == 2:
            formatted = "{" + formatted + "}"
            temp_len += 2
        self.after_edit_def = formatted
        if formatted == self.before_edit_def:
            self.update() 
            print(self.before_edit_def)
        else:
            self.current_def_length -= temp_len
            if self.current_def_length < 0:
                self.current_def_length *= -1
            
            self.total_character_count += self.current_def_length
            self.current_def_length = 0
            counted = "Character Count: " + str(self.total_character_count) + " / 3200"
            self.char_def_counter.configure(text=counted)
            self.update()
        formatted = formatted.replace("{", "\{")
        formatted = formatted.replace("}", "\}")
        # ===========================
        formatted = formatted.replace(" ", "\ ")
        self.tree.item(self.current_active_definition, values=formatted)