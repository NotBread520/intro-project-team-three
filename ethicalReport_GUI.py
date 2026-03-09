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

import tkinter as tk
from tkinter import ttk

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

        # Temporary Report ID
        data_stored.reporter_data["Report ID"] = "ER-001"

        # Create a Container Widget to hold the Frames
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Configure the Container grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Store all pages
        self.frames = {}

        for page in (hello, reportDetails, incidentDetails1, incidentDetails2, incidentDetails3, resolve, finalize):
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


# PAGES - Each class object defines one of the 7 forms required to fill out an EthicalReport document
class hello(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME - Included on each page, provides a title and instructions for the forms
        headerFrame = tk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Welcome", font=("Calibri", 30, "bold"))
        header.pack(pady=10)

        # BODY FRAME - Included on each page, the main body contents of the form including entries
        bodyFrame = tk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        typeReportLabel = ttk.Label(bodyFrame, text="Type of Report", font=("Calibri", 20))
        typeReportLabel.grid(row=1, column=1, sticky="sw", padx=10, pady=10)

        hReportButton = ttk.Button(
            bodyFrame,
            text="Harassment",
            command=lambda: controller.save_data("Report Type", "Harassment")
        )
        hReportButton.grid(row=2, column=0, padx=10, pady=10)

        dReportButton = ttk.Button(
            bodyFrame,
            text="Discrimination",
            command=lambda: controller.save_data("Report Type", "Discrimination")
        )
        dReportButton.grid(row=2, column=1, padx=10, pady=10)

        rReportButton = ttk.Button(
            bodyFrame,
            text="Retaliation",
            command=lambda: controller.save_data("Report Type", "Retaliation")
        )
        rReportButton.grid(row=2, column=2, padx=10, pady=10)

        # NAVIGATION FRAME - Included on each page, a progress bar and buttons to navigate between form pages
        navFrame = tk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", state="disabled")
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(navFrame, text="Next", command=lambda: controller.show_frame("reportDetails"))
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 0
        progressBar.grid(row=0, column=1, padx=10, pady=10)


class reportDetails(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Report Details", font=("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10)
        headerInfo = ttk.Label(headerFrame, text="Please fill in the following data:", font=("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = tk.Frame(self, width=500, height=200)
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
        isAnonymousToggle = ttk.Checkbutton(
            bodyFrame,
            variable=isAnonymous,
            onvalue=True,
            offvalue=False,
            command=toggle_reporter_details
        )
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
        navFrame = tk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("hello"))
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(
            navFrame,
            text="Next",
            command=lambda: [save_report_data(), controller.show_frame("incidentDetails1")]
        )
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 20
        progressBar.grid(row=0, column=1, padx=10, pady=10)


class incidentDetails1(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Incident Details", font=("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10)
        headerInfo = ttk.Label(headerFrame, text="Page 1", font=("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = tk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        incidentDateLabel = ttk.Label(bodyFrame, text="Incident date: ", font=("Calibri", 12))
        incidentDateLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        incidentDateEntry = ttk.Entry(bodyFrame, width=30)
        incidentDateEntry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        incidentTimeLabel = ttk.Label(bodyFrame, text="Incident time: ", font=("Calibri", 12))
        incidentTimeLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        incidentTimeEntry = ttk.Entry(bodyFrame, width=30)
        incidentTimeEntry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        incidentLocationLabel = ttk.Label(bodyFrame, text="Incident location: ", font=("Calibri", 12))
        incidentLocationLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        incidentLocationEntry = ttk.Entry(bodyFrame, width=30)
        incidentLocationEntry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        def save_incident_page_1():
            controller.save_data("Incident Date", incidentDateEntry)
            controller.save_data("Incident Time", incidentTimeEntry)
            controller.save_data("Incident Location", incidentLocationEntry)

        # NAVIGATION FRAME
        navFrame = tk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("reportDetails"))
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(
            navFrame,
            text="Next",
            command=lambda: [save_incident_page_1(), controller.show_frame("incidentDetails2")]
        )
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 40
        progressBar.grid(row=0, column=1, padx=10, pady=10)


class incidentDetails2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Incident Details", font=("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10)
        headerInfo = ttk.Label(headerFrame, text="Page 2", font=("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = tk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        accusedNameLabel = ttk.Label(bodyFrame, text="Reported person name: ", font=("Calibri", 12))
        accusedNameLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        accusedNameEntry = ttk.Entry(bodyFrame, width=30)
        accusedNameEntry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        accusedRoleLabel = ttk.Label(bodyFrame, text="Reported person role: ", font=("Calibri", 12))
        accusedRoleLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        accusedRoleEntry = ttk.Entry(bodyFrame, width=30)
        accusedRoleEntry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        descriptionLabel = ttk.Label(bodyFrame, text="Incident description: ", font=("Calibri", 12))
        descriptionLabel.grid(row=2, column=0, sticky="nw", padx=5, pady=5)
        descriptionText = tk.Text(bodyFrame, width=50, height=8)
        descriptionText.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        def save_incident_page_2():
            controller.save_data("Accused Name", accusedNameEntry)
            controller.save_data("Accused Role", accusedRoleEntry)
            controller.save_data("Incident Description", descriptionText.get("1.0", "end").strip())

        # NAVIGATION FRAME
        navFrame = tk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("incidentDetails1"))
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(
            navFrame,
            text="Next",
            command=lambda: [save_incident_page_2(), controller.show_frame("incidentDetails3")]
        )
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 60
        progressBar.grid(row=0, column=1, padx=10, pady=10)


class incidentDetails3(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Incident Details", font=("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10)
        headerInfo = ttk.Label(headerFrame, text="Page 3", font=("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = tk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        witnessesLabel = ttk.Label(bodyFrame, text="Witnesses: ", font=("Calibri", 12))
        witnessesLabel.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        witnessesText = tk.Text(bodyFrame, width=50, height=5)
        witnessesText.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        evidenceLabel = ttk.Label(bodyFrame, text="Evidence: ", font=("Calibri", 12))
        evidenceLabel.grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        evidenceText = tk.Text(bodyFrame, width=50, height=5)
        evidenceText.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        def save_incident_page_3():
            controller.save_data("Witnesses", witnessesText.get("1.0", "end").strip())
            controller.save_data("Evidence", evidenceText.get("1.0", "end").strip())

        # NAVIGATION FRAME
        navFrame = tk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("incidentDetails2"))
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(
            navFrame,
            text="Next",
            command=lambda: [save_incident_page_3(), controller.show_frame("resolve")]
        )
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 80
        progressBar.grid(row=0, column=1, padx=10, pady=10)


class resolve(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Resolution Process Request", font=("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10)
        headerInfo = ttk.Label(headerFrame, text="Please select the desired resolution process.", font=("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = tk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        resolutionLabel = ttk.Label(bodyFrame, text="Requested resolution: ", font=("Calibri", 12))
        resolutionLabel.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        resolutionText = tk.Text(bodyFrame, width=50, height=8)
        resolutionText.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        def save_resolution():
            controller.save_data("Resolution Request", resolutionText.get("1.0", "end").strip())

        # NAVIGATION FRAME
        navFrame = tk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("incidentDetails3"))
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonNext = ttk.Button(
            navFrame,
            text="Next",
            command=lambda: [save_resolution(), controller.show_frame("finalize")]
        )
        navButtonNext.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 90
        progressBar.grid(row=0, column=1, padx=10, pady=10)


class finalize(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # HEADER FRAME
        headerFrame = tk.Frame(self)
        headerFrame.pack(side="top")
        header = ttk.Label(headerFrame, text="Report Complete", font=("Calibri", 30, "bold"))
        header.grid(row=0, column=0, pady=10, padx=10)
        headerInfo = ttk.Label(headerFrame, text="Your Report ID is: ER-001", font=("Calibri", 12))
        headerInfo.grid(row=1, column=0, pady=10, padx=10)

        # BODY FRAME
        bodyFrame = tk.Frame(self)
        bodyFrame.pack(padx=10, pady=10)

        finishLabel = ttk.Label(
            bodyFrame,
            text="Click Finish to generate and save your markdown report.",
            font=("Calibri", 12)
        )
        finishLabel.pack(pady=20)

        def finish_report():
            report_generator.save_markdown_report(data_stored.reporter_data)
            controller.destroy()

        # NAVIGATION FRAME
        navFrame = tk.Frame(self)
        navFrame.pack(side="bottom")

        navButtonPrev = ttk.Button(navFrame, text="Previous", command=lambda: controller.show_frame("resolve"))
        navButtonPrev.grid(row=0, column=0, padx=5, pady=5)

        navButtonFinish = ttk.Button(navFrame, text="Finish", command=finish_report)
        navButtonFinish.grid(row=0, column=2, padx=5, pady=5)

        progressBar = ttk.Progressbar(navFrame, orient="horizontal", length=950, mode="determinate", maximum=100)
        progressBar["value"] = 100
        progressBar.grid(row=0, column=1, padx=10, pady=10)


# EXECUTE - Final stage of the program: we simply call the AppManager() to run its tkinter mainloop(), launching the GUI.
AppManager().mainloop()
print(data_stored.reporter_data)