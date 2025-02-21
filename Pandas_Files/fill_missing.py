import pandas as pd

df = pd.read_csv("updated_file.csv") 

missing_before = df['rate'].isnull().sum()
print(f"Missing values before filling: {missing_before}")

df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

mean_value = round(df['rate'].mean())

df['rate'].fillna(mean_value, inplace=True)

missing_after = df['rate'].isnull().sum()
print(f"Missing values after filling: {missing_after}")

df.to_csv("cleaned_file.csv", index=False)  
