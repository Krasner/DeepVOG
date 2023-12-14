import numpy as np
import skimage.io as ski
from DeepVOG_model import load_DeepVOG
import cv2

def test_if_model_work():
    model = load_DeepVOG()
    img = np.zeros((1, 240, 320, 3))
    # img[:, :, :, :] = (ski.imread("test_image.png") / 255).reshape(1, 240, 320, 1)
    img[:, :, :, :] = (cv2.cvtColor(cv2.imread("test_image.png"), cv2.COLOR_BGR2GRAY).astype(np.float32) / 255).reshape(1, 240, 320, 1)
    # for onnx
    # img = img.transpose(0, 3, 1, 2) # (B, C, H, W)
    prediction = model.predict(img)
    # ski.imsave("test_prediction.png", prediction[0, :, :, 1])
    cv2.imwrite("test_prediction.png", prediction[0, :, :, 1] * 255)


if __name__ == "__main__":
    # If model works, the "test_prediction.png" should show the segmented area of pupil from "test_image.png"
    test_if_model_work()
