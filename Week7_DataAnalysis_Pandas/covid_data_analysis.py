import pandas as pd

# Load COVID CSV data
df = pd.read_csv("covid_data.csv")

# Preview data
print(df.head())

# Summary statistics
print(df.describe())

# Group by country and get total cases
country_cases = df.groupby("Country")["Cases"].sum()
print(country_cases)
