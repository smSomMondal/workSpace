import json
import csv

# Step 1: Read JSON data from file
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# Step 2: Prepare data for CSV
rows = []
for partner in data:
    partner_id = partner.get("partnerID", "")
    domain_ids = list({domain.get("id", "") for domain in partner.get("domains", [])})

    # Format as list-like string e.g. ["D458, D636, D020"]
    formatted_domain_list = [", ".join(domain_ids)]

    rows.append({
        "partnerID": partner_id,
        "domainIDs": json.dumps(formatted_domain_list)  # ensures proper brackets and quotes
    })

# Step 3: Write to CSV
with open("partner_domains.csv", "w", newline="") as csv_file:
    fieldnames = ["partnerID", "domainIDs"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print(" Data successfully saved to partner_domains.csv")
