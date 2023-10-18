import folium

# Create a base map
m = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=5)

# Add points to the map
for idx, row in df.iterrows():
    if row['latitude'] and row['longitude']:
        folium.Marker([row['latitude'], row['longitude']], popup=row['church_name']).add_to(m)

# Save it to an HTML file
m.save('interactive_map.html')
