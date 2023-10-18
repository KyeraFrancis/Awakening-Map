import pandas as pd
from faker import Faker
import random

# Create a Faker generator
fake = Faker()

# Define the number of entries you want in your CSV
num_entries = 100

# Lists of dummy church names and cities for variability
church_names = [f"Assembly of {fake.word()}" for _ in range(20)]
cities_states = [fake.city() + ", " + fake.state() for _ in range(20)]

# Generating the data
data = {
    "church_name": [random.choice(church_names) for _ in range(num_entries)],
    "location": [random.choice(cities_states) for _ in range(num_entries)],
    "address": [fake.street_address() for _ in range(num_entries)],
    "pastor": [fake.name() for _ in range(num_entries)],
    "phone": [fake.phone_number() for _ in range(num_entries)],
    
}

# Create a DataFrame
df = pd.DataFrame(data)

# Specify the relative path to your CSV. Modify this path to match your project's directory structure.
path_to_csv = 'data/raw/assembly_info.csv'  # Make sure this path is correct for your project!

# Save the DataFrame to your existing CSV file
df.to_csv(path_to_csv, index=False)

print(f"Dummy data written to {path_to_csv} with {num_entries} entries.")