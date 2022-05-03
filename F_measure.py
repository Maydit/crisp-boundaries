import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def dice(pred, true, k = 1):
    intersection = np.sum(pred[true==k]) * 2.0
    dice = intersection / (np.sum(pred) + np.sum(true))
    return dice

def dice_coef(img, img2):
        if img.shape != img2.shape:
            raise ValueError("Shape mismatch: img and img2 must have to be of the same shape.")
        else:
            
            lenIntersection=0
            
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    if ( np.array_equal(img[i][j],img2[i][j]) ):
                        lenIntersection+=1
             
            lenimg=img.shape[0]*img.shape[1]
            lenimg2=img2.shape[0]*img2.shape[1]  
            value = (2. * lenIntersection  / (lenimg + lenimg2))
        return value

def get_dice(path1, path2):
  y_pred = cv2.imread(path1, cv2.IMREAD_UNCHANGED)
  y_true = cv2.imread(path2, cv2.IMREAD_UNCHANGED)
  y_true = cv2.resize(y_true, (640, 360))
  y_true = cv2.bitwise_not(y_true)
  _, y_true = cv2.threshold(y_true, 127, 255, cv2.THRESH_BINARY)
  _, y_pred = cv2.threshold(y_pred, 127, 255, cv2.THRESH_BINARY)
  return dice_coef(y_pred, y_true)

if __name__ == '__main__':
  num = 0
  total = 0
  for filename in os.listdir('datasets/BIPED_eval'):
    f = os.path.join('datasets/BIPED_eval', filename)
    fother = os.path.join('datasets/BIPED_gt', filename[:-4] + '.png')
    if os.path.isfile(f):
      total += get_dice(f, fother)
      num += 1
  print(total / num)