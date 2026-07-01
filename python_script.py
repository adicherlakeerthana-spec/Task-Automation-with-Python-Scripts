# CodeAlpha Python Internship
# Task 3: Email Extractor

import re

print("=" * 50)
print("        EMAIL EXTRACTOR")
print("=" * 50)

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

try:
    # Read the input file
    with open(input_file, "r") as file:
        text = file.read()

    # Extract email addresses using regular expression
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

    # Remove duplicate email addresses
    unique_emails = list(set(emails))

    # Save email addresses to a new file
    with open(output_file, "w") as file:
        if unique_emails:
            for email in sorted(unique_emails):
                file.write(email + "\n")
        else:
            file.write("No email addresses found.")

    print(f"\nTotal Email Addresses Found: {len(unique_emails)}")

    if unique_emails:
        print("\nExtracted Email Addresses:")
        for email in sorted(unique_emails):
            print(email)

    print(f"\nResults saved successfully in '{output_file}'")

except FileNotFoundError:
    print(f"\nError: '{input_file}' not found.")
    print("Create a file named 'input.txt' in the same folder as this program.")