from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical
from sklearn.metrics import confusion_matrix


#scarico e assegno dati a train e test set, a parte le etichette
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#controllo quante immagini ci sono nei due dataset
num_images_train = x_train.shape[0]
print("Numero di immagini:", num_images_train)

num_images_test = x_test.shape[0]
print("Numero di immagini:", num_images_test)

#stampo alcune immaghini 
plt.figure(figsize=(7,7))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Etichetta: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()

print(x_train[0].shape)

height, width = x_train[0].shape

print("Altezza dell'immagine:", height)
print("Larghezza dell'immagine:", width)

#controllo sui valori dei pixel (bit immagine)
min_val = np.min(x_train)
max_val = np.max(x_train)

print(f"Valore minimo dei pixel: {min_val}")
print(f"Valore massimo dei pixel: {max_val}") #le immagini sono in 8 bit



#normalizzazione
x_train_norm = x_train.astype('float32') / 255
x_test_norm = x_test.astype('float32') / 255

#le etichette sono numeriche
y_train_onehot = to_categorical(y_train, num_classes=10)
y_test_onehot = to_categorical(y_test, num_classes=10)

model = Sequential()
# Appiattire le immagini 28x28 in vettori di 784 elementi
model.add(Flatten(input_shape=(28, 28)))
# Aggiungere uno strato denso con 128 neuroni e attivazione ReLU
model.add(Dense(128, activation='relu'))
# Strato di output con 10 neuroni (uno per classe) e attivazione softmax
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Stampare un riepilogo del modello
model.summary()

# Addestrare il modello
history = model.fit(x_train_norm, y_train_onehot,
                    epochs=20,
                    batch_size=32,
                    validation_split=0.1)

test_loss, test_accuracy = model.evaluate(x_test_norm, y_test_onehot)
print(f"Perdita sul test: {test_loss:.4f}")
print(f"Accuratezza sul test: {test_accuracy:.4f}")

# Grafico della perdita
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Perdita di addestramento')
plt.plot(history.history['val_loss'], label='Perdita di validazione')
plt.title('Perdita durante l\'addestramento')
plt.xlabel('Epoche')
plt.ylabel('Perdita')
plt.legend()

# Previsioni su alcune immagini di test
predictions = model.predict(x_test_norm)

# Visualizzazione delle prime 9 previsioni
plt.figure(figsize=(7, 7))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_test[i], cmap='gray')
    plt.title(f"Predizione: {np.argmax(predictions[i])}\nEtichetta reale: {y_test[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()

predictions = model.predict(x_test_norm)

y_pred = np.argmax(predictions, axis=1)

# Calcolo la matrice di confusione
confusion_mat = confusion_matrix(y_test, y_pred)

# Calcolo le percentuali
confusion_mat_percent = confusion_mat.astype('float32') / confusion_mat.sum(axis=1)[:, np.newaxis] * 100

# Visualizzo la matrice di confusione
plt.figure(figsize=(10, 7))
plt.matshow(confusion_mat_percent, cmap='Blues')
plt.colorbar()

# Aggiungo le percentuali nella matrice
for i in range(10):
    for j in range(10):
        plt.text(j, i, f"{confusion_mat_percent[i, j]:.2f}%", ha='center', va='center')

plt.xlabel('Etichetta prevista')
plt.ylabel('Etichetta reale')
plt.title('Matrice di confusione (percentuali)')
plt.show()




