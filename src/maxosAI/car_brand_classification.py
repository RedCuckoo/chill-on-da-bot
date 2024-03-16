import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open("../car_brands.txt", "r", encoding="utf-8") as f:
    messages = f.readlines()

messages = [message.strip() for message in messages]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(messages)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(messages)
max_len = max([len(seq) for seq in sequences])
padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')

# Extract unique words from the tokenizer's word index
labels = list(word_index.keys())

# Ensure that each input sequence has a corresponding label
labels = labels[:len(padded_sequences)]

# Convert labels to indices
label_to_index = {label: index for index, label in enumerate(labels)}
label_indices = np.array([label_to_index[label] for label in labels])

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(word_index) + 1, output_dim=16),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(len(labels), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(padded_sequences, label_indices, epochs=10)

model.save("car_brand_classification_model.h5")  # Save the model with the correct file extension

print("Model saved")

with open("labels.txt", "w", encoding="utf-8") as f:
    for label in labels:
        f.write(label + "\n")

print("Labels saved")
