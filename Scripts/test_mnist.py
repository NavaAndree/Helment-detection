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
#test_loss, test_accuracy = model.evaluate(test_data)
# Print test results
#print('Test loss: {0:.4f}. Test accuracy: {1:.2f}%'.format(test_loss, test_accuracy*100.))

# Split the test data into two arrays containing the images and the labels
for images, labels in test_data.take(1):
    images_test = images.numpy()
    labels_test = labels.numpy()

# Reshape the images to 28x28
images_plot = np.reshape(images_test, (10000, 28, 28))

i = 589
# Plot the first 100 images
plt.figure(figsize=(2,2))
plt.axis('off')
plt.imshow(images_plot[i-1], cmap='gray', aspect='auto')
plt.show()

# Print the label of the first image
print('Label: {}'.format(labels_test[i-1]))

# Predict the label of the first image
predictions = model.predict(images_test)
print('Prediction: {}'.format(np.argmax(predictions[i-1])))
