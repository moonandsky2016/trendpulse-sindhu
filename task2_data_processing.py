import pandas as pd
import os

# Step 1 — Load JSON file
# ---------------------------------------
# Assuming the file from Task 1 exists in data/ folder
# You can change filename if needed

file_path = "data/trends_20260409.json"

try:
    df = pd.read_json(file_path)
    print(f"Loaded {len(df)} stories from {file_path}")
except Exception as e:
    print("Error loading file:", e)
    df = pd.DataFrame()

# Step 2 — Clean the Data
# ---------------------------------------

# 1. Remove duplicates based on post_id
before = len(df)
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# 2. Remove rows with missing critical fields
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# 3. Fix data types (convert to integers)
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce").fillna(0).astype(int)

# 4. Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# 5. Clean whitespace in title
df["title"] = df["title"].str.strip()

# Step 3 — Save as CSV
# ---------------------------------------

# Ensure data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

output_file = "data/trends_clean.csv"

df.to_csv(output_file, index=False)

print(f"\nSaved {len(df)} rows to {output_file}")

# Summary: stories per category
print("\nStories per category:")
print(df["category"].value_counts())