import cv2
import numpy as np
import pyautogui
import time
from pathlib import Path

# gets the path of skip_button reference image
def get_image_path():
    filename = 'skip_button.png'
    project_directory = Path(__file__).parent
    file_path = project_directory / filename
    return file_path

def detect_and_click_skip_button(reference_image_path=get_image_path()):
    reference_image = cv2.imread(reference_image_path)
    if reference_image is None:
        raise FileNotFoundError(f"Could not load image at path: {reference_image_path}")
    h, w, _ = reference_image.shape

    while True:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(screenshot, reference_image, cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        loc = np.where(result >= threshold)

        if loc[0].size > 0:
            for pt in zip(*loc[::-1]):
                click_x = pt[0] + w // 2
                click_y = pt[1] + h // 2
                pyautogui.click(click_x, click_y)
                print("Clicked on Skip Ads button!")
                break

        time.sleep(1)

if __name__ == "__main__":
    try:
        detect_and_click_skip_button()
    except KeyboardInterrupt:
        print("Script stopped.")