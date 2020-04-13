from pynput.mouse import Button, Controller
import time
import webbrowser

#takes the posts to be liked
posts = ['https://www.instagram.com/p/B1VIu0WDQgc/', 'https://www.instagram.com/p/ByyhF5xjFsa/',
         'https://www.instagram.com/p/BzvmaRODVES/', 'https://www.instagram.com/p/Bzw3lJKjnnd/',
         'https://www.instagram.com/p/B0Wc4kJD904/', 'https://www.instagram.com/p/B1VIu0WDQgc/',
         'https://www.instagram.com/p/BwlQsluDhhV/', 'https://www.instagram.com/p/BwiN-bDDbx5/',
         'https://www.instagram.com/p/BwSmlL8D731/', 'https://www.instagram.com/p/Bum56R7D-68/']

while True:
    for i in range(0, len(posts)):
        webbrowser.open(posts[i])
        mouse = Controller()
        time.sleep(3)
        mouse.position = (320,560)
        mouse.click(Button.left,2)
        time.sleep (2)
