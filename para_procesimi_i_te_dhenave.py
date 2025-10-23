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

# 5. Kontrolli i vlerave të zbrazëta
print("\nVlerat e zbrazëta:")
print(df.isnull().sum())

# 6. Trajtimi i vlerave të zbrazëta
# Postal Code - mbushe sipas qytetit
df['Postal Code'] = df.groupby('City', observed=True)['Postal Code'].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else np.nan))

# Nëse akoma ka NaN, mbush me median
df['Postal Code'] = df['Postal Code'].fillna(df['Postal Code'].median())

# Datat – mbush me median
df['Order Date'] = df['Order Date'].fillna(df['Order Date'].median())
df['Ship Date'] = df['Ship Date'].fillna(df['Ship Date'].median())

print("\nPas trajtimit të vlerave të zbrazëta:")
print(df.isnull().sum())

# 7. Duplikatet
print("\nNumri i rreshtave të duplikuar:", df.duplicated().sum())
df = df.drop_duplicates()

df_cleaned_no_outliers = df.copy()
df_cleaned_no_outliers.to_csv("cleaned_data_without_outliers.csv", index=False)
print("✅ Dataset i pastruar (pa outliers) ruhet si 'cleaned_data_without_outliers.csv'")