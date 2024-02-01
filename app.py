import os
import tweepy
from PIL import Image
from datetime import datetime
import pytz

def update_twitter_header(api, image_paths, current_hour):

    image_path = image_paths[current_hour - 1] 

    # Open and resize the image
    img = Image.open(image_path)
    img = img.resize((1500, 500))

    # Convert the image from RGBA to RGB
    img_rgb = img.convert('RGB')

    # Save the image
    img_rgb.save("header.jpg")

    # Update the Twitter header
    api.update_profile_banner("header.jpg")

if __name__ == '__main__':
    # Array of image paths
    image_paths = [
        '1.png',  
        '2.png', 
        '3.png', 
        '4.png', 
        '5.png', 
        '6.png', 
        '7.png', 
        '8.png', 
        '9.png', 
        '10.png', 
        '11.png', 
        '12.png', 
        '13.png', 
        '14.png', 
        '15.png', 
        '16.png', 
        '17.png', 
        '18.png', 
        '19.png', 
        '20.png', 
        '21.png', 
        '22.png', 
        '23.png', 
        '24.png', 
    ]

    # Twitter API credentials
    consumer_key = 'EYiDp3DAgJ63GWglkd7t7NKto'
    consumer_secret = 'GEogBm4WhpidViklHgRM0TEJ2X2da9TWoOjcw5vp0adpfdftkP'
    access_token = '1298426893730029568-TYC4ISkKBMgRUBax2iXdk1VySb5Fxg'
    access_token_secret = 'gVCC24yNeMduHwHRw55T9KBUDqaOu0Nw9fXJJCpJiczGE'

    # Authenticate with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get the current time in Riyadh
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    riyadh_time = datetime.now(riyadh_tz)

    # Call the function with the current hour in Riyadh
    update_twitter_header(api, image_paths, riyadh_time.hour)
