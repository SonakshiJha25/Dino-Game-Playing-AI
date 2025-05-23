import pyautogui
import time

def press_space():
    pyautogui.press('space')

def is_obstacle_detected():
    # Screenshot leke pixel check karke obstacle detect karna
    return False  # Placeholder, yeh logic implement karna hoga

def play_dino_game():
    print("Game start ho raha hai...")
    time.sleep(2)  # Thoda time dene ke liye
    
    while True:
        if is_obstacle_detected():
            press_space()
        time.sleep(0.1)  # Optimize karo jitna zaroori ho

if __name__ == "__main__":
    play_dino_game()
