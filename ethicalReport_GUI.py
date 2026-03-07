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
# https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/
#
# -------------------------------------------------------

import tkinter as tk
from tkinter import ttk

import data_stored

# APPMANAGER
class AppManager(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main Window Settings
        self.title("EthicalReport v1.0")
        self.geometry("1200x700")
        self.resizable(False, False)

        # Create a Container Widget to hold the Frames, which represent each "page" of the report process
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Configure the Container grid to expand, to fill the full window
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create a dict object to store all the Frames
        self.frames = {}

        # Loop to add each page to the self.frames list
        for page in (hello, reportDetails, incidentDetails1, incidentDetails2, incidentDetails3, resolve, finalize):
            frame = page(parent=container, controller=self)
            self.frames[page.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("hello")

    # Defining a function to "raise" the desired frame to the front of the stack of frames
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # Defining a function that saves inputs from entries to a dictionary on data_stored.py
    def save_data(self, description, entry):
        data_stored.reporter_data[description] = entry.get()


# PAGES
class hello(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
       
        
        # HEADER FRAME
        headerFrame = tk.Frame(self, width = 0, height = 0)
        headerFrame.pack(side = "top")
        header = ttk.Label(headerFrame, text="Welcome", font=("Calibri", 30, "bold"))
        header.pack(pady = 10)


        # BODY FRAME
        bodyFrame = tk.Frame(self, width = 0, height = 0)
        bodyFrame.pack(padx = 10, pady = 10)

        typeReportLabel = ttk.Label(bodyFrame, text="Type of Report", font=("Calibri", 20))
        typeReportLabel.grid(row=1, column=1, sticky="sW", padx=10, pady=10)

        hReportButton = ttk.Button(bodyFrame, text="Harassment").grid(row = 2, column = 0, sticky="", padx = 10, pady = 10)
        dReportButton = ttk.Button(bodyFrame, text="Discrimination").grid(row = 2, column = 1, sticky="", padx = 10, pady = 10)
        rReportButton = ttk.Button(bodyFrame, text="Retaliation").grid(row = 2, column = 2, sticky="", padx = 10, pady = 10)


        # NAVIGATION FRAME
        navFrame = tk.Frame(self, width=0, height = 0)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", state = "disabled")
        navButtonPrev.grid(row=0, column=0, sticky="", padx=10, pady=10)
        navButtonPrev.grid(row=0, column=0, sticky="", padx=5, pady=5)

        navButtonNext = ttk.Button(navFrame, text="Next", command=lambda: controller.show_frame("reportDetails"))
        navButtonNext.grid(row = 0, column = 2, sticky = "")
        navButtonNext.grid(row = 0, column = 2, sticky = "", padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 0
        progressBar.grid(row = 0, column = 1, padx = 10, pady = 10)

class reportDetails(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self, width = 0, height = 0)
        headerFrame.pack(side = "top")
        header = ttk.Label(headerFrame, text="Report Details", font = ("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10, sticky="")
        headerInfo = ttk.Label(headerFrame, text="Please fill in the following data:", font = ("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10, sticky="")


        # BODY FRAME
        bodyFrame = tk.Frame(self, width = 500, height = 200)
        bodyFrame.pack(padx = 10, pady = 10)

        # based what the isAnonymousToggle is toggled to displayy Reporter detail questions
        def toggle_reporter_details():
            if isAnonymous.get():
                reporterNameLabel.grid_remove()
                reporterNameEntry.grid_remove()
                reporterEmailLabel.grid_remove()
                reporterEmailEntry.grid_remove()
                reporterPhoneLabel.grid_remove()
                reporterPhoneEntry.grid_remove()
                reporterRoleLabel.grid_remove()
                reporterRoleEntry.grid_remove()
            else:
                reporterNameLabel.grid()
                reporterNameEntry.grid()
                reporterEmailLabel.grid()
                reporterEmailEntry.grid()
                reporterPhoneLabel.grid()
                reporterPhoneEntry.grid()
                reporterRoleLabel.grid()
                reporterRoleEntry.grid()



        # Questions
        reportDateLabel = ttk.Label(bodyFrame, text="Report date: ", font=("Calibri", 12))
        reportDateLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        reportDateEntry = ttk.Entry(bodyFrame, width=30)
        reportDateEntry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        reportTimeLabel = ttk.Label(bodyFrame, text="Time of report: ", font=("Calibri", 12))
        reportTimeLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        reportTimeEntry = ttk.Entry(bodyFrame, width=30)
        reportTimeEntry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        isAnonymous = tk.BooleanVar(value=False)
        isAnonymousLabel = ttk.Label(bodyFrame, text="Remain anonymous: ", font=("Calibri", 12))
        isAnonymousLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        isAnonymousToggle = ttk.Checkbutton(bodyFrame, variable=isAnonymous, onvalue=True, offvalue=False, command=toggle_reporter_details)
        isAnonymousToggle.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        reporterNameLabel = ttk.Label(bodyFrame, text="Reporter name: ", font=("Calibri", 12))
        reporterNameLabel.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        reporterNameEntry = ttk.Entry(bodyFrame, width=30)
        reporterNameEntry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        reporterEmailLabel = ttk.Label(bodyFrame, text="Reporter email: ", font=("Calibri", 12))
        reporterEmailLabel.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        reporterEmailEntry = ttk.Entry(bodyFrame, width=30)
        reporterEmailEntry.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        reporterPhoneLabel = ttk.Label(bodyFrame, text="Reporter phone number: ", font=("Calibri", 12))
        reporterPhoneLabel.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        reporterPhoneEntry = ttk.Entry(bodyFrame, width=30)
        reporterPhoneEntry.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        reporterRoleLabel = ttk.Label(bodyFrame, text="Reporter position: ", font=("Calibri", 12))
        reporterRoleLabel.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        reporterRoleEntry = ttk.Entry(bodyFrame, width=30)
        reporterRoleEntry.grid(row=6, column=1, sticky="w", padx=5, pady=5)

        # function to save multiple variables for report details
        def Save_report_data():
            controller.save_data("Report Date", reportDateEntry)
            controller.save_data("Report Time", reportTimeEntry)
            if isAnonymous.get():
                controller.save_data("Anonymous", isAnonymous)
            else:    
                controller.save_data("Anonymous", isAnonymous)
                controller.save_data("Reporter Name", reporterNameEntry)
                controller.save_data("Reporter Email", reporterEmailEntry)
                controller.save_data("Reporter Phone", reporterPhoneEntry)
                controller.save_data("Reporter Role", reporterRoleEntry)
            # NAVIGATION FRAME
        navFrame = tk.Frame(self, width=0, height = 0)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("hello"))
        navButtonPrev.grid(row=0, column=0, sticky="", padx=10, pady=10)
        navButtonPrev.grid(row=0, column=0, sticky="", padx=5, pady=5)

        navButtonNext = ttk.Button(navFrame, text="Next", command=lambda: [Save_report_data(), controller.show_frame("incidentDetails1")])
        navButtonNext.grid(row = 0, column = 2, sticky = "")
        navButtonNext.grid(row = 0, column = 2, sticky = "", padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 20
        progressBar.grid(row = 0, column = 1, padx = 10, pady = 10)

class incidentDetails1(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self, width = 0, height = 0)
        headerFrame.pack(side = "top")
        header = ttk.Label(headerFrame, text="Incident Details", font = ("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10, sticky="")
        headerInfo = ttk.Label(headerFrame, text="Page 1", font = ("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10, sticky="")

        # BODY FRAME
        bodyFrame = tk.Frame(self, width = 0, height = 0)
        bodyFrame.pack(padx = 10, pady = 10)

        # NAVIGATION FRAME
        navFrame = tk.Frame(self, width=0, height = 0)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("reportDetails"))
        navButtonPrev.grid(row=0, column=0, sticky="", padx=10, pady=10)
        navButtonPrev.grid(row=0, column=0, sticky="", padx=5, pady=5)

        navButtonNext = ttk.Button(navFrame, text="Next", command=lambda: controller.show_frame("incidentDetails2"))
        navButtonNext.grid(row = 0, column = 2, sticky = "")
        navButtonNext.grid(row = 0, column = 2, sticky = "", padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 40
        progressBar.grid(row = 0, column = 1, padx = 10, pady = 10)

class incidentDetails2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self, width = 0, height = 0)
        headerFrame.pack(side = "top")
        header = ttk.Label(headerFrame, text="Incident Details", font = ("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10, sticky="")
        headerInfo = ttk.Label(headerFrame, text="Page 2", font = ("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10, sticky="")

        # BODY FRAME
        bodyFrame = tk.Frame(self, width = 0, height = 0)
        bodyFrame.pack(padx = 10, pady = 10)

        # NAVIGATION FRAME
        navFrame = tk.Frame(self, width=0, height = 0)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("incidentDetails1"))
        navButtonPrev.grid(row=0, column=0, sticky="", padx=10, pady=10)
        navButtonPrev.grid(row=0, column=0, sticky="", padx=5, pady=5)

        navButtonNext = ttk.Button(navFrame, text="Next", command=lambda: controller.show_frame("incidentDetails3"))
        navButtonNext.grid(row = 0, column = 2, sticky = "")
        navButtonNext.grid(row = 0, column = 2, sticky = "", padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 60
        progressBar.grid(row = 0, column = 1, padx = 10, pady = 10)

class incidentDetails3(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self, width = 0, height = 0)
        headerFrame.pack(side = "top")
        header = ttk.Label(headerFrame, text="Incident Details", font = ("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10, sticky="")
        headerInfo = ttk.Label(headerFrame, text="Page 3", font = ("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10, sticky="")

        # BODY FRAME
        bodyFrame = tk.Frame(self, width = 0, height = 0)
        bodyFrame.pack(padx = 10, pady = 10)

        # NAVIGATION FRAME
        navFrame = tk.Frame(self, width=0, height = 0)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("incidentDetails2"))
        navButtonPrev.grid(row=0, column=0, sticky="", padx=10, pady=10)
        navButtonPrev.grid(row=0, column=0, sticky="", padx=5, pady=5)

        navButtonNext = ttk.Button(navFrame, text="Next", command=lambda: controller.show_frame("resolve"))
        navButtonNext.grid(row = 0, column = 2, sticky = "")
        navButtonNext.grid(row = 0, column = 2, sticky = "", padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 80
        progressBar.grid(row = 0, column = 1, padx = 10, pady = 10)

class resolve(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self, width = 0, height = 0)
        headerFrame.pack(side = "top")
        header = ttk.Label(headerFrame, text="Resolution Process", font = ("Calibri", 30, "bold"))
        header = ttk.Label(headerFrame, text="Resolution Process Request", font = ("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10, sticky="")
        headerInfo = ttk.Label(headerFrame, text="Please select the desired resolution process.", font = ("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10, sticky="")

        # BODY FRAME
        bodyFrame = tk.Frame(self, width = 0, height = 0)
        bodyFrame.pack(padx = 10, pady = 10)

        # NAVIGATION FRAME
        navFrame = tk.Frame(self, width=0, height = 0)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("incidentDetails3"))
        navButtonPrev.grid(row=0, column=0, sticky="", padx=10, pady=10)
        navButtonPrev.grid(row=0, column=0, sticky="", padx=5, pady=5)

        navButtonNext = ttk.Button(navFrame, text="Next", command=lambda: controller.show_frame("finalize"))
        navButtonNext.grid(row = 0, column = 2, sticky = "")
        navButtonNext.grid(row = 0, column = 2, sticky = "", padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 90
        progressBar.grid(row = 0, column = 1, padx = 10, pady = 10)

class finalize(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self, width = 0, height = 0)
        headerFrame.pack(side = "top")
        header = ttk.Label(headerFrame, text="Report Complete", font = ("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10, sticky="")
        headerInfo = ttk.Label(headerFrame, text="Your Report ID is: ", font = ("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10, sticky="")

        # BODY FRAME
        bodyFrame = tk.Frame(self, width = 0, height = 0)
        bodyFrame.pack(padx = 10, pady = 10)

        # NAVIGATION FRAME
        navFrame = tk.Frame(self, width=0, height = 0)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("resolve"))
        navButtonPrev.grid(row=0, column=0, sticky="", padx=10, pady=10)
        navButtonPrev.grid(row=0, column=0, sticky="", padx=5, pady=5)

        navButtonFinish = ttk.Button(navFrame, text="Finish", command=lambda: controller.destroy())
        navButtonFinish.grid(row=0, column=2, sticky="", padx=10, pady=10)

        navButtonFinish.grid(row=0, column=2, sticky="", padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 100
        progressBar.grid(row = 0, column = 1, padx = 10, pady = 10)

# EXECUTE
AppManager().mainloop()
print (data_stored.reporter_data)
