import pandas as pd

# Load the full MedQuAD dataset
df = pd.read_csv("medquad.csv")  # Replace with your actual filename

# Sample 100 rows (without replacement)
test_df = df[:100].copy()


# Save to new test file
test_df.to_csv("first100.csv", index=False)

print("✅ Created test_medquad_100.csv with 100 rows.")
