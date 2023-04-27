import pandas as pd
import tensorflow as tf

# Load data from file
df = pd.read_csv("example.txt", delimiter=":", header=None, names=["label", "text"])

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

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(word_index) + 1, 64, input_length=max_length),
    tf.keras.layers.Conv1D(128, 5, activation="relu"),
    tf.keras.layers.GlobalMaxPooling1D(),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(len(labels.columns), activation="softmax")
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()

# Train the model
model.fit(padded_sequences, labels, epochs=10, verbose=1)

# Test the model with user input
while True:
    input_text = input("Enter symptoms separated by comma: ")
    input_text = input_text.lower().strip().split(",")
    input_sequences = tokenizer.texts_to_sequences([input_text])
    input_padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(input_sequences, maxlen=max_length, padding="post")
    predicted_label = model.predict(input_padded_sequences)
    predicted_index = predicted_label[0].argmax()
    predicted_disease = labels.columns[predicted_index]
    print(f"Predicted Disease: {predicted_disease}")
    if input("Do you want to test again? (y/n): ").lower() != "y":
        break
# Total params: 55,107
# Trainable params: 55,107
# Non-trainable params: 0
# _________________________________________________________________
# Epoch 1/10
# 3/3 [==============================] - 4s 42ms/step - loss: 1.0942 - accuracy: 0.4306
# Epoch 2/10
# 3/3 [==============================] - 0s 31ms/step - loss: 1.0677 - accuracy: 0.8194
# Epoch 3/10
# 3/3 [==============================] - 0s 27ms/step - loss: 1.0438 - accuracy: 0.9444
# Epoch 4/10
# 3/3 [==============================] - 0s 31ms/step - loss: 1.0137 - accuracy: 0.9722
# Epoch 5/10
# 3/3 [==============================] - 0s 27ms/step - loss: 0.9754 - accuracy: 0.8611
# Epoch 6/10
# 3/3 [==============================] - 0s 32ms/step - loss: 0.9360 - accuracy: 0.7917
# Epoch 7/10
# 3/3 [==============================] - 0s 24ms/step - loss: 0.8907 - accuracy: 0.8333
# Epoch 8/10
# 3/3 [==============================] - 0s 34ms/step - loss: 0.8316 - accuracy: 0.9028
# Epoch 9/10
# 3/3 [==============================] - 0s 27ms/step - loss: 0.7671 - accuracy: 0.9722
# Epoch 10/10
# 3/3 [==============================] - 0s 27ms/step - loss: 0.6998 - accuracy: 0.9861