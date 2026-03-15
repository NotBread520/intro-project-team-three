# EthicalReport
A workplace harassment, discrimination, and retaliation reporting tool that focuses on human-readable output.
---
## About This Project: EthicalReport v1.0
This project is software that helps employees create well formatted report documents for workplace harassment, discrimination, and retaliation incidents. The software aims to provide a human readable, portable markdown file. The resulting report includes information like date and time the incident occurred, the individuals involved, witnesses, a description of the incident, the compliance officer assigned to review the report, a report ID, and the report status. 

## Why EthicalReport Matters
Workplace harassment and discrimination reporting tools can be confusing, lack confidentiality, and the followup process is often opaque to the reporter. This can make the employee feel that the report is not being taken seriously, or has been simply ignored. If the company itself and the filing individual do not have proper records, it can be difficult to track and solve workplace incidents that satisfy all parties. By creating a comprehensive and human readable markdown file, we can create a digital record that helps hold the company accountable and keep the filer informed. EthicalReport is designed around an intuitive data structure that an HR team could quickly integrate into existing HR tools.

---

## Problems with Existing Reporting Tools
- Often complicated and confusing, using overly technical terminology, requiring unnecessary or exhaustive info, or presenting a confusing user infterface.
- Lack of confidentiality, which can result in fear of retaliation
- Reporters often receive no feedback regarding the report status and are provided with no information about how their report is being handled.

## Our Solution
- EthicalReport assists the user in documenting the incident as quickly and easily as possible with a simple GUI.
- It ensures that all the information necessary for seeking justice is present, helping the user cover all their bases legally.
- Provides a dated and organized report that can be used as the basis of investigations performed by the company or compliance organization.
- Provides information about the compliance officer and report status to hold the compliance team accountable for timely acknowledgement of the incident.
- Anonymizes the information as necessary to protect trust and avoid illegal retaliation.

---

## How to Use EthicalReport
1. EthicalReport uses a graphical user interface to make creating your report as easy as possible. Run the ethicalReport_GUI.py file to access the GUI.
2. Use the navigation bar at the bottom of the GUI window to navigate between the different pages of the report form.
3. Follow the prompts on the screen to fill out all the relevant information.
4. On the final page, record the Report ID that EthicalReport generates for you. This ID records the date of the report when filed and a unique ID for your individual report.

---
## Citations

Python Datetime Docs - for using datetime
https://docs.python.org/3/library/datetime.html

The Tkinter Docs - Overall Functionality
https://docs.python.org/3/library/tkinter.html

Themed Tk Widges Docs - Understanding Themed Tkinter Widgets
https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk

A StackOverflow comment made by Bryan Oakley - for the idea of stacking frames and switching between them using tk.raise()
https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

