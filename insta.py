from instapy import InstaPy
from instabot import Bot
from random import randint
from time import sleep
from os import listdir
from os.path import isfile, join
import os
import glob
#----------------->
# cookie_del = glob.glob("config/*cookie.json")
# os.remove(cookie_del[0])
#----------------->
usrName='pmyogz'
passwd='tafakorepars38'

def UpLoad_dir(usr,passwrd,dirPath):

    cookie_del=glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])
    bot=Bot()
    bot.login(username=usr,password=passwrd)
    ListOnlyFiles=[f for f in listdir(dirPath) if isfile(join(dirPath,f))]
    if len(ListOnlyFiles)>=11:
        print("illogical amount of photos for uploading")
        return 0
    else:
        for i in ListOnlyFiles:
            Npath=dirPath+'/'+i
            sleep(30)
            bot.upload_photo(Npath, caption=i)

UpLoad_dir(usrName,passwd,dirPath='/home/dragonfly/Downloads/pics/17520.jpg')

def UPload (usr,passwrd,pathtophoto):
    cookie_del=glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])
    bot=Bot()
    bot.login(username=usr,password=passwrd)
    sleep(30)
    bot.upload_photo(pathtophoto)

#UpLoad(usrName,passwd,dirPath='/home/dragonfly/Downloads/pics/17520.jpg')

#             '''instaBot'''

# bot.upload_photo('/home/dragonfly/Downloads/pics/1243.jpeg',caption='nice !')
# bot.follow('personsId')
# bot.send_message('Hi how are you my friend')
# followers = bot.get_user_followers('personsId')
# for follower in followers:
#     print(bot.get_user_info(follower))
#bot.download_stories(story_usrName)


# session = InstaPy(username=usrName,password=passwd)
# session.login()
# sleep(10)
# session.like_by_tags(['bmw','mercedes'], amount=1)
# session.set_dont_like(['naked','nsfw'])
#session.set_do_follow(True,percentage=2)
#session.set_do_comment(['nice!','gorgeous'])

# from os import listdir
# from os.path import isfile, join
# mypath='/home/dragonfly/Documents/python/mysql/'
# ListOnlyFiles=[f for f in listdir(mypath) if isfile(join(mypath, f))]
