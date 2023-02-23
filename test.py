# import customtkinter
# import tkinter as tk              # Python 3
# import tkinter.ttk as ttk
# import queue

# import multiprocessing as mp
# import time

# class App(customtkinter.CTk):

    
#     def __init__(self,):
#         super().__init__()

#         # configure window
#         self.title("CustomTkinter complex_example.py")
#         self.geometry(f"{1100}x{580}")
        
#         self.minsize(800, 500)
#                 # set grid layout 1x2
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)
#          # create navigation frame
#         self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
#         self.navigation_frame.grid(row=0, column=0, sticky="nsew")
#         self.navigation_frame.grid_rowconfigure(4, weight=1)


#         self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, 
#                                                    height=40, border_spacing=10, text="Create",font=customtkinter.CTkFont(size=18),
#                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
#                                                    width=100, anchor="w", command=self.home_button_event)
#         self.home_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

#         self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, 
#                                                       height=40, border_spacing=10, 
#                                                       text="Characters",font=customtkinter.CTkFont(size=18),
#                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
#                                                       width=100, anchor="w", command=self.frame_2_button_event)
#         self.frame_2_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

#         self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, 
#                                                       height=40, border_spacing=10, 
#                                                       text="Save",font=customtkinter.CTkFont(size=18),
#                                                       fg_color="transparent", 
#                                                       text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
#                                                       width=100, anchor="w", command=self.frame_3_button_event)
#         self.frame_3_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
#         self.appearance_mode_label = customtkinter.CTkLabel(self.navigation_frame, 
#                                                             text="Appearance Mode:", 
#                                                             anchor="w")
#         self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
#         self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, 
#                                                                 values=["Light", "Dark", "System"],
#                                                                 command=self.change_appearance_mode_event, 
#                                                                 width=90)
#         self.appearance_mode_menu.grid(row=6, column=0, padx=5, pady=5, sticky="s")

#     # ! Multiprocessing implementation (work in progress)
#     # ! ====================================================
#     # ! ====================================================

#         self.queue = mp.Queue()
#         self.process = None

#     def start_work(self):
#         self.process = mp.Process(target=self.work, args=(self.queue,))
#         # self.button.configure(state='disabled')
#         self.process.start()
#         self.periodic_call()

#     def periodic_call(self):
#         # check a queue once
#         self.check_queue()

#         # if exit code is None - process is on the run and we should re-schedule check
#         if self.process.exitcode is None:
#             self.after(100, self.periodic_call)
#         # things are executed
#         else:
#             self.process.join()
#             self.button.configure(state='normal')
#             self.label.configure(text='Waiting for "work"')
#             self.progressbar.configure(value=0)

#     def check_queue(self):
#         # common check of the queue
#         while self.queue.qsize():
#             try:
#                 self.label.configure(text=self.queue.get(0))
#                 self.progressbar.configure(value=self.progressbar['value'] + 1)
#             except queue.Empty:
#                 pass


#     def work(working_queue):
#         for type_of_work in ['Combobulationg Discombobulator', 'Pointing towards space',
#                             'Calculating Ultimate Answer']:
#             working_queue.put(type_of_work)
#             time.sleep(1.5)

#     # ! ====================================================
#     # ! ====================================================

#     def select_frame_by_name(self, name):
#             # set button color for selected button
#         self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
#         self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
#         self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

#         # show selected frame
#         if name == "home":
#             self.home_frame.grid(row=0, column=1, sticky="nsew")
#         else:
#             self.home_frame.grid_forget()
#         if name == "frame_2":
#             self.second_frame.grid(row=0, column=1, sticky="nsew")
#         else:
#             self.second_frame.grid_forget()
#         if name == "frame_3":
#             self.third_frame.grid(row=0, column=1, sticky="nsew")
#         else:
#             self.third_frame.grid_forget()

#     def home_button_event(self):
#         self.select_frame_by_name("home")

#     def frame_2_button_event(self):
#         self.select_frame_by_name("frame_2")

#     def frame_3_button_event(self):
#         self.select_frame_by_name("frame_3")

#     def change_appearance_mode_event(self, new_appearance_mode):
#         customtkinter.set_appearance_mode(new_appearance_mode)  
        

# customtkinter.set_appearance_mode("Light")      
        
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()  

# # import pyperclip as pc

# # text1 = "bitches"
# # pc.copy(text1)
import tkinter as tk
from functools import partial


def function(i):
    print("You toggled number %i"%i)
    print([var.get() for var in variables])


root = tk.Tk()
variables = []




# Create the new variable
variable = tk.IntVar()
variables.append(variable)

# Create the command using partial
command = partial(function, 0)

# Create the radio button
button = tk.Radiobutton(root, variable=variable, value=0, command=command)
button.pack()

command1 = partial(function, 1)

# Create the radio button
button1 = tk.Radiobutton(root, variable=variable, value=1, command=command)
button1.pack()

root.mainloop() 