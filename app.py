from flask import Flask
from flask_apscheduler import APScheduler
import os
import tweepy
from PIL import Image
from datetime import datetime
import pytz
import time

app = Flask(__name__)
scheduler = APScheduler()

def update_twitter_header(api, image_paths, current_hour):
    image_path = image_paths[current_hour - 1] 
    img = Image.open(image_path)
    img = img.resize((1500, 500))
    img_rgb = img.convert('RGB')
    img_rgb.save("header.jpg")
    api.update_profile_banner("header.jpg")

@app.route('/update_header')
def update_header():
    image_paths = [
        '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', 
        '9.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', 
        '16.png', '17.png', '18.png', '19.png', '20.png', '21.png', '22.png', 
        '23.png', '24.png'
    ]
    
    # Twitter API credentials should be configured as environment variables
    # for better security practices
    consumer_key = 'EYiDp3DAgJ63GWglkd7t7NKto'
    consumer_secret = 'GEogBm4WhpidViklHgRM0TEJ2X2da9TWoOjcw5vp0adpfdftkP'
    access_token = '1298426893730029568-TYC4ISkKBMgRUBax2iXdk1VySb5Fxg'
    access_token_secret = 'gVCC24yNeMduHwHRw55T9KBUDqaOu0Nw9fXJJCpJiczGE'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    riyadh_tz = pytz.timezone('Asia/Riyadh')
    riyadh_time = datetime.now(riyadh_tz)

    update_twitter_header(api, image_paths, riyadh_time.hour)
    
    return "Twitter header updated!"

# Schedule the function to run every minute
@scheduler.task('interval', id='update_header_task', seconds=60)
def scheduled_update_header():
    with app.app_context():
        update_header()

if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)
