import pandas as pd
# import logging
import re
from functions import *
from constraints import *
# from time import time

"""
INPUT_FILE_PATH='input_data files'
OUTPUT_FILE_PATH='output_data files'
"""

def main():
    # Read the Excel sheets and save sheets as log files
    df = read_excel(EXCEL_FILE, SHEET_NAMES)

    # Generate emails from the extracted names
    emails = generate_emails(combined_df)
    SHEET["Email Address"] = SHEET["Student Name"].apply(generate_email)

    # List names with special characters
    names_with_special_chars = list_names_with_special_characters(EXCEL_FILE)
    
    #Save to csv
    save_to_csv(emails, CSV_EMAIL)
    save_to_csv([names_with_special_chars], CSV_SPECIAL_NAMES)

if __name__ == "__main__":
    main()
