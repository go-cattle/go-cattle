import pandas as pd
import tensorflow as tf

# Load data from file
df = pd.read_csv("examples.txt", delimiter=":", header=None, names=["label", "text"])

# Clean data
df["text"] = df["text"].str.lower().str.strip()

# Convert labels to one-hot encoding
labels = pd.get_dummies(df["label"])

