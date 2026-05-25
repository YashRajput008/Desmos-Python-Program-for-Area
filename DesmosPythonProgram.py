import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import binary_closing, binary_fill_holes

img = Image.open("desmos-graph.png").convert("L")
img = np.array(img)

coords = np.column_stack(np.where(img < 250))
top, left = coords.min(axis=0)
bottom, right = coords.max(axis=0)
img = img[top:bottom, left:right]

binary = img < 80
outline = binary_closing(binary, iterations=1)
filled = binary_fill_holes(outline)

h_px, w_px = filled.shape

width_units = 12
height_units = 41

area_per_pixel = (width_units * height_units) / (w_px * h_px)
area_graph_units = np.sum(filled) * area_per_pixel

print("Estimated area:", area_graph_units)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(binary, cmap="gray")

plt.subplot(1, 3, 2)
plt.imshow(outline, cmap="gray")

plt.subplot(1, 3, 3)
plt.imshow(filled, cmap="gray", vmin=0, vmax=1)

plt.tight_layout()
plt.show()
