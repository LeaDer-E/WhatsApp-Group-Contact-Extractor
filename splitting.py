import re
from openpyxl import Workbook
from datetime import datetime

# Read the content of "unsorted.txt"
with open("unsorted.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Use regex to extract all phone numbers (strings starting with '+' and containing digits, spaces, or dashes)
pattern = r'\+\d[\d\s-]*\d'
phone_numbers = re.findall(pattern, content)

# Clean the numbers (remove extra whitespace)
phone_numbers = [num.strip() for num in phone_numbers]

print(f"Extracted {len(phone_numbers)} phone numbers.")

# Create a new Excel workbook and select the active worksheet
wb = Workbook()
ws = wb.active
ws.title = "Phone Numbers"

# Write each phone number into a separate cell in column A (starting at A1)
for idx, number in enumerate(phone_numbers, start=1):
    ws.cell(row=idx, column=1, value=number)

# Create a filename with the current date and time
now = datetime.now()
file_name = now.strftime("Numbers%Y%m%d_%H%M%S.xlsx")

# Save the workbook
wb.save(file_name)
print(f"File '{file_name}' created successfully.")

