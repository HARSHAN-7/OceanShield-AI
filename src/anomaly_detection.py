from sklearn.ensemble import IsolationForest

def detect_anomalies(df, contamination=0.05):
    """
    Detect suspicious vessels using Isolation Forest.
    Adds 'anomaly' column: -1 = suspicious, 1 = normal
    """
    features = df[['latitude', 'longitude', 'speed']]
    model = IsolationForest(contamination=contamination, random_state=42)
    df['anomaly'] = model.fit_predict(features)
    return df
