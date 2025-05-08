import pandas as pd

# Correcting the file path using raw string (r"") or double backslashes (\\)
csv_path = r"C:\Users\Admin\Downloads\FASDH25\python_exercises\lesson_13.1\data\title.csv"

# Reading the CSV file
df = pd.read_csv(csv_path)

# Printing column names
print(df.columns)

# Step 4: Print the title of the longest article
# Since we already have a 'length' column, use it
longest_index = df['length'].idxmax()
print("Longest title is:")
print(df.loc[longest_index, 'title'])

# Step 5: Print sum of all article lengths
total_length = df['length'].sum()
print("Total length of all titles:", total_length)

# Step 6: Export top 20 longest articles
top20_df = df.sort_values(by='length', ascending=False).head(20)
output_path_top20 = r"C:\Users\Admin\Downloads\FASDH25\python_exercises\lesson_13.1\outputs\Zeeshan-Karim-top20.csv"
top20_df.to_csv(output_path_top20, index=False)

# Step 7: Combine year, month, and day into a new column (as yyyy{yy}-{mm}-{dd})
# Ensure all date parts are strings
df['year'] = df['year'].astype(str)
df['month'] = df['month'].astype(str).str.zfill(2)  # Ensure 2 digits
df['day'] = df['day'].astype(str).str.zfill(2)

# Step 8: Export articles from first 6 months of 2023
mask = (df['year'] == '2023') & (df['month'].astype(int) <= 6)
first6m_df = df[mask]

output_path_6m2023 = r"C:\Users\Admin\Downloads\FASDH25\python_exercises\lesson_13.1\outputs\Zeeshan-Karim-6m2023.csv"
first6m_df.to_csv(output_path_6m2023, index=False)

print("Articles from Jan to Jun 2023 saved to:")
print(output_path_6m2023)

