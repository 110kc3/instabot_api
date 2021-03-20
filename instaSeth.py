#!/usr/bin/python
# - * - coding: utf-8 - * -
from __future__ import unicode_literals

import argparse
import os
import sys
#import random #random time posting
import captions_for_medias

from instabot import Bot  # noqa: E402

import schedule
import time
from datetime import datetime

sys.path.append(os.path.join(sys.path[0], "../../"))

#photosPostedFileBackup = open('/home/sppedi1103/python_scripts/instaBot/instaRick/photosPostedBackup2.txt', 'w')

#reading file which picture was posted recently
#photosToRead = open('/home/sppedi1103/python_scripts/instaBot/instaRick/photosPosted2.txt', 'r')
#photosToReadNumber = int(photosToRead.readline())
#photosToRead.close()

#incrementing picture for posting new one
#photosToReadNumber = photosToReadNumber + 1

print("Working...  Date: " + str(datetime.now().strftime("%d-%m-%Y %H:%M")))

#photosPostedFileBackup.write(str(datetime.now().strftime("%d-%m-%Y %H:%M") + " Photo count is: " + str(photosToReadNumber) + "\n"))
print(str(datetime.now().strftime("%d-%m-%Y %H:%M")) + " is party time")



parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("-photo", type=str, help="photo name")
parser.add_argument("-caption", type=str, help="caption for photo")
parser.add_argument('-tag', action='append', help='taged user id')

args = parser.parse_args()

bot = Bot()

#photosToRead = open('/home/sppedi1103/python_scripts/instaBot/instaRick/photosPosted2.txt', 'r')
#photosToReadNumber = int(photosToRead.readline())
#photosToRead.close()

instaFile = open('username.txt', 'r')
instaUsername = str(instaFile.readline())
print(instaUsername)
instaFile.close()


instaFile2 = open('password.txt', 'r')

instaPass= str(instaFile2.readline())
print(instaPass)
instaFile2.close()


#bot.login(username=instaUsername,password=str(instaPass))
bot.login(username=instaUsername,password=instaPass)

# posted_pic_file = "pics.txt"

# posted_pic_list = []
caption = ""
customCaption = str(datetime.now().strftime("%d-%m-%Y")) +" is party time"
#Let's see how long i can go without instagram blocking my account"  

# #writing posted pic number to same file and clearing it's context
# photosToWrite = open('/home/sppedi1103/python_scripts/instaBot/instaRick/photosPosted2.txt', 'w')
# photosToWrite.write(str(photosToReadNumber))
# photosToWrite.close()

pic="party.jpg"
pics = [pic]


try:
    for pic in pics:
        bot.logger.info("Checking {}".format(pic))
        if args.caption:
            caption = args.caption
        else:
            caption = customCaption
        bot.logger.info(
            "Uploading pic `{pic}` with caption: `{caption}`".format(
                pic=pic, caption=caption
            )
        )

        
        if not bot.upload_photo(
            os.path.dirname(os.path.realpath(__file__)) + "/media/" + pic,
            caption=caption,
            #user_tags=users_to_tag
            options={'rename':0}
        ):
            bot.logger.error("Something went wrong with uploading photo...")
            break
        #posted_pic_list.append(pic)
        # with open(posted_pic_file, "a") as f:
        #     f.write(pic + "\n")
        bot.logger.info("Succesfully uploaded: " + pic)
        break
except Exception as e:
    bot.logger.error("\033[41mERROR...\033[0m")
    bot.logger.error(str(e))






