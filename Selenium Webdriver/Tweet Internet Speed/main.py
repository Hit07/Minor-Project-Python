from internet_speed import InternetSpeed
from tweet import Tweet

PROMISED_DOWN = 100
PROMISED_UP = 100

obj = InternetSpeed()
obj.get_internet_speed()
print(f'Up:{obj.up}\nDown:{obj.down}')

obj_1 = Tweet()
post = f"Hey Internet Provider, why is my internet speed {obj.down}down/{obj.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
obj_1.tweet_at_provider(post)
print("Tweeted Check your feed!")