import cv2
import numpy as np
from imgaug import augmenters as iaa
from pathlib import Path
import os, sys

# Para usar esse arquivo basta executar o comando passando os seguintes argumentos:
# python renomear_arquivos.py FOLDER_DESEJA_RENOMEAR FOLDER_DESTINO NUM_INICIAL

PATH_ORIGEM = sys.argv[1]
PATH_DESTINO = sys.argv[2]
N_IMAGES_POR_IMAGEM = int(sys.argv[3])
EXTENSION = '.png'
n_img_aug = 0


seq = iaa.Sequential([
        iaa.Fliplr(0.50), # horizontally flip 50% of the images
        iaa.Flipud(0.50), # vertical flip 50% of the images
        iaa.Sometimes(
            0.5, # 50%
            iaa.GaussianBlur(sigma=(0, 0.5))
        ),
        iaa.LinearContrast((0.75, 1.5)),
        iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
        iaa.Multiply((0.8, 1.2), per_channel=0.2),
        iaa.Sometimes(
            0.4, # 40%
            iaa.Rot90(1),
        ),  
        ]
        , random_order=True) # apply augmenters in random order)
print(len(os.listdir(PATH_ORIGEM)))

# Pega cada imagem do diretório images para serem modificadas para o novo diretório
for file in os.listdir(PATH_ORIGEM)[:]:
    img = cv2.imread(os.path.join(PATH_ORIGEM, file), cv2.IMREAD_COLOR)
    height, width, channels = img.shape

    for i in range(0, N_IMAGES_POR_IMAGEM):
        n_img_aug = n_img_aug + 1
        # Data augmentation
        img = img.reshape(1, height, width, channels) # 4D-array - 1 batch
        img_aug = seq(images=img)
        img_aug = img_aug.reshape(height, width, channels) # retornar para 3D-array para salvar
        cv2.imwrite(os.path.join(PATH_DESTINO, f'{n_img_aug:0>6d}' + EXTENSION), img_aug)

sys.exit()
