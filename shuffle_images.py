import os
import glob
import numpy as np

from shutil import copyfile


def shuffle_and_move_images(IMAGES_DIR, DATA_HOME_DIR):
    g = glob(IMAGES_DIR + '*.jpg')
    shuf = np.random.permutation(g)
    for i in range(2000):
        os.rename(shuf[i], DATA_HOME_DIR+'/valid/' + shuf[i])


def shuffle_and_copy_images(IMAGES_DIR, DATA_HOME_DIR):
    g = glob('*.jpg')
    shuf = np.random.permutation(g)
    for i in range(200):
        copyfile(shuf[i], DATA_HOME_DIR+'/sample/train/' + shuf[i])
