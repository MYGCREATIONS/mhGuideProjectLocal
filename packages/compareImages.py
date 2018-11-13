from skimage.measure import compare_ssim as ssim
import numpy as np
import cv2
import traceback
import sys


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def compare_images(imageA, imageB):
    try:
        imageA = cv2.imread(imageA)
        imageB = cv2.imread(imageB)
        m = mse(imageA, imageB)
        s = ssim(imageA, imageB, multichannel=True)
        # The higher the MSE value, the less similar (identical = 0, completely different = 1)
        # The lower the SSIM value, the less similar (identical = 1, completely different = 0)
        assert m < 0.05
        assert s > 0.95
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)  # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        raise Exception('An error occurred on line {} in statement {}'.format(line, text))
