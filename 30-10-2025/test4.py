import csv
import ast

input_file = "outputRandom.csv"          # your original CSV
output_file = "randomDiatary.csv"  # cleaned version

rows = []

# Step 1: Read and clean each row
with open(input_file, "r", newline="") as infile:
    reader = csv.reader(infile)
    for row in reader:
        if not row:
            continue
        # Each row is a string like "['i123', 'i456', ...]"
        try:
            cleaned = row[0].replace("'", "").replace('"', "")
            rows.append([cleaned])
        except Exception as e:
            print("Skipping invalid row:", row, "| Error:", e)

# Step 2: Write cleaned data to a new CSV
with open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print(f" Done! {len(rows)} rows written to '{output_file}'")
