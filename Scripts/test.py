import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt

# load the a HDF5 file containing the model 
model = tf.keras.models.load_model('models/mnist_model.h5')

# load the dataset
mnist_dataset, mnist_info = tfds.load(name='mnist', with_info=True, as_supervised=True)
mnist_test = mnist_dataset['test']

# preprocess the data
def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255.
    return image, label

test_data = mnist_test.map(scale)  # apply the scale function to the test data
test_data = test_data.batch(10000) # batch the test data

# evaluate the model
test_loss, test_accuracy = model.evaluate(test_data)
# Print test results
print('Test loss: {0:.4f}. Test accuracy: {1:.2f}%'.format(test_loss, test_accuracy*100.))