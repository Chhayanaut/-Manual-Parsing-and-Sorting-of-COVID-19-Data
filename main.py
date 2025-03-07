# Open and read the file line by line
with open("country_wise_latest.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()


header_line = lines[0].strip()
headers = header_line.split(",")

print("Headers:", headers)

data = []
for line in lines[1:]:

    row = line.strip()
    if not row:
        continue
    values = row.split(",")
    if len(values) != len(headers):
        continue
    row_dict = dict(zip(headers, values))
    data.append(row_dict)

# Display the first 5 dictionaries to verify
print("First 5 rows of parsed data:")
for row in data[:5]:
    print(row)


sorted_data = sorted(data, key=lambda x: int(x["Confirmed"]), reverse=True)

# Display the first 5 rows of the sorted data to verify
print("\nTop 5 rows after sorting by Confirmed cases:")
for row in sorted_data[:5]:
    print(row)

# Write the sorted data back to a new CSV file.
output_filename = "sorted_country_wise_latest.csv"
with open(output_filename, "w", encoding="utf-8") as file:

    file.write(",".join(headers) + "\n")
    for row_dict in sorted_data:
        row_values = [row_dict[header] for header in headers]
        file.write(",".join(row_values) + "\n")

print(f"\nSorted data has been saved to {output_filename}")
