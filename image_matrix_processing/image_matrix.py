from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. Load image (same folder me 'ss.png' hona chahiye)
img = Image.open("ss.png").convert("L")  # Convert to grayscale
img_array = np.array(img)

print("Original Image Array Shape:", img_array.shape)

# 2. Adjust brightness (add 50)
bright_img = np.clip(img_array + 50, 0, 255)

# 3. Adjust contrast (scale pixels by 1.2)
contrast_img = np.clip(1.2 * img_array, 0, 255)

# 4. Convert numpy arrays back to images
bright_image = Image.fromarray(bright_img.astype(np.uint8))
contrast_image = Image.fromarray(contrast_img.astype(np.uint8))

# 5. Save processed images
bright_image.save("bright_ss.png")
contrast_image.save("contrast_ss.png")

# 6. Show images
plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(img_array, cmap="gray")
plt.axis("off")

plt.subplot(1,3,2)
plt.title("Brightness +50")
plt.imshow(bright_img, cmap="gray")
plt.axis("off")

plt.subplot(1,3,3)
plt.title("Contrast x1.2")
plt.imshow(contrast_img, cmap="gray")
plt.axis("off")

plt.show()
