import pandas as pd

df = pd.read_csv('cleaned_diabetic_screening.csv')  
df['rate'] = (df['numerator']/df['denomenator'] * 100).round()

df.to_csv('updated_file.csv', index=False)

print(df.head())
