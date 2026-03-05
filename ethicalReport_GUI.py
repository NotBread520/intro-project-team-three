# CS110 - Group 3 - Final Group Project - EthicalReport - 3/4/2026
# Project Members:
#   Luc DeBenon
#   Jacob Gilseth
#   Xander Mickelson
#
# This python document is a temporary program that creates and configures the GUI for the EthicalReport software project. It can be used to test new features, make adjustments, or to copy from as we develop the final EthicalReport software.
#
# -------------------------------------------------------
#
# SOURCES:
# https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
# https://python.swaroopch.com/oop.html
# https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk
# BRAVE AI Chat (all AI interactions will be properly documented in README.md)



# -------------------------------------------------------

import tkinter as tk
from tkinter import ttk

# -------------------------------------------------------

# VIEWMANAGER
class ViewManager(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Main Window Settings
        self.title("EthicalReport v1.0")
        self.geometry("1200x700")
        self.resizable(False, False)
        
        # Create a Container Widget to hold the Frames
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Configure the Container Grid to Expand, to fill the full window
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create a dict object to store all the frames
        self.frames = {}

        # Loop to add each page to the self.frames list
        for page in (Entry, reportDetails, incidentDetails1, incidentDetails2, incidentDetails3, Resolve, Finalize):
            frame = page(parent=container, controller=self)
            self.frames[page.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Entry")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

# PAGES
class Entry(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Entry Page")
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

        # BUTTONS
        button = ttk.Button(self, text="Next", command=lambda: controller.show_frame("reportDetails"))
        button.grid(row=1, column=0, sticky="se", padx=10, pady=10)

class reportDetails(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Report Details")
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nw")
        
        # BUTTONS
        button = ttk.Button(self, text="Previous", command=lambda: controller.show_frame("Entry"))
        button.grid(row=1, column=0, sticky="sW", padx=10, pady=10)

        button = ttk.Button(self, text="Next", command=lambda: controller.show_frame("incidentDetails1"))
        button.grid(row=1, column=0, sticky="se", padx=10, pady=10)

        
class incidentDetails1(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Incident Details - Page 1")
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

        #BUTTONS
        button = ttk.Button(self, text="Previous", command=lambda: controller.show_frame("reportDetails"))
        button.grid(row=1, column=0, sticky="sW", padx=10, pady=10)

        button = ttk.Button(self, text="Next", command=lambda: controller.show_frame("incidentDetails2"))
        button.grid(row=1, column=0, sticky="se", padx=10, pady=10)

class incidentDetails2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Incident Details - Page 2")
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

        #BUTTONS
        button = ttk.Button(self, text="Previous", command=lambda: controller.show_frame("incidentDetails1"))
        button.grid(row=1, column=0, sticky="sW", padx=10, pady=10)

        button = ttk.Button(self, text="Next", command=lambda: controller.show_frame("incidentDetails3"))
        button.grid(row=1, column=0, sticky="se", padx=10, pady=10)

class incidentDetails3(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Incident Details - Page 3")
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

        #BUTTONS
        button = ttk.Button(self, text="Previous", command=lambda: controller.show_frame("incidentDetails2"))
        button.grid(row=1, column=0, sticky="sW", padx=10, pady=10)

        button = ttk.Button(self, text="Next", command=lambda: controller.show_frame("Resolve"))
        button.grid(row=1, column=0, sticky="se", padx=10, pady=10)

class Resolve(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Resolution Page")
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

        #BUTTONS
        button = ttk.Button(self, text="Previous", command=lambda: controller.show_frame("reportDetails"))
        button.grid(row=1, column=0, sticky="sW", padx=10, pady=10)

        button = ttk.Button(self, text="Next", command=lambda: controller.show_frame("Finalize"))
        button.grid(row=1, column=0, sticky="se", padx=10, pady=10)

class Finalize(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Reporter Finalized")
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

        #BUTTONS
        button = ttk.Button(self, text="Previous", command=lambda: controller.show_frame("Resolve"))
        button.grid(row=1, column=0, sticky="sW", padx=10, pady=10)

        button = ttk.Button(self, text="Finish", command=lambda: controller.destroy())
        button.grid(row=1, column=0, sticky="se", padx=10, pady=10)

# EXECUTE
ViewManager().mainloop()
