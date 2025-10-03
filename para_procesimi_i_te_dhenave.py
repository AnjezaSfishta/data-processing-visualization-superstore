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

