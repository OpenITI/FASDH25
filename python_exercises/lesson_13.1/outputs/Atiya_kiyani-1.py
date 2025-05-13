import pandas as pd
data = {
    'Name': ['Ali', 'Sara', 'John', 'Fatima'],
    'Age': [25, 30, 22, 28],
    'City': ['Karachi', 'Lahore', 'Islamabad', 'Quetta']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
older_than_25 = df[df['Age'] > 25]
print("\nPeople older than 25:")
print(older_than_25)
