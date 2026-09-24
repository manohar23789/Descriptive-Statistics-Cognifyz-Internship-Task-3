import pandas as pd

# STEP 1: Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# STEP 2: Display all column names
print("Columns in Dataset:")
print(df.columns.tolist())

# STEP 3: Identify numerical columns
# Convert columns that contain numeric values
# into numeric data types where possible
numeric_df = df.apply(
    lambda column: pd.to_numeric(column, errors="coerce")
)

# Keep only columns that contain at least
# one numeric value
numeric_columns = numeric_df.select_dtypes(
    include="number"
).columns


print("\nNumerical Columns:")
print(numeric_columns.tolist())


# STEP 4: Calculate Mean
mean_values = numeric_df[numeric_columns].mean()

print("\nMean:")
print(mean_values)

# STEP 5: Calculate Median
median_values = numeric_df[numeric_columns].median()

print("\nMedian:")
print(median_values)

# STEP 6: Calculate Standard Deviation
std_values = numeric_df[numeric_columns].std()

print("\nStandard Deviation:")
print(std_values)

# STEP 7: Create a summary table
summary = pd.DataFrame({
    "Column": numeric_columns,
    "Mean": mean_values.values,
    "Median": median_values.values,
    "Standard Deviation": std_values.values
})

print("\n============================================")
print("DESCRIPTIVE STATISTICS")
print("============================================")

print(summary.to_string(index=False))