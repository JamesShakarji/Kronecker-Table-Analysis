import csv

# Open the input CSV file
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

# Open the output CSV file
with open('some_training_set.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the rows to the CSV file
    writer.writerows(rows)
