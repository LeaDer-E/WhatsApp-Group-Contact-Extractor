# WhatsApp Group Contact Extractor

This repository contains Python scripts designed to extract phone numbers and contact names from WhatsApp Web groups. The tool helps automate the process of retrieving data from copied HTML elements (via Inspect Element) and organizing them into Excel files for easy analysis and processing.

## Features

- **Extract Phone Numbers via `splitting.py`:**  
  Reads HTML snippets (e.g., from unsorted.txt) containing WhatsApp group data and extracts phone numbers. Each phone number is placed in its own cell in an Excel file with a timestamped filename.

- **Merge Excel Files via `merging.py`:**  
  Combines multiple Excel files that contain extracted phone numbers into one consolidated Excel file. Duplicate entries are removed to ensure only unique numbers remain.

- **Extract Group Contact Names:**  
  Optionally, extract group contact names from HTML elements, even if some contacts only show a phone number.

## Prerequisites

- **Python 3.x**
- **Required Libraries:**  
  - [openpyxl](https://openpyxl.readthedocs.io/)  
  - [pandas](https://pandas.pydata.org/)

You can install the required packages using the provided requirements file.

### Using requirements.txt

Ther's a file named `requirements.txt` with the following content:

```
openpyxl==3.1.2
pandas==1.5.3
```

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Project Structure

- **splitting.py:**  
  Extracts phone numbers from an input HTML file (`unsorted.txt`) and writes them into a timestamped Excel file (e.g., `Numbers20250330_041126.xlsx`).

- **merging.py:**  
  Merges multiple Excel files (e.g., those starting with `Numbers20250330_`) by reading their first column, removing duplicates, and creating a single consolidated Excel file with a unique, timestamped filename.

- **README.md:**  
  This documentation file.

- **requirements.txt / requirements.py:**  
  Files listing project dependencies.

## Usage

### Extracting Phone Numbers

1. **Prepare Input File:**  
   Copy the HTML element from WhatsApp Web (using Inspect Element) and save it into a file named `unsorted.txt`. For example, your HTML might look like:

   ```html
   <span title="+20 10 10101010, +20 12 12121212, ... , and 389 more" class="...">
   </span>
   ```

2. **Run the Extraction Script:**  
   Execute the script to extract phone numbers and create an Excel file:

   ```bash
   python split_numbers.py
   ```

   The script will output the number of phone numbers extracted and save the Excel file with a filename like `NumbersYYYYMMDD_HHMMSS.xlsx`.

### Merging Multiple Excel Files

If you have multiple Excel files generated from different runs of the extraction script and want to merge them into one file:

1. **Place all Excel Files:**  
   Ensure that all Excel files (e.g., `Numbers20250330_*.xlsx`) are in the same directory.

2. **Run the Merge Script:**  
   Execute the merge script:

   ```bash
   python merge_numbers.py
   ```

   This script will combine the numbers from each file, remove duplicates, and create a new file named something like `MergedNumbers_YYYYMMDD_HHMMSS.xlsx`.

### Extracting Group Contact Names

If your WhatsApp group shows contact names (or a mix of names and numbers) in an element like:

```html
<div class="x78zum5 x1cy8zhl xisnujt x1nxh6w3 xcgms0a x16cd2qt">
  <span title="Dreamnet, Edaraah, You" class="...">Dreamnet, Edaraah, You</span>
</div>
```

You can modify the extraction code to target the `title` attribute of the `<span>` element. Adjust the CSS selector as needed.

## Customization

Feel free to modify the regular expressions or file paths in the scripts to suit your extraction needs. For instance, you may update the regex pattern to better match the phone number format used in your WhatsApp group data.

## License

This project is licensed under the MIT License.

## Contributing

Contributions, bug reports, and suggestions are welcome! Please open an issue or submit a pull request on GitHub.

## Acknowledgements

- [openpyxl](https://openpyxl.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)
- WhatsApp Web for the data source inspiration

