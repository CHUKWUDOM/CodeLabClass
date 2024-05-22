from constraints import *

def read_excel(file_path, sheet_names):
    for sheet_name in sheet_names:
    sheets_data[sheet_name] = pd.read_excel(file_path, sheet_name=sheet_name)
    return sheets_data

def generate_emails(names):
    emails = []
    for sheet_name, SHEET in sheets_data.items():

    for name in names:
        # Split student name into first name and last name
        parts = name.split()
        first_name = parts[0]
        last_name = parts[-1] if len(parts) > 1 else ""
        # Remove special characters such as ' from last name using regular expressions
        last_name = re.sub(r'[^a-zA-Z]', '', last_name)
        # Generate email address
        email = f"{first_name[0]}{last_name}@gmail.com".lower()
        emails.append(email)
    return emails

def generate_special_char_names(names):
    # Regular expression pattern to find special characters
    special_char_pattern = re.compile(r"[^\w\s]", re.UNICODE)
    # Extract the column named 'Student Name' and find names with special characters
    names_with_special_chars = df[df['Student Name'].str.contains(special_char_pattern, na=False)]
    return names_with_special_chars['Student Name'].tolist()


def save_to_csv(data, filename):
    """Save a list of tuples to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write data rows
        writer.writerows(data)


def save_to_tsv(data, filename):
    """Save data to a TSV file."""
    pd.DataFrame(data).to_csv(filename, sep='\t', index=False, header=False)

c