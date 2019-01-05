


import numpy as np
import matplotlib.pyplot as plt
import theano
from theano import tensor
import keras
from keras import layers

print('\n test numpy----\n')

arr = np.array([[1,2], [3, 4]])
print(arr)

print('\n test theao-----\n')
a = tensor.dscalar()
b = tensor.dscalar()

c = a + b

f = theano.function([a,b], c)

print('1.5+2.5=', f(1.5, 2.5))

assert 4.0 == f(1.5, 2.5)

'''
----------------
'''

print('\n Test Keras -----\n')
np.random.seed(123)  # for reproducibility
(X_train, y_train), (X_test, y_test)  = keras.datasets.mnist.load_data()
plt.imshow(X_train[0])


X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

X_train = X_train[0:]

model = keras.Sequential()
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
model.add(keras.layers.Dropout(0.25))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(10, activation='softmax'))

#----------------

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#--------
model.fit(X_train, y_train, batch_size=32, epochs=10, verbose=1)
#--------
score = model.evaluate(X_test, y_test, verbose=0)

print(score)
print(X_train.shape)
print(y_train.shape)
print(y_train[0])
#plt.show()


