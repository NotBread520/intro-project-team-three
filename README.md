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


## Configuration, Installation, and Execution
[ Windows ]
EthicalReport has not been packaged as an executable. To run this software, follow these instructions:
1. Download all of the .py files from the EthicalReport repository to your local computer.
2. Install Python 3.13 or later. You can do this using the following command:
   
```
winget install -e --id Python.Python.3.13
```

3. With Python installed, navigate to the folder containing ethicalReport_GUI.py, open a Terminal prompt there, and use the following command: 

```
python ethicalReport_GUI.py
```

---

## App Screenshots
[Ethical Report GUI Screenshots](https://drive.google.com/file/d/1F0BnH4kxwmBBqj2QcPUNS0KGVRWDc9_8/view?usp=sharing)

## File Breakdown

| File Name               | Description                                                                                                                                         | Contributors            |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |-------------------------|
| ethicalReport_GUI.py    | primary logic and code for the GUI. Execute this file to run the app and create your report file.                                                   | Luc, Jacob,             |
| data_stored.py          | contains a python dictionary that stores information from the GUI at runtime so that the report can be generated from a defined dictionary of keys. | Jacob                   |
| report_generator.py     | logic and formatting for compiling and saving the markdown document, our final output.                                                              | Xander                  |
| ER_2026-03-15_SAMPLE.md | sample report generated using EthicalReport's GUI.                                                                                                  |                         |

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

Python dictionaries are easy 📙 - for reviewing how to save data to a dictionary
https://youtu.be/MZZSMaEAC2g?si=K_Mn3N6jd5VC_ea9

Python Tkinter Tutorial #07 | How to create a CHECKBUTTON using TKINTER - for learning how to use a check button
https://youtu.be/coDWIWqrupg?si=gFlyxyvH_PZHcjaA

How to Easily Transfer Data Between Python Files: Importing Variables Explained - for learning how to save data between .py files
https://youtu.be/BI58Vu1Wb2k?si=UYYNl5KIJGn-yv91
