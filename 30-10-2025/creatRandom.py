import csv
import random

# Step 1: Read data from CSV file
input_file = "input.csv"  # 🔹 your CSV file name
data = []

with open(input_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        # Assuming each row has one column (e.g. "i10007")
        if row:  # skip empty lines
            data.append(row[0])

# Step 2: Randomly select N elements
N = 2  # number of random IDs you want
random_selection = random.sample(data, N)  # ensures no duplicates
rows=[]
for _ in range(763):  # total rows needed
    random_selection = random.sample(data, random.randint(2,8))
    rows.append([random_selection])


with open("outputRandom.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # writer.writerow(["ID", "Code"])  # header
    writer.writerows(rows)
# Step 3: Make an array (list)
selected_array = random_selection

print("Selected IDs:", selected_array)
