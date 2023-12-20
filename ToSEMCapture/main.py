from datetime import datetime
from openpyxl import Workbook
from pathlib import Path

#import Sub Procs
from Email_Proc import Send_Email
from ToS_Proc import Tos_EM_Capture

#Declare Global Variables
global recipients_email
global Email_Message

#Initilize Global Variables
recipients_email = ["cesenthil@gmail.com,sud.sarkar@gmail.com"]

print("Main: Process Started: " + datetime.now().strftime("%m-%d-%Y, %H:%M:%S")) #Start Time

Email_Subject = "SPX | 1 DTE | ToS EM @ " + datetime.now().strftime("%d-%b-%Y")
Email_Message = Tos_EM_Capture()

Send_Email(recipients_email,Email_Subject,Email_Message)

print("Main: Process Completed: " + datetime.now().strftime("%mmm-%d-%Y, %H:%M:%S"))  #End Time

