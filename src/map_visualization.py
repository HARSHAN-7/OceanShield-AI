import folium

def create_map(df, map_file='OceanShield_Map.html'):
    
    map_center = [df['latitude'].mean(), df['longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=5)
    
    for _, row in df.iterrows():
        color = 'red' if row['anomaly'] == -1 or row['dark_activity'] else 'blue'
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=3,
            color=color,
            fill=True
        ).add_to(m)
    
    # Save map to HTML
    m.save(map_file)
    print(f"Map saved as {map_file}")
    return m
