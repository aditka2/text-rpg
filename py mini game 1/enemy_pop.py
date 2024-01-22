import cv2
import pyttsx3
import time

def popMessage(enemy_type):
    """Display an image and play a message based on the enemy type."""
    img_path = ""
    if enemy_type == 'w':
        img_path = "C:\\Users\\Adit\\Desktop\\py mini game 1\\images\\were.jpg"
        message = "you hear the howl of a wear wolf."
    elif enemy_type == 'gi':
        img_path = "C:\\Users\\Adit\\Desktop\\py mini game 1\\images\\giant.jpg"
        message = "You hear a loud thumping sound, and see a giant approaching you."
    elif enemy_type == 'f':
        img_path = "C:\\Users\\Adit\\Desktop\\py mini game 1\\images\\fire.jpg"
        message = "The temperature suddenly rises and you see a fire demon."
    elif enemy_type == 'go':
        img_path = "C:\\Users\\Adit\\Desktop\\py mini game 1\\images\\golem.jpg"
        message = "You hear a loud clunking sound, and see a golem approaching you."
    elif enemy_type == 'd':
        img_path = "C:\\Users\\Adit\\Desktop\\py mini game 1\\images\\dragon.jpg"
        message = "You hear a loud roar, and see a dragon flying towards you."
    elif enemy_type == 'j':
        img_path = "C:\\Users\\Adit\\Desktop\\py mini game 1\\images\\jeez.jpg"
        message = "A gateway opens up in the sky and you hear a loud voice."    
    else:
        print("Invalid enemy type entered.")
        return

    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say(message)
    engine.runAndWait()
    img = cv2.imread(img_path)
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", 800, 600)
    cv2.moveWindow("Image", 0, 0)
    cv2.imshow("Image", img)
    cv2.setWindowProperty("Image", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
