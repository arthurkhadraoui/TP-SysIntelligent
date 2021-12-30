import numpy as np
import csv
import tensorflow as tf
from io import StringIO
import matplotlib.pyplot as plt

inputs=[]
teacher = []




inputs = np.genfromtxt('INPUTS.csv',usecols=range(7),dtype='int',skip_header=1,delimiter=';')
teacher = np.genfromtxt('INPUTS.csv',usecols=7,dtype='int',skip_header=1,delimiter=';')

x = np.array(inputs)
y = np.array(teacher)
y = tf.keras.utils.to_categorical(y)

sgd = tf.keras.optimizers.SGD(lr=1)
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(10, input_dim=7, activation='sigmoid'))
model.summary()
model.compile(optimizer=sgd, loss='binary_crossentropy')
history = model.fit(x, y, epochs=2000)

value_to_guess = inputs
predictions = model.predict(value_to_guess)
print([teacher[np.argmax(v)-1] for v in predictions])
print(history.history.keys())
print(history.history['loss'])
plt.plot(history.history['loss'])
plt.show()