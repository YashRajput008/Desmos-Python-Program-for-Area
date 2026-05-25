import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import binary_closing, binary_fill_holes

# ----------------------------
# 1. Load image
# ----------------------------
img = Image.open("desmos-graph.png").convert("L")
img = np.array(img)

print("Image stats:")
print("min:", img.min())
print("max:", img.max())
print("mean:", img.mean())

# ----------------------------
# 2. Convert to binary (extract curve only)
# ----------------------------
# Dark pixels = graph lines
binary = img < 80   # adjust 60–120 if needed

print("Binary coverage:", np.mean(binary))

# ----------------------------
# 3. Clean + connect curve
# ----------------------------
outline = binary_closing(binary, iterations=1)

# ----------------------------
# 4. Fill enclosed region
# ----------------------------
filled = binary_fill_holes(outline)

# ----------------------------
# 5. Pixel dimensions
# ----------------------------
height_px, width_px = filled.shape

# ----------------------------
# 6. Graph coordinate dimensions
# ----------------------------
width_units = 12
height_units = 41

# ----------------------------
# 7. Convert pixels → area
# ----------------------------
area_per_pixel = (width_units * height_units) / (width_px * height_px)

area_graph_units = np.sum(filled) * area_per_pixel

print("\nEstimated area:", area_graph_units)

# ----------------------------
# 8. Visual debugging
# ----------------------------
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(binary, cmap="gray")
plt.title("Binary (curve extraction)")

plt.subplot(1, 3, 2)
plt.imshow(outline, cmap="gray")
plt.title("Outline (after closing)")

plt.subplot(1, 3, 3)
plt.imshow(filled, cmap="gray", vmin=0, vmax=1)
plt.title("Filled region")

plt.tight_layout()
plt.show()
