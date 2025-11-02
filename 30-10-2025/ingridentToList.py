import csv

input_file = "cleaned_output.csv"
output_file = "unique_ids.csv"

# Step 1: Read all IDs from input file
unique_ids = set() # set to collect unick element

with open(input_file, "r", newline="") as infile:
    reader = csv.reader(infile)
    for row in reader:
        if not row:
            continue
        # Remove brackets and spaces
        cleaned = row[0].replace("[", "").replace("]", "").replace(" ", "")
        # Split into individual IDs
        ids = cleaned.split(",") 
        # Add each to set (automatically removes duplicates)
        unique_ids.update(ids)

# Step 2: Write unique IDs to CSV file
with open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Unique_IDs"])
    for uid in sorted(unique_ids):  # sorted for nice order
        writer.writerow([uid])

print(f" Done! {len(unique_ids)} unique IDs written to '{output_file}'")
