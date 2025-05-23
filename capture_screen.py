import pyautogui
import cv2
import numpy as np
import time

# Define region of interest (ROI)
ROI_X = 400  
ROI_Y = 380  
ROI_WIDTH = 150  
ROI_HEIGHT = 50    

def detect_obstacle():
    # Capture the defined region
    screenshot = pyautogui.screenshot(region=(ROI_X, ROI_Y, ROI_WIDTH, ROI_HEIGHT))
  
    # Convert to grayscale
    gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Apply edge detection (Canny filter)
    edges = cv2.Canny(gray, threshold1=100, threshold2=200)

    # Show the processed image (debugging)
    cv2.imshow("Obstacle Detection", edges)  
    cv2.waitKey(1)  

    # Count white pixels
    obstacle_count = np.sum(edges == 255)

    return obstacle_count > 300  

print("AI will start in 3 seconds...")
time.sleep(3)

while True:
    if detect_obstacle():
        print("Obstacle detected! Jumping...")
        pyautogui.press("space")  

    time.sleep(0.05)  
                 