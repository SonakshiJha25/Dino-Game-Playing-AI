import cv2
import numpy as np
import pyautogui

# Function to load and resize obstacle images
def load_and_resize(image_path, size=(50, 50)):  # Resize all images to (50x50)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img_resized = cv2.resize(img, size)
        print(f"✅ {image_path} loaded successfully with new size {img_resized.shape}")
        return img_resized
    else:
        print(f"❌ Failed to load {image_path}")
        return None

# Load all 6 cactus images
cactus_images = [
    load_and_resize('cactus1.png'),
    load_and_resize('cactus2.png'),
    load_and_resize('cactus3.png'),
    load_and_resize('cactus4.png'),
    load_and_resize('cactus5.png'),
    load_and_resize('cactus6.png')
]

# Load 2 bird images
bird_images = [
    load_and_resize('bird1.png'),
    load_and_resize('bird2.png')
]

# Set detection area (where obstacles appear)
x, y, width, height = 250, 400, 600, 150  # Adjust as needed

def detect_obstacle():
    screen = pyautogui.screenshot(region=(x, y, width, height))
    screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)

    # Check for cactus
    for i, cactus_img in enumerate(cactus_images):
        if cactus_img is not None:
            res_cactus = cv2.matchTemplate(screen_gray, cactus_img, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res_cactus)
            print(f"🔍 Cactus{i+1}: Max Match = {max_val}")  # Debugging info
            if max_val >= 0.7:  # If confidence is above threshold
                print(f"🚨 Cactus detected at {max_loc}!")
                return "cactus"

    # Check for bird
    for i, bird_img in enumerate(bird_images):
        if bird_img is not None:
            res_bird = cv2.matchTemplate(screen_gray, bird_img, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res_bird)
            print(f"🔍 Bird{i+1}: Max Match = {max_val}")  # Debugging info
            if max_val >= 0.7:  # If confidence is above threshold
                print(f"🚨 Bird detected at {max_loc}!")
                return "bird"

    print("✅ No obstacles detected")
    return None

# Test function
if __name__ == "__main__":
    while True:
        detect_obstacle()
