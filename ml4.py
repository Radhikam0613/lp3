import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from tensorflow.keras.models import Sequential # Sequential builds a neural network layer by layer.
from tensorflow.keras.layers import Dense, Dropout # Dense creates fully connected neural network layers.Dropout reduces overfitting by randomly disabling some neurons during training.
from tensorflow.keras.callbacks import EarlyStopping # EarlyStopping stops training when validation performance stops improving.

df = pd.read_csv('data.csv')

df = df.drop(columns=['RowNumber', 'CustomerId', 'Surname'])

X = df.drop(columns=['Exited'])
y = df['Exited']

X = pd.get_dummies(X, columns=['Geography', 'Gender'], dtype=int) # dtype=int represents encoded values as 0 or 1.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) # stratify=y preserves approximately the same proportion of each outcome class in both sets.

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(16, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
history = model.fit(
    X_train, y_train, validation_split=0.2,
    epochs=100, batch_size=32,
    callbacks=[early_stop], verbose=1
)
y_pred = (model.predict(X_test, verbose=0) >= 0.5).astype(int).ravel()

print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training vs Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training vs Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

#plt.figure(figsize=(12, 5)) — creates a figure 12 inches wide and 5 inches tall.
#plt.subplot(1, 2, 1) — selects the first plot (left).
#plt.subplot(1, 2, 2) — selects the second plot (right).













# model = Sequential([
#     # Dense(16, activation='relu', ...) creates a hidden layer with 16 neurons. 
#     # ReLU outputs max(0,x), helping the network learn nonlinear patterns.
#     # input_shape=(X_train.shape[1],) specifies the number of input features after encoding.
#     Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
#     Dropout(0.2),
#     Dense(16, activation='relu'),
#     Dropout(0.2),
#     # Dense(1, activation='sigmoid') creates one output neuron. 
#     # Sigmoid returns a value between 0 and 1, interpreted as the 
#     # estimated probability of churn.
#     Dense(1, activation='sigmoid')
# ])

# # optimizer='adam' updates model weights to reduce prediction error.Adam used? Adam is an adaptive optimization algorithm that adjusts parameter updates using estimates of gradients and their historical magnitude
# # loss='binary_crossentropy' is the standard loss function for binary classification.
# # metrics=['accuracy'] tracks the proportion of correct predictions during training.
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# # monitor='val_loss' monitors the loss on validation data.
# # patience=5 stops training after 5 consecutive epochs 
# # without improvement in validation loss.
# # restore_best_weights=True restores the model weights 
# # from the epoch with the lowest validation loss.
# early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# # epoch One complete pass through the training data.
# # epochs = 100 Maximum of 100 training iterations over the dataset
# # verbose=1 Displays training progress
# # history Stores training and validation loss and accuracy for each epoch
# history = model.fit(
#     X_train, y_train, validation_split=0.2,
#     epochs=100, batch_size=32,
#     callbacks=[early_stop], verbose=1
# )

# # This line converts the neural network's probability predictions into binary class labels.
# # (model.predict(X_test, verbose=0) predicts prb, then we apply threshhold and 
# # seperate in true and false then (astype(int)) convert to int and (ravel()) flatten the array
# y_pred = (model.predict(X_test, verbose=0) >= 0.5).astype(int).ravel()