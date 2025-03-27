import pandas as pd

def delete_empty(f_csv):
    df = pd.read_csv(f_csv)
    df_new = df.dropna()
    return df_new

f = 'flights_NY.csv'
ans_df = delete_empty(f)

if ans_df is not None:
  ans_df.to_csv('flights_new.csv', index=False)

  
