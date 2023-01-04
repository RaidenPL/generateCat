import shutil
import generateCat as Cat
from instabot import Bot

Cat.generateCat("cat","cat.jpg")

bot = Bot()
bot.login()  # login to Instagram using your account credentials

photo_path = '/home/kuba/Desktop/instaCats/cat.jpg'
caption = 'What a cute cat!  😍\n #cats #dailykitten #cutekitten #catofinsta #catsarelife #catphotos #catofig #kittenlovers #kittengram #catbaby #kittensofig #kittensofinsta #kittenlife #mycat #catsonly #cat #catlover #catmemes #kitty #politecat #catpics #cataccount #animalovers #memes #chonk #catalonia #catsocket #catagram #catphoto #catclout'

bot.upload_photo(photo_path, caption=caption)

shutil.rmtree('./config')
