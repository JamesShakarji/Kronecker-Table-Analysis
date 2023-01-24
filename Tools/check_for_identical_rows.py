import csv

# Open the CSV file
with open('some_csv_of_kronekervalues_from_/data', 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Skip the first row
    next(reader)

    # Initialize a list to store the rows
    rows = []

    # Iterate through the rows in the CSV file
    for row in reader:
        # Skip the first column
        rows.append(row[1:])

# Check for identical rows
identical_rows_found = False
for i in range(len(rows)):
    for j in range(i + 1, len(rows)):
        if rows[i] == rows[j]:
            print(f"Identical rows found at index {i + 1} and {j + 1}")
            identical_rows_found = True

if not identical_rows_found:
    print("There are no identical rows")
