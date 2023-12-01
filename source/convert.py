import cv2
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def quantization(input,output,palette):
    image = cv2.imread(input, cv2.IMREAD_UNCHANGED)
    if image.shape[2] == 3: 
        X_query = image.reshape(-1, 3).astype(np.float32)
        X_index = palette.astype(np.float32)

        knn = cv2.ml.KNearest_create()
        knn.train(X_index, cv2.ml.ROW_SAMPLE, np.arange(len(palette)))
        ret, results, neighbours, dist = knn.findNearest(X_query, 1)

        quantized_image = np.array([palette[idx] for idx in neighbours.astype(int)])
        quantized_image = quantized_image.reshape(image.shape)
        
        cv2.imwrite(output, quantized_image)
    else:
        bgr_image = image[:, :, :3]
        alpha_channel = image[:, :, 3]

        X_query = bgr_image.reshape(-1, 3).astype(np.float32)
        X_index = palette.astype(np.float32)

        knn = cv2.ml.KNearest_create()
        knn.train(X_index, cv2.ml.ROW_SAMPLE, np.arange(len(palette)))
        ret, results, neighbours, dist = knn.findNearest(X_query, 1)

        quantized_image = np.array([palette[idx] for idx in neighbours.astype(int)])
        quantized_image = quantized_image.reshape(bgr_image.shape)

        quantized_image_with_alpha = np.concatenate((quantized_image, alpha_channel[:, :, np.newaxis]), axis=2)

        cv2.imwrite(output, quantized_image_with_alpha)

def transparencyQuantization(input,output):
    image = cv2.imread(input, cv2.IMREAD_UNCHANGED)

    if image.shape[2] == 4:
        img = np.array(Image.open(input))

        r, g, b, a = img[:, :, 0], img[:, :, 1], img[:, :, 2], img[:, :, 3]

        threshold = 127

        transparent_mask = (a <= threshold)

        a[transparent_mask] = 0
        a[~transparent_mask] = 255

        new_img = np.dstack((r, g, b, a))

        result = Image.fromarray(new_img, 'RGBA')
        result.save(output)
    else:
        cv2.imwrite(output, image)

def resizeImage(input, output, width, height):
    img = Image.open(input)

    img.thumbnail((width, height),)

    img.save(output)

def convertToPNG(input,output):
    image = Image.open(input)
    image.save(output, "PNG")

def askExplorer():
    root = tk.Tk()
    root.withdraw()

    # Déterminer le chemin du bureau selon le système d'exploitation
    bureau = os.path.join(os.path.expanduser('~'), 'Desktop') if os.name == 'posix' else os.path.join(os.environ['USERPROFILE'], 'Desktop')

    fichier_selectionne = filedialog.askopenfilename(
        initialdir=bureau,  # Répertoire initial sur le bureau
        title="Sélectionner un fichier",
        filetypes=(
            ("Fichiers image", "*.webp;*.jpg;*.jpeg;*.png"),
            ("Tous les fichiers", "*.*")
        )
    )

    if fichier_selectionne:
        return fichier_selectionne
    else:
        return False