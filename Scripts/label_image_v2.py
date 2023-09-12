import tensorflow as tf
import sys

# Carga el modelo y el archivo de etiquetas
model = tf.keras.models.load_model("RPDir/retrained_model.h5")
label_lines = [line.rstrip() for line in tf.io.gfile.GFile("RPDir/retrained_labels.txt")]

# Carga y preprocesa la imagen
image_path = sys.argv[1]
image = tf.io.read_file(image_path)
image = tf.image.decode_jpeg(image, channels=3)
image = tf.image.convert_image_dtype(image, tf.float32)
image = tf.image.resize(image, (224, 224))  # Ajusta al tamaño requerido por el modelo

# Realiza una predicción
predictions = model.predict(tf.expand_dims(image, axis=0))

# Clasifica las predicciones en orden de confianza
top_k = tf.argsort(predictions[0], direction='DESCENDING')
for node_id in top_k:
    human_string = label_lines[node_id]
    score = predictions[0][node_id].numpy()
    print('%s (score = %.5f)' % (human_string, score))
