import os
import tweepy
from PIL import Image
import requests
from io import BytesIO
from datetime import datetime
import pytz
import time

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception(f"Error downloading image: Status code {response.status_code}")

def update_twitter_header(api, image_paths, current_hour):
    image_index = current_hour - 2
    if 0 <= image_index < len(image_paths):
        image_url = image_paths[image_index]
        if image_url.startswith('http'):
            img = download_image(image_url)
        else:
            img = Image.open(image_url)
        
        img = img.resize((1500, 500))
        img_rgb = img.convert('RGB')
        img_rgb.save("header.jpg")
        api.update_profile_banner("header.jpg")
        print("updated!")
    else:
        raise Exception("Invalid hour or no image path available.")

if __name__ == '__main__':
    image_paths = [
        #Put your Pics here
    ]

    # credentials
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    riyadh_time = datetime.now(riyadh_tz)
    update_twitter_header(api, image_paths, riyadh_time.hour)
