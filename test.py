import crimedatasets as crd

# List all available datasets

datasets = crd.list_datasets()
print(datasets)

# Load a specific dataset

df = crd.load_dataset('us_mass_shootings')
print(df.head())