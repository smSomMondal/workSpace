import csv
import re

# Example input list (replace this with reading from file if needed)
domain_data = [
    "[D935, D448, D632, D233]",
    "[D629, D070, D195, D956, D867, D808, D063, D054, D563, D654, D413]",
    "[D055, D056]",
    "[D057, D058, D321]",
    "[D059, D459, D060, D104]",
    "[D755, D353]",
    "[D636, D020, D458]",
    "[]",
    "[D250]",
    "[D407]",
    "[D167]",
    "[D524]"
]

def parse_entry(entry: str):
    """
    Parse a string that represents a list of domains.
    Accepts formats like:
      - [a, b, c]
      - "['a','b']"
      - '["a","b"]'
      - []
    Returns a list of domain strings (may be empty).
    """
    if entry is None:
        return []
    s = entry.strip()
    # remove outer quotes if the whole string is quoted
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1].strip()

    # ensure it starts with [ and ends with ]
    if s.startswith('[') and s.endswith(']'):
        inner = s[1:-1].strip()
    else:
        inner = s

    if not inner:
        return []

    # If items are properly quoted (e.g. "a","b" or 'a','b'), split respecting quotes
    # Otherwise split on commas
    # We'll use a regex to capture quoted strings or plain tokens
    pattern = r"""
        (?:
          "([^"]+)"      # double-quoted content group1
        |
          '([^']+)'      # single-quoted content group2
        |
          ([^,]+)        # unquoted token group3 (anything up to comma)
        )
    """
    tokens = re.findall(pattern, inner, flags=re.VERBOSE)
    results = []
    for g1, g2, g3 in tokens:
        token = g1 or g2 or g3
        if token is None:
            continue
        token = token.strip()
        # ignore empty tokens
        if token:
            results.append(token)
    return results

# collect unique domains
unique_domains = set()
for entry in domain_data:
    parsed = parse_entry(entry)
    for d in parsed:
        unique_domains.add(d)

# write to CSV (one domain per row)
output_csv = "unique_domains.csv"
with open(output_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["domain_name"])
    for domain in sorted(unique_domains):
        writer.writerow([domain])

print(f" Saved {len(unique_domains)} unique domains to: {output_csv}")
