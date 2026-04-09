import pandas as pd
import numpy as np
import os

# Step 1 — Load and Explore
# ---------------------------------------

file_path = "data/trends_clean.csv"

try:
    df = pd.read_csv(file_path)
    print(f"Loaded data: {df.shape}")
except Exception as e:
    print("Error loading file:", e)
    df = pd.DataFrame()

# Print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Average values using pandas
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score   : {int(avg_score)}")
print(f"Average comments: {int(avg_comments)}")

# Step 2 — Analysis with NumPy
# ---------------------------------------

scores = df["score"].values
comments = df["num_comments"].values

print("\n--- NumPy Stats ---")

# Mean, Median, Std
print(f"Mean score   : {int(np.mean(scores))}")
print(f"Median score : {int(np.median(scores))}")
print(f"Std deviation: {int(np.std(scores))}")

# Max and Min
print(f"Max score    : {int(np.max(scores))}")
print(f"Min score    : {int(np.min(scores))}")

# Category with most stories
category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Story with most comments
max_comments_index = np.argmax(comments)
top_story = df.iloc[max_comments_index]

print(f"\nMost commented story: \"{top_story['title']}\" — {top_story['num_comments']} comments")

# Step 3 — Add New Columns
# ---------------------------------------

# Engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = score > average score
df["is_popular"] = df["score"] > avg_score

# Step 4 — Save Result
# ---------------------------------------

output_file = "data/trends_analysed.csv"

df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")