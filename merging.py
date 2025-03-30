import pandas as pd
import glob
from datetime import datetime

# Find all Excel files starting with "Numbers20250330_"
excel_files = glob.glob("Numbers20250330_*.xlsx")
print(f"Found {len(excel_files)} files.")

all_numbers = []

# Read the first column (assumed to contain the phone numbers) from each file
for file in excel_files:
    try:
        # Read the file without a header, so that column A is index 0
        df = pd.read_excel(file, header=None)
        # Drop any empty values
        df = df.dropna()
        numbers = df[0].astype(str).tolist()
        all_numbers.extend(numbers)
        print(f"Read {len(numbers)} numbers from file: {file}")
    except Exception as e:
        print(f"Error reading file {file}: {e}")

# Remove duplicate numbers
unique_numbers = list(set(all_numbers))
unique_numbers.sort()  # Optional: sort the numbers

print(f"Total unique numbers: {len(unique_numbers)}")

# Create a new DataFrame with the unique numbers (each number in a separate row)
df_out = pd.DataFrame(unique_numbers)

# Create an output filename with the current date and time
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"MergedNumbers_{timestamp}.xlsx"

# Save the DataFrame to an Excel file without a header or index
df_out.to_excel(output_file, index=False, header=False)

print(f"File '{output_file}' created successfully with {len(unique_numbers)} unique numbers.")
