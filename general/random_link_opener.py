import webbrowser
import random
import time

websites = ['google.com', 'github.com', 'facebook.com', 'gmail.com', 'youtube.com']

while True:
    site = random.choice(websites)
    visit = 'https://{}'.format(site)
    webbrowser.open(visit)
    # Selects a random number from range 5 to 20, so that all links doesn't open at once.
    sec = random.randrange(5, 20)
    time.sleep(sec)
