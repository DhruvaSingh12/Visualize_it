import pandas as pd
import os

df = pd.read_csv('County_Health_Rankings.csv')  

grouped = df.groupby(['measure_id', 'measure_name'])

output_dir = 'output_csv_files'
os.makedirs(output_dir, exist_ok=True)

for (measure_id, measure_name), group in grouped:
    valid_filename = "".join(c if c.isalnum() or c in " _-" else "_" for c in measure_name)
    file_name = f"{valid_filename}.csv"
    file_path = os.path.join(output_dir, file_name)

    group.to_csv(file_path, index=False)

    print(f"File created: {file_path}")
