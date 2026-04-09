
import pandas as pd

def load_and_clean(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(['vessel_id', 'timestamp'])
  return df
