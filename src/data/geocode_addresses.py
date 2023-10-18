import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Load your data
path_to_csv = '/Users/kyerafrancis/Desktop/Data Science/awakening-map/data/raw/assembly_info.csv'  # Adjust path as necessary
df = pd.read_csv(path_to_csv)

# Set up Nominatim Geocoder
geolocator = Nominatim(user_agent="myGeocoder", timeout=10)  # replace "myGeocoder" with a suitable user-agent for your app

# RateLimiter to avoid overloading Nominatim's server
geocode_with_delay = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Define a function that applies geocoding
def get_location_by_address(address):
    try:
        location = geocode_with_delay(address)
        if location:
            return pd.Series({'Latitude': location.latitude, 'Longitude': location.longitude, 'Address': location.address})
    except Exception as e:
        print(f"Error: {e}")
    return None  # Return None if no coordinates are found

# Apply the function to the "address" column
df[['Latitude', 'Longitude', 'Address']] = df['address'].apply(lambda addr: get_location_by_address(addr) if pd.notna(addr) else None)

# Save the data with coordinates into a new CSV file
df.to_csv('/Users/kyerafrancis/Desktop/Data Science/awakening-map/data/processed/assembly_with_coordinates.csv', index=False)  # Adjust path as necessary
