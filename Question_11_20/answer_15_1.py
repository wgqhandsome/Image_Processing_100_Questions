import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
H, W,C = img.shape


b = img[:,:,0].copy()
g = img[:,:,1].copy()
r = img[:,:,1].copy()

# Gray scale
gray = 0.2126*r + 0.7152*g + 0.0772*b
gray = gray.astype(np.uint8)

# Sobel filter
K_size = 3

# Zero padding
pad = K_size//2
out_h = np.zeros((H + pad*2, W + pad*2), dtype=np.float)
out_v = np.zeros((H + pad*2, W + pad*2), dtype=np.float)
out_h[pad:pad+H, pad:pad+W] = gray.copy.astype(np.float)
out_v[pad:pad+H, pad:pad+W] = gray.copy.astype(np.float)
tem = out_h.copy()




