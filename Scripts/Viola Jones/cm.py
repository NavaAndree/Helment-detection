# import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# Crea una matriz de confusión
cm = [[3495, 117],
      [25, 3585]]

# Visualiza la matriz de confusión
plt.figure(figsize=(5, 5))
plt.imshow(cm, cmap="Blues")
plt.title("Matriz de confusión")
plt.xlabel("Clase predicha")
plt.ylabel("Clase real")
plt.xticks([0, 1], ["Clase 0", "Clase 1"])
plt.yticks([0, 1], ["Clase 0", "Clase 1"])

for i in range(len(cm)):
    for j in range(len(cm[0])):
        plt.text(j, i, cm[i][j], ha='center', va='center')

plt.show()