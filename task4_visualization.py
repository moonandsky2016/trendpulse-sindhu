import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1 — Setup
# ---------------------------------------

file_path = "data/trends_analysed.csv"

# Load data
df = pd.read_csv(file_path)

# Create outputs folder if not exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# Helper function to shorten long titles
def shorten_title(title, max_len=50):
    return title[:max_len] + "..." if len(title) > max_len else title


# Step 2 — Chart 1: Top 10 Stories by Score
# ---------------------------------------

top10 = df.sort_values(by="score", ascending=False).head(10)

titles = [shorten_title(t) for t in top10["title"]]

plt.figure(figsize=(8, 6))
plt.barh(titles, top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()  # highest at top

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# Step 3 — Chart 2: Stories per Category
# ---------------------------------------

category_counts = df["category"].value_counts()

plt.figure(figsize=(6, 5))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()


# Step 4 — Chart 3: Scatter Plot (Score vs Comments)
# ---------------------------------------

plt.figure(figsize=(6, 5))

# Separate popular vs non-popular
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()


# Bonus — Dashboard
# ---------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1 (Barh)
axes[0].barh(titles, top10["score"])
axes[0].set_title("Top 10 Stories")
axes[0].invert_yaxis()

# Chart 2 (Bar)
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Stories per Category")

# Chart 3 (Scatter)
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

fig.suptitle("TrendPulse Dashboard")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("Charts saved in outputs/ folder")