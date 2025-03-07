# -Manual-Parsing-and-Sorting-of-COVID-19-Data
Objective
The purpose of this task is to help you understand how to manually parse and process CSV files without using libraries like csv. You will work with real-world COVID-19 data and learn how to manipulate text files, convert data into intermediate structures, and sort it based on specific criteria.

Instructions
Download the File:

Download the file country_wise_latest.csv from the Corona Virus Report Dataset.
This file contains country-wise data on COVID-19-https://www.kaggle.com/datasets/imdevskp/corona-virus-report, such as confirmed cases, deaths, recoveries, and more.
Load the File:

Open the file and read its contents line by line.
Separate the headers (the first line) from the rows (the data).
Parse the Data Manually:

Split each row by commas to extract individual data points. For example:
row = "Afghanistan,36263,1269,25198,9796,106,10,18,3.5,69.49,5.04,35526,737,2.07,Eastern Mediterranean"
values = row.split(",")
Convert the rows into a list of dictionaries, where:
The keys come from the header row.
The values are the corresponding elements from each data row.
Example structure:
[
    {"Country/Region": "Afghanistan", "Confirmed": "36263", "Deaths": "1269", ...},
    {"Country/Region": "Albania", "Confirmed": "4880", "Deaths": "144", ...},
    ...
]
Sort the Data:
Use Python’s sorted() function to sort the list of dictionaries by the “Confirmed” column in descending order.
Convert the “Confirmed” column values to integers before sorting.
Example of using sorted():
sorted_data = sorted(data, key=lambda x: int(x['Confirmed']), reverse=True)
Save the Data:

Write the sorted data back into a new CSV file.
Ensure the new file has the same format as the original, with the header as the first line.
Document the Process:

Use a Jupyter Notebook to:
Explain each step in Markdown cells.
Include the code for each part of the task in code cells.
Display intermediate outputs to demonstrate your work (e.g., print the first 5 rows of the sorted data).
Sample Workflow in Jupyter Notebook
Step 1: Open the file and read it line by line.
Step 2: Split the header and rows.
Step 3: Parse the rows into a list of dictionaries.
Step 4: Sort the data by “Confirmed” cases.
Step 5: Save the sorted data back to a file.
Example Data (Preview)
Here’s how the data looks:

Country/Region  Confirmed  Deaths  Recovered  Active  New cases  …
Afghanistan     36263      1269    25198      9796    106        …
Albania         4880       144     2745       1991    117        …
Algeria         27973      1163    18837      7973    616        …
After sorting by “Confirmed” in descending order, it might look like this:

Country/Region  Confirmed  Deaths  Recovered  Active  New cases  …
Algeria         27973      1163    18837      7973    616        …
Afghanistan     36263      1269    25198      9796    106        …
Albania         4880       144     2745       1991    117        …
