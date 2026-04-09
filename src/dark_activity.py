def detect_dark_activity(df, hours=2):
    """
    Detect ships that have turned off AIS signals for more than 'hours'.
    Adds 'dark_activity' column: True = suspicious
    """
    df['time_diff'] = df.groupby('vessel_id')['timestamp'].diff()
    df['dark_activity'] = df['time_diff'] > pd.Timedelta(hours=hours)
    return df
