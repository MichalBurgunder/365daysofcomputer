# CREATED BY CHATGPT

from PIL import Image
import os

folder = "frames"
images = []

for file in sorted(os.listdir(folder)):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):
        img = Image.open(os.path.join(folder, file))
        images.append(img)

# Save as GIF
images[0].save(
    "output.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,  # milliseconds per frame
    loop=0
)
print("gif created!")