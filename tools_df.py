import pandas as pd

def expand_column(df, col):
    expanded = df[col].dropna().apply(pd.Series).add_prefix(f'{col}_')
    df = df.drop(columns=[col])
    df = df.join(expanded)
    return df
