import pandas as pd
import tensorflow as tf

# Load data from file
df = pd.read_csv("examples.txt", delimiter=":", header=None, names=["label", "text"])

# Clean data
df["text"] = df["text"].str.lower().str.strip()

# Convert labels to one-hot encoding
labels = pd.get_dummies(df["label"])

# Tokenize text
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(df["text"])
sequences = tokenizer.texts_to_sequences(df["text"])
word_index = tokenizer.word_index

# Pad sequences to a fixed length
max_length = 100
padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_length, padding="post")

