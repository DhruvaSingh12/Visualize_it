import pandas as pd

df = pd.read_csv("Violent_crime.csv")

def expand_years(year_span):
    if pd.isna(year_span) or str(year_span).strip() == "":
        return []
    
    year_span = str(year_span).strip() 

    if '-' in year_span: 
        try:
            start, end = map(int, year_span.split('-'))
            return list(range(start, end + 1))
        except ValueError:
            return [] 
    else:
        try:
            return [int(year_span)]
        except ValueError:
            return [] 

df['expanded_years'] = df['year_span'].apply(expand_years)

df_expanded = df.explode('expanded_years')

df_expanded = df_expanded.dropna(subset=['expanded_years'])

df_expanded['expanded_years'] = df_expanded['expanded_years'].astype(int)
df_expanded.drop(columns=['year_span'], inplace=True)

df_avg = df_expanded.groupby(['state', 'county'], as_index=False).agg({
    'raw_value': lambda x: round(x.mean(), 2) 
})

columns_to_keep = [col for col in df_expanded.columns if col not in ['expanded_years', 'raw_value']]
df_final = df_expanded[columns_to_keep].drop_duplicates().merge(df_avg, on=['state', 'county'], how='left')

df_final.to_csv("violent.csv", index=False)

print(df_final.head())
