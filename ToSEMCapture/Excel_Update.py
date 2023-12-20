from openpyxl import Workbook
from pathlib import Path

workbook = Workbook()
workbook.active['A1'] = Email_Message
workbook.save(Path.home() / "Desktop" / "email_messages.xlsx")