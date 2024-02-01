# cron_task.py
import os
import tweepy
from PIL import Image
from datetime import datetime
import pytz

def update_twitter_header(api, image_paths, current_hour):
    image_path = image_paths[current_hour - 1] 
    img = Image.open(image_path)
    img = img.resize((1500, 500))
    img_rgb = img.convert('RGB')
    img_rgb.save("header.jpg")
    api.update_profile_banner("header.jpg")

def update_header():
    image_paths = [
        '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', 
        '9.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', 
        '16.png', '17.png', '18.png', '19.png', '20.png', '21.png', '22.png', 
        '23.png', '24.png'
    ]
    
    # Twitter API credentials should be configured as environment variables
    # for better security practices
    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    riyadh_tz = pytz.timezone('Asia/Riyadh')
    riyadh_time = datetime.now(riyadh_tz)

    update_twitter_header(api, image_paths, riyadh_time.hour)
    
    print("Twitter header updated!")

if __name__ == '__main__':
    update_header()
