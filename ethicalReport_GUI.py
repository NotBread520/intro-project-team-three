# CS110 - Group 3 - Final Group Project - EthicalReport - 3/9/2026
#
#  Project Members:
#   Luc DeBenon
#   Jacob Gilseth
#   Xander Mickelson
#
# This python program creates and configures the GUI for the EthicalReport software project.
# It also saves the data collected from the GUI into the data_stored.py file,
# and generates a final markdown report.

import random
from datetime import date
import tkinter as tk
from tkinter import ttk, PhotoImage

import data_stored
import report_generator


# APPMANAGER
class AppManager(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main Window Settings
        self.title("EthicalReport v1.0")
        self.geometry("1200x700")
        self.resizable(False, False)

        
        # Tkinter Styling Configuration: we create some default 'styles' that we can easily assign to any label or button with style='stylename'
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Header.TLabel', font=('Calibri', 32, 'bold'))
        style.configure('Notes.TLabel', font=('Calibri', 12))
        style.configure('Default.TLabel', font=('Calibri', 12))
        style.configure('Default.TButton', font=('Calibri', 12))
        style.configure('Default.Horizontal.TProgressbar', background='#bee8a5')


        # Report ID - Using today's date and a randomly generated, unique number, we use an fstring to create a unique ID we use as the file name and to track the report.
        currentDate = str(date.today())
        uniqueID = str(random.randint(1000, 9999))
        global reportID 
        reportID = f"ER-{currentDate}-{uniqueID}"
        data_stored.reporter_data["Report ID"] = reportID

        # Create a Container Widget to hold the Frames
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)


        # Configure the Container grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Store all pages
        self.frames = {}

        for page in (hello, reportDetails, incidentDetails, resolve, finalize):
            frame = page(parent=container, controller=self)
            self.frames[page.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("hello")
    
    #APPMANAGER Functions
    def show_frame(self, page_name): #Manages page selection in GUI
        frame = self.frames[page_name]
        frame.tkraise()

    def save_data(self, description, widget_or_value): #Records tkinger entry() fields as workable data in our data_stored file
        try:
            data_stored.reporter_data[description] = widget_or_value.get()
        except AttributeError:
            data_stored.reporter_data[description] = widget_or_value


# PAGES - Each class object defines one of the forms required to fill out an EthicalReport document

# Hello Page - The first page you see when you open the program.
class hello(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME - Included on each page, provides a title and instructions for the forms
        headerFrame = ttk.Frame(self)
        headerFrame.pack(side="top")

        logo = PhotoImage(file = "resources\\EthicalReport_Logo.pbm")
        logoLabel =  ttk.Label(headerFrame, image=logo)
        logoLabel.image = logo
        logoLabel.grid(row=0, column=0, sticky="s", pady=50, padx=50)

        # BODY FRAME - Included on each page, the main body contents of the form, especially entries for report information
        bodyFrame = ttk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        helloNote = ttk.Label(bodyFrame, text="Welcome to the EthicalReport Reporting Tool. Use the \"Next\" and \"Previous\" buttons to navigate through the form.", style='Notes.TLabel')
        helloNote.grid(row=1, column=0, sticky="s", pady=10, padx=10)
        

        # NAVIGATION FRAME - Included on each page, a progress bar and buttons to navigate between form pages
        navFrame = ttk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", state="disabled", style='Default.TButton')
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(navFrame, text="Next", command=lambda: controller.show_frame("reportDetails"), style='Default.TButton')
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

# The Progress bar is statically fit to the bottom edge. Since we know the number and order of pages we simply set a static progress bar value per page.
        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=900, mode="determinate", maximum=10, style='Default.Horizontal.TProgressbar') 
        progressBar["value"] = 0
        progressBar.grid(row=0, column=1, padx=10, pady=10)



# Report Details Page - Gathers information about the report itself.
class reportDetails(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = ttk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Report Details", style = 'Header.TLabel')
        header.grid(row=0, column=0, pady=10, padx=10)

        headerNote = ttk.Label(headerFrame, text="Provide details about the report. Selecting the \"Remain Anonymous\" button will not include your information in the report.", style='Notes.TLabel')
        headerNote.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = ttk.Frame(self, width=500, height=200)
        bodyFrame.pack(padx=10, pady=10)

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

        typeSelectLabel = ttk.Label(headerFrame, text="Select the type of report:", style='Notes.TLabel')
        typeSelectLabel.grid(row=2, column=0, pady=10, padx=10)

        hReportButton = ttk.Button(
            bodyFrame,
            text="Harassment",
            command=lambda: controller.save_data("Report Type", "Harassment"),
            style='Default.TButton'
        )
        hReportButton.grid(row=3, column=0, padx=10, pady=10, ipadx = 40, ipady = 30)

        dReportButton = ttk.Button(
            bodyFrame,
            text="Discrimination",
            command=lambda: controller.save_data("Report Type", "Discrimination"),
            style='Default.TButton'
        )
        dReportButton.grid(row=3, column=1, padx=10, pady=10, ipadx = 40, ipady = 30)

        rReportButton = ttk.Button(
            bodyFrame,
            text="Retaliation",
            command=lambda: controller.save_data("Report Type", "Retaliation"),
            style='Default.TButton'
        )
        rReportButton.grid(row=3, column=2, padx=10, pady=10, ipadx = 40, ipady = 30)

        reportDateLabel = ttk.Label(bodyFrame, text="Report Date: ", style='Default.TLabel')
        reportDateLabel.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        reportDateEntry = ttk.Entry(bodyFrame, width=30)
        reportDateEntry.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        reportTimeLabel = ttk.Label(bodyFrame, text="Time of Report: ", style='Default.TLabel')
        reportTimeLabel.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        reportTimeEntry = ttk.Entry(bodyFrame, width=30)
        reportTimeEntry.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        isAnonymous = tk.BooleanVar(value=False)
        isAnonymousLabel = ttk.Label(bodyFrame, text="Remain Anonymous: ", style='Default.TLabel')
        isAnonymousLabel.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        isAnonymousToggle = ttk.Checkbutton(
            bodyFrame,
            variable=isAnonymous,
            onvalue=True,
            offvalue=False,
            command=toggle_reporter_details
        )
        isAnonymousToggle.grid(row=6, column=1, sticky="w", padx=5, pady=5)

        reporterNameLabel = ttk.Label(bodyFrame, text="Reporter Name: ", style='Default.TLabel')
        reporterNameLabel.grid(row=7, column=0, sticky="w", padx=5, pady=5)
        reporterNameEntry = ttk.Entry(bodyFrame, width=30)
        reporterNameEntry.grid(row=7, column=1, sticky="w", padx=5, pady=5)

        reporterEmailLabel = ttk.Label(bodyFrame, text="Reporter Email: ", style='Default.TLabel')
        reporterEmailLabel.grid(row=8, column=0, sticky="w", padx=5, pady=5)
        reporterEmailEntry = ttk.Entry(bodyFrame, width=30)
        reporterEmailEntry.grid(row=8, column=1, sticky="w", padx=5, pady=5)

        reporterPhoneLabel = ttk.Label(bodyFrame, text="Reporter Phone Number: ", style='Default.TLabel')
        reporterPhoneLabel.grid(row=9, column=0, sticky="w", padx=5, pady=5)
        reporterPhoneEntry = ttk.Entry(bodyFrame, width=30)
        reporterPhoneEntry.grid(row=9, column=1, sticky="w", padx=5, pady=5)

        reporterRoleLabel = ttk.Label(bodyFrame, text="Reporter Position: ", style='Default.TLabel')
        reporterRoleLabel.grid(row=10, column=0, sticky="w", padx=5, pady=5)
        reporterRoleEntry = ttk.Entry(bodyFrame, width=30)
        reporterRoleEntry.grid(row=10, column=1, sticky="w", padx=5, pady=5)

        def save_report_data():
            controller.save_data("Report Date", reportDateEntry)
            controller.save_data("Report Time", reportTimeEntry)
            controller.save_data("Anonymous", isAnonymous)

            if not isAnonymous.get():
                controller.save_data("Reporter Name", reporterNameEntry)
                controller.save_data("Reporter Email", reporterEmailEntry)
                controller.save_data("Reporter Phone", reporterPhoneEntry)
                controller.save_data("Reporter Role", reporterRoleEntry)

        # NAVIGATION FRAME
        navFrame = ttk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("hello"), style='Default.TButton')
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(
            navFrame,
            text="Next",
            command=lambda: [save_report_data(), controller.show_frame("incidentDetails")],
            style='Default.TButton'
        )
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=900, mode="determinate", maximum=100, style='Default.Horizontal.TProgressbar')
        progressBar["value"] = 25
        progressBar.grid(row=0, column=1, padx=10, pady=10)

# Indcident Details Page - Gathers information about the incident being reported
class incidentDetails(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = ttk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Incident Details", style = 'Header.TLabel')
        header.grid(row=0, column=0, pady=10, padx=10)
        headerInfo = ttk.Label(headerFrame, text="Provide information about the incident being reported.", style='Notes.TLabel')
        headerInfo.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = ttk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        incidentDateLabel = ttk.Label(bodyFrame, text="Incident Date: ", style='Default.TLabel')
        incidentDateLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        incidentDateEntry = ttk.Entry(bodyFrame, width=30)
        incidentDateEntry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        incidentTimeLabel = ttk.Label(bodyFrame, text="Incident Time: ", style='Default.TLabel')
        incidentTimeLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        incidentTimeEntry = ttk.Entry(bodyFrame, width=30)
        incidentTimeEntry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        incidentLocationLabel = ttk.Label(bodyFrame, text="Incident Location: ", style='Default.TLabel')
        incidentLocationLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        incidentLocationEntry = ttk.Entry(bodyFrame, width=30)
        incidentLocationEntry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        accusedNameLabel = ttk.Label(bodyFrame, text="Reported Person's Name: ", style='Default.TLabel')
        accusedNameLabel.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        accusedNameEntry = ttk.Entry(bodyFrame, width=30)
        accusedNameEntry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        accusedRoleLabel = ttk.Label(bodyFrame, text="Reported Person's Role: ", style='Default.TLabel')
        accusedRoleLabel.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        accusedRoleEntry = ttk.Entry(bodyFrame, width=30)
        accusedRoleEntry.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        descriptionLabel = ttk.Label(bodyFrame, text="Incident Description: ", style='Default.TLabel')
        descriptionLabel.grid(row=5, column=0, sticky="nw", padx=5, pady=5)
        descriptionText = tk.Text(bodyFrame, width=50, height=8)
        descriptionText.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        witnessesLabel = ttk.Label(bodyFrame, text="Witnesses: ", style='Default.TLabel')
        witnessesLabel.grid(row=6, column=0, sticky="nw", padx=5, pady=5)
        witnessesText = tk.Text(bodyFrame, width=50, height=5)
        witnessesText.grid(row=6, column=1, sticky="w", padx=5, pady=5)

        def save_incidentDetails():
            controller.save_data("Incident Date", incidentDateEntry)
            controller.save_data("Incident Time", incidentTimeEntry)
            controller.save_data("Incident Location", incidentLocationEntry)
            controller.save_data("Accused Name", accusedNameEntry)
            controller.save_data("Accused Role", accusedRoleEntry)
            controller.save_data("Incident Description", descriptionText.get("1.0", "end").strip())
            controller.save_data("Witnesses", witnessesText.get("1.0", "end").strip())

        # NAVIGATION FRAME
        navFrame = ttk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("reportDetails"), style='Default.TButton')
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(
            navFrame,
            text="Next",
            command=lambda: [save_incidentDetails(), controller.show_frame("resolve")],
            style='Default.TButton'
        )
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=900, mode="determinate", maximum=100, style='Default.Horizontal.TProgressbar')
        progressBar["value"] = 50
        progressBar.grid(row=0, column=1, padx=10, pady=10)

# Resolution Page - Allows the filer to indicate the resolution process they'd like to go through regarding this report
class resolve(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = ttk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Resolution Process Request", style = 'Header.TLabel')
        header.grid(row=0, column=0, pady=10, padx=10)
        headerInfo = ttk.Label(headerFrame, text="Please select how you'd like this report to be handled:", style='Notes.TLabel')
        headerInfo.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = ttk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        internalInvestigationButton = ttk.Button(
            bodyFrame,
            text="Internal HR Investigation",
            command=lambda: controller.save_data("Resolution Request", "Internal"),
            style='Default.TButton'
        )
        internalInvestigationButton.grid(row=2, column=0, padx=10, pady=10, ipadx = 40, ipady = 30)

        PeerReviewButton = ttk.Button(
            bodyFrame,
            text="Peer Review",
            command=lambda: controller.save_data("Resolution Request", "Peer Review"),
            style='Default.TButton'
        )
        PeerReviewButton.grid(row=2, column=1, padx=10, pady=10, ipadx = 40, ipady = 30)

        thirdPartyInvestigationButton = ttk.Button(
            bodyFrame,
            text="Third Party Investigation",
            command=lambda: controller.save_data("Resolution Request", "Third Party"),
            style='Default.TButton'
        )
        thirdPartyInvestigationButton.grid(row=2, column=2, padx=10, pady=10, ipadx = 40, ipady = 30)

        # Comment Box
        commentFrame = ttk.Frame(self)
        commentFrame.pack(padx=10, pady=10)
        resolutionLabel = ttk.Label(commentFrame, text="Please provide any additional comments or information here:", style='Notes.TLabel')
        resolutionLabel.grid(row=0, column=1, sticky="s", padx=5, pady=5)
        resolutionText = tk.Text(commentFrame, width=100, height=16)
        resolutionText.grid(row=1, column=1, sticky="s", padx=5, pady=5)
        

        def save_resolution():
            controller.save_data("Resolution Comment", resolutionText.get("1.0", "end").strip())

        # NAVIGATION FRAME
        navFrame = ttk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("incidentDetails"), style='Default.TButton')
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(
            navFrame,
            text="Next",
            command=lambda: [save_resolution(), controller.show_frame("finalize")],
            style='Default.TButton'
        )
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=900, mode="determinate", maximum=100, style='Default.Horizontal.TProgressbar')
        progressBar["value"] = 75
        progressBar.grid(row=0, column=1, padx=10, pady=10)

# Finalize Page - Wraps up the process by providing the report ID and generating the file.
class finalize(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = ttk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Report Complete", style = 'Header.TLabel')
        header.grid(row=0, column=0, pady=10, padx=10)
        headerInfo = ttk.Label(headerFrame, text=f"Your Report ID is: {reportID}", style='Notes.TLabel')
        headerInfo.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = ttk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        finishLabel = ttk.Label(
            bodyFrame,
            text="Click Finish to generate and save your markdown report.",
            style='Notes.TLabel'
        )
        finishLabel.pack(pady=20)

        def finish_report():
            report_generator.save_markdown_report(data_stored.reporter_data)
            controller.destroy()

        # NAVIGATION FRAME
        navFrame = ttk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("resolve"), style='Default.TButton')
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonFinish = ttk.Button(navFrame, text="Finish", command=finish_report, style='Default.TButton')
        navButtonFinish.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=900, mode="determinate", maximum=100, style='Default.Horizontal.TProgressbar')
        progressBar["value"] = 100
        progressBar.grid(row=0, column=1, padx=10, pady=10)


# EXECUTE - Final stage of the program: we simply call the AppManager() to run its tkinter mainloop(), launching the GUI.
AppManager().mainloop()

# Optional for debugging: pring the contents of the stored data file. This is disabled by default to protect privacy.
#print(data_stored.reporter_data)