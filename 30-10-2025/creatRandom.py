import csv
import random

# Step 1: Read data from CSV file
input_file = "input.csv"  # 🔹 your CSV file name
data = []  # list to add dat

with open(input_file, "r") as f: # open file
    reader = csv.reader(f) # read file
    for row in reader: # for each row in data line
        # Assuming each row has one column (e.g. "i10007")
        if row:  # skip empty lines
            data.append(row[0]) # add to data

# Step 2: Randomly select N elements
N = 2  # number of random IDs you want
random_selection = random.sample(data, N)  # ensures no duplicates with out no replecement


rows=[] # list to create csv
for _ in range(763):  # total rows needed
    random_selection = random.sample(data, random.randint(2,8)) # collect the sample and the range between 2 to 8
    rows.append([random_selection]) # add to row


with open("outputRandom.csv", "w", newline="") as f:
    writer = csv.writer(f) # make the point to wrie
    # writer.writerow(["ID", "Code"])  # header
    writer.writerows(rows) # write to page
    
"""
# Step 3: Make an array (list)
selected_array = random_selection

print("Selected IDs:", selected_array)

"""