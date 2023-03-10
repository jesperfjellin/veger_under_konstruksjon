import csv

# Open the two CSV files
with open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_json_lastmonth.csv', 'r', newline='', encoding='utf-8-sig') as f1, \
     open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_json.csv', 'r', newline='', encoding='utf-8-sig') as f2, \
     open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/new_geometry.csv', 'w', newline='', encoding='utf-8-sig') as fout:

    # Create CSV readers for the two input files
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)

    # Create a CSV writer for the output file
    writer = csv.writer(fout)

    # Read the rows from the input files
    rows1 = [row for row in reader1]
    rows2 = [row for row in reader2]

    # Find the rows in rows2 that are not present in rows1
    not_present = [row for row in rows2 if row not in rows1]
    if len(not_present) == 0:
        print("No new lines found!")
    # Write the rows to the output file
    for row in not_present:
        writer.writerow(row)
