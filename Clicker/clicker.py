from pynput.mouse import Button, Controller
import time
import webbrowser
import threading
import random
while True:
    sites = random.choice(['https://www.instagram.com/p/B1VIu0WDQgc/','https://www.instagram.com/p/ByyhF5xjFsa/','https://www.instagram.com/p/BzvmaRODVES/','https://www.instagram.com/p/Bzw3lJKjnnd/','https://www.instagram.com/p/B0Wc4kJD904/','https://www.instagram.com/p/B1VIu0WDQgc/','https://www.instagram.com/p/BwlQsluDhhV/','https://www.instagram.com/p/BwiN-bDDbx5/','https://www.instagram.com/p/BwSmlL8D731/','https://www.instagram.com/p/Bum56R7D-68/'])
    webbrowser.open(sites)
    mouse = Controller()
    time.sleep(3)
    mouse.position = (320,560)
    mouse.click(Button.left,2)
    time.sleep (2)