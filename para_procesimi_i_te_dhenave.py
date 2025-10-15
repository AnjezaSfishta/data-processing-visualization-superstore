import pandas as pd

# 1. Leximi i datasetit
df = pd.read_csv("superstore.csv")

print("Shape i datasetit:", df.shape)

# 2. Shfaq disa rreshta fillestare
print("\nDisa rreshta nga dataset-i:")
print(df.head())

# 3. Shfaq tipet fillestare
print("\nTipat e kolonave fillestare:")
print(df.dtypes)

# 4. Konvertimi i tipeve të dhënave
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Konvertimi i disa kolonave kategorike
cat_cols = ['Ship Mode', 'Segment', 'Country', 'City', 'State', 'Region', 'Category', 'Sub-Category']
for col in cat_cols:
    df[col] = df[col].astype('category')

print("\nPas konvertimit:")
print(df.dtypes)