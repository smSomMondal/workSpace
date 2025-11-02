import csv
import random

# Step 1: Your data array
data = [
    ["P001D101R172", "P001D101R179", "P001D101R153"],
    ["P001D102R197", "P001D102R168", "P001D102R177"],
    ["P001D103R158", "P001D103R179", "P001D103R161"],
    # ... (add your full dataset here)
]

# Step 2: Function to generate unique IDs
def generate_unique_id():
    new_id = "i" + str(random.randint(10000, 99999))
    return new_id

# Step 3: Flatten data and assign IDs
unique_ids = set()
id_array = []
rows = []
for _ in range(791):  # total rows needed
    id_array = []  # fresh list for each row
    for _ in range(random.randint(4, 8)):  # 5 elements per row
        random_id = generate_unique_id()
        id_array.append(random_id)
    rows.append([id_array]) # Add a new row to the rows list, where that row contains id_array as a single column

# Step 4: Write to CSV
with open("output_with_ids.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # writer.writerow(["ID", "Code"])  # header
    writer.writerows(rows)

print(f" Done! {len(rows)} records written to 'output_with_ids.csv'")
