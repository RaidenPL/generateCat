import shutil
from instabot import Bot

bot = Bot()
bot.login()  # login to Instagram using your account credentials

photo_path = '/home/kuba/Downloads/cat.jpg'
caption = 'What a cute cat!'

bot.upload_photo(photo_path, caption=caption)

shutil.rmtree('./config')
