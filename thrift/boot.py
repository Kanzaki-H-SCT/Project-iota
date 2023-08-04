# -*- coding: utf-8 -*-
from linepy import *

from akad.ttypes import Message

from akad.ttypes import ContentType as Type

from akad.ttypes import TalkException

from datetime import datetime, timedelta

from time import sleep

from bs4 import BeautifulSoup as bSoup

from bs4 import BeautifulSoup

from humanfriendly import format_timespan, format_size, format_number, format_length

from threading import Thread

from io import StringIO

from multiprocessing import Pool

from googletrans import Translator

from urllib.parse import urlencode

from random import randint

from shutil import copyfile

from datetime import datetime

from datetime import datetime

from time import sleep

from bs4 import BeautifulSoup

from googletrans import Translator

from humanfriendly import format_timespan, format_size, format_number, format_length

import socket,time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,timeit,atexit,youtube_dl,pafy ,pytz,asyncio

from time import sleep

from humanfriendly import format_timespan, format_size, format_number, format_length

import requests

import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz,  urllib, urllib.parse,timeit,atexit,youtube_dl,pafy

from bs4 import BeautifulSoup

from humanfriendly import format_timespan, format_size, format_number, format_length

import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit,youtube_dl,pafy

from gtts import gTTS

from googletrans import Translator

from threading import Thread

import subprocess, youtube_dl, humanize, traceback

import subprocess as cmd

import platform

import requests, json

import  subprocess, six, ast, urllib, urllib.parse,timeit,atexit,pytz

import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback

import asyncio

_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

botStart = time.time()

ts = time.time()


cl = LINE("iop73898@cuoly.com","q224300978")

cl.log(cl.authToken)
AuthToken = []
#線程數設定
for i in range(0, 1): AuthToken.append(LINE(cl.authToken))



profile = cl.getProfile()
status = str(profile.statusMessage)
lock = _name = "\n\n中路 ßöᴛ 運行中(๑′ᴗ‵๑)\n長久運作中Ing.....\n作者:中路\nMade in Taiwan\nLineID:0970737883"
if lock not in status:
    profile.statusMessage = status + lock
    cl.updateProfile(profile)
else:
    pass

oepoll = OEPoll(cl)

datadir = {"switch": False,"gid": ""}


readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen)


settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
backdoor = settings["backdoor"]
backdoor1 = settings["backdoor1"]
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
cl.sendMessage(backdoor,"復讀登入成功\n開啟時間: {} s".format(time.time()-ts))
cl.sendMessage(backdoor1,"[自動發送]\n通知作者我已經登入成功咯~")

redOpen = codecs.open("red.json","r","utf-8")
red = json.load(redOpen)

jgOpen = codecs.open("jg.json","r","utf-8")
jg = json.load(jgOpen)

banOpen = codecs.open("ban.json","r","utf-8")
ban = json.load(banOpen)


myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}


lineSettings = cl.getSettings()
clMID = cl.profile.mid
clProfile = cl.getProfile()
clSetting = cl.getSettings()


ulist = []
bl = [clMID,'u2db707c088044deb4757c666d1eea1a0']
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus


admin=[clMID,'u2db707c088044deb4757c666d1eea1a0']
X = ["u2db707c088044deb4757c666d1eea1a0","u02def746004509d0eaa645bd3035a54a"]
clfl=[]
King = clMID


msg_dict = {}
msg_dictt = {}



wait = {
    'logout': {},
    'rapidFire': {},
    'group': "",
    'getmid': False,
    'um': False,#收回高速
    'cvp': False,#更換頭貼
    'gbc':{},
    'comment':"機器自動留言中\n我的作者是:中路",
    'allbye': False,
    'resset': False#偵測更新
    }



wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
game = {
    "1a2b": {},
    "ooxx": {}
}



setTime = {}
setTime = wait2['setTime']



profile = cl.getProfile()



msg_dict = {}
msg_dictt = {}



Start = time.time()
mulai = time.time()

def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
def test(msg):
    cl.sendMessage(backdoor,"【後台系統】\n"+msg)
def test1(msg):
    cl.sendMessage(backdoor1,"【後台系統】\n"+msg)
def ismid(mid):
    try:
        cl.getContact(mid)
        return True
    except:
        return False
def ismid1(mid):
    try:
        cl.getContact(mid)
        return True
    except:
        return False
def kick(n, to, mid):
    while 1: AuthToken[n].kickoutFromGroup(to, mid); break
def Runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天\n%02d 時\n%02d 鐘\n%02d 秒\n以上為復讀機運行時間\n復讀機 運行時間測試' % (days, hours, mins, secs)
def Rtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天 %02d 時 %02d 鐘 %02d 秒' % (days, hours, mins, secs)
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(gp, codecs.open('group.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = jg
        f = codecs.open('jg.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    cl.sendMessage(backdoor,"[ 錯誤 ]" + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("[%s] %s" % (str(time), text))
        cl.sendMessage(backdoor,"[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageTag(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  此人在群組(私聊)標住您'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessagegat(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  廢物出來'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendReplyMention(self,RynId, to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@Jwwwwwwwww "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            for mid in mids:
                textx += str(texts[mids.index(mid)])
                slen = len(textx)
                elen = len(textx) + 15
                arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ""
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        return cl.sendReplyMention(msg_id, to,textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def check_input(user_input):
    try:
        int(user_input)
    except:
        return False
    for x in user_input:
        if user_input.count(x) > 1:
            return False
    if len(user_input) != 4:
        return False
    else:
        return True
def check_answer(ans, nums):
    a, b = 0, 0
    for n in nums:
        if n in ans:
            if nums.index(n) == ans.index(n):
                a += 1
            else:
                b += 1
    return a, b
def help():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('helpr.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help = text.format(key=key.title())
    return help
def help1():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('helpr1.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help1 = text.format(key=key.title())
    return help1
def help2():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('helpr2.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help2 = text.format(key=key.title())
    return help2
def unsend(msgid):
    sleep(1)
    cl.unsendMessage(msgid)
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 1:
            print ("更新配置文件")
            profile = cl.getProfile()
            status = str(profile.statusMessage)
            lock = _name = "\n\n ßöᴛ 運行中(๑′ᴗ‵๑)\n長久運作中Ing.....\n作者:中路\nMade in Taiwan\nLineID:0970737883"
            if lock not in status:
                profile.statusMessage = status + lock
                cl.updateProfile(profile)
        if op.type == 26:
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                else:
                    to = receiver
                if msg.toType == 0:
                    cl.log("[私聊監控]\n[發送者]%s"%(cl.getContact(sender).displayName+"\n"+"[訊息內容]"+msg.text))
                    cl.sendMessage(backdoor,"[私聊監控]\n●發送者:\n%s"%(cl.getContact(sender).displayName+"\n"+"●訊息內容:\n"+msg.text+"\n"+"●發送者MID:\n%s"%(msg._from)+"\n"+"●位置ID:\n%s"%(msg._from)+"\n"+"●後台位置:\n{}").format(backdoor))
                else:
                    if msg.contentType == 0:#文字
                        cl.log("[%s]"%(msg.to)+msg.text)
                    elif msg.contentType == 7:#貼圖
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata['STKID'])
                    elif msg.contentType == 13:#友資
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["mid"]+' '+msg.contentMetadata["displayName"])
                    elif msg.contentType == 14:#檔案
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["FILE_NAME"]+'檔案下載完成')
                    else:#若是都沒有則是錯誤
                        cl.log("[%s] [E]"%(msg.to)+msg.text)
                if msg.contentType == 0:#文字
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 1:#圖片
                    image = cl.downloadObjectMsg(msg_id, saveAs="檔案/圖片/{}-jpg.jpg".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"image":image,"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 2:#影片
                    Video = cl.downloadObjectMsg(msg_id, saveAs="檔案/影片/{}-Video.mp4".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"Video":Video,"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 3:#錄音檔
                    sound = cl.downloadObjectMsg(msg_id, saveAs="檔案/音檔/{}-sound.mp3".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"sound":sound,"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 7:#貼圖
                    msg_dict[msg.id] = {"from":msg._from,"id":msg.contentMetadata['STKID'],"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 13:#友資
                    msg_dict[msg.id] = {"from":msg._from,"mid":msg.contentMetadata["mid"],"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 14:#檔案
                    file = cl.downloadObjectMsg(msg_id, saveAs="檔案/檔案/{}-".format(msg.createdTime)+msg.contentMetadata['FILE_NAME'])
                    msg_dict[msg.id] = {"from":msg._from,"file":file,"createdTime":msg.createdTime,"wh":to}
                else:#若是都沒有則是錯誤
                    msg_dict[msg.id] = {"from":msg._from,"createdTime":msg.createdTime,"wh":to}
            except Exception as e:
                print(e)
        if op.type == 2:
            contact = cl.getContact(op.param1)
            if wait["resset"] == True:
                if op.param2 == "2":
                    cl.sendMessage(op.param1,"[自動發送]\n抓到更改名稱摟!!!")
                    cl.sendMessage("u4f998dda4280d43f46d3c686d28d253a","通知好友更改名稱:\n" + contact.displayName)
                if op.param2 == "8":
                    cl.sendMessage(op.param1,"[自動發送]\n抓到更改頭貼/動態頭貼摟!!!")
                    cl.sendMessage("u4f998dda4280d43f46d3c686d28d253a","通知好友更改動態頭貼:\n" + contact.displayName)
                if op.param2 == "16":
                    cl.sendMessage(op.param1,"[自動發送]\n抓到更改個簽摟!!!")
                    cl.sendMessage("u4f998dda4280d43f46d3c686d28d253a","通知好友更改個簽:\n" + contact.displayName)
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            cl.sendMessage(backdoor,"通知添加好友 名字:"+contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1,"感謝您加我為好友\n本機器為中路復讀機\n作者連結:line.me/ti/p/~0970737883")
        if op.type == 5:#自動防封鎖
            print ("[ 5 ] INV PRO")
            if settings["invBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1, "•防邀機功能運行中•\n•[已啟動自動封鎖]•\nÇręätør:中路 我的作者網址:line.me/ti/p/~none".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if op.param2 in admin or op.param2 in X:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('[進群通知]\n')
                        arr = []
                        mention = "@Mili "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "\n感謝您邀我入群組\n此機器為中路復讀機"
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        cl.sendContact(op.param1, "u2db707c088044deb4757c666d1eea1a0")
                        cl.sendMessage('u2db707c088044deb4757c666d1eea1a0',"通知邀請群組:\n" + str(group.name)+"群組 \n"+ str(group.id)+ "\n邀請者:\n" + contact1.displayName + "\nMid:\n" + contact1.mid)    
                    except Exception as error:
                        print(error)
        if op.type == 15:
            if settings["seeLeave"] == True:
                contact1 = cl.getContact(op.param2)
                group = cl.getGroup(op.param1)
                try:
                    arrData = ""
                    text = "%s "%('[提示]\n')
                    arr = []
                    mention = "@Mili "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "退出了 {} 群組 離我們而去了OAO！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 60:
            if op.param1 in jg["JoinGroup"]:
                if op.param2 not in admin:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)
        if op.type == 60:
            if op.param1 not in settings["welcomes"]:
                if op.param1 not in settings['wel']:
                    try:
                        name = str(cl.getGroup(op.param1).name)
                        sendMention(op.param1, "你好 @! 歡迎加入"+name,[op.param2])
                        cl.sendContact(op.param1, op.param2)
                    except Exception as error:
                        print(error)
                try:
                    arrData = ""
                    text = "%s " %('你好~~')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + settings['wel'][op.param1]
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    cl.sendContact(op.param1, op.param2)
                except Exception as error:
                    print(error)
        if op.type == 17:
            if settings["seeJoin"] == True:
                contact1 = cl.getContact(op.param2)
                group = cl.getGroup(op.param1)
                try:
                    arrData = ""
                    text = "%s "%('歡迎')
                    arr = []
                    mention = "@Mili "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "您加入 {} 我們的小窩！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            cl.sendMessage("u33dd24081c8f5cc35309a56b2e2ba3bc","有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            if op.param3 in admin:
                try:
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1,[op.param3])
                except:
                    pass
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('[警告]')
                            arr = []
                            mention1 = "@Mili "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + '踢了 '
                            mention2 = "@Mili "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('[警告]')
                        arr = []
                        mention1 = "@Mili "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + '踢了 '
                        mention2 = "@Mili "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
        if op.type == 24:
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            ulist.append(op.message.id)
        if op.type == 25 and wait["um"]: cl.unsendMessage(op.message.id)
        if op.type == 25 or op.type ==26:
                    msg = op.message
                    if msg.contentType == 1:
                        if msg._from in admin:
                            if wait["lbpic"] == True:
                                pathselfcp = cl.downloadObjectMsg(msg.id)
                                cl.sendMessage(msg.to, "圖片下載完成\n正在更換頭貼(｡･ω･｡)")                         
                                time.sleep(1)
                                cl.updateProfilePicture(pathselfcp)  
                                wait["lbpic"] = False                      
                                cl.sendMessage(msg.to, "更改完成(｡･ω･｡)")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver 
            if sender in admin:
                pass 
            else:
                if msg.to in wait["rapidFire"]:
                    if time.time() - wait["rapidFire"][msg.to] < 2:
                        return
                    else:
                        wait["rapidFire"][msg.to] = time.time()
                else:
                    wait["rapidFire"][msg.to] = time.time()       
            if msg.contentType == 0:
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ 貼圖資料 ]"
                    ret_ += "\n貼圖ID : {}".format(stk_id)
                    ret_ += "\n貼圖包ID : {}".format(pkg_id)
                    ret_ += "\n貼圖網址 : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n貼圖圖片網址：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ 完 ]"
                    cl.sendReplyMessage(msg.id, to, str(ret_))
                    cl.sendImageWithURL(to, path)
            if msg.contentType == 7:
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                number = str(stk_id) + str(pkg_id)
                if sender in settings['limit']:
                    if number in settings['limit'][sender]['stick']:
                        if settings ['limit'][sender]['stick'][number] >= 3:
                            settings ['limit'][sender]['stick']['react'] = False
                        else:
                            settings ['limit'][sender]['stick'][number] += 1
                            settings ['limit'][sender]['stick']['react'] = True
                    else:
                        try:
                            del settings['limit'][sender]['stick']
                        except:
                            pass
                        settings['limit'][sender]['stick'] = {}
                        settings['limit'][sender]['stick'][number] = 1
                        settings['limit'][sender]['stick']['react'] = True
                else:
                    settings['limit'][sender] = {}
                    settings['limit'][sender]['stick'] = {}
                    settings['limit'][sender]['text'] = {}
                    settings['limit'][sender]['stick'][number] = 1
                    settings['limit'][sender]['stick']['react'] = True
                if settings['limit'][sender]['stick']['react'] == False:
                    return
                if to in settings['cc']:
                    command = "貼圖新增回覆:" + format(stk_id) + ":" + format(pkg_id) + ":"
                    command1 = "刪除貼圖回覆:" + format(stk_id) + ":" + format(pkg_id)
                    cl.sendReplyMessage(msg.id, to, command)
                    cl.sendReplyMessage(msg.id, to, command1)
                elif number in settings['sr']:
                    react = settings['sr'][number]
                    cl.sendReplyMention(msg_id, to,"@!" + str(react),[sender])
            if msg.contentType == 16:
                if settings["likeOn"] == True:
                    url = msg.contentMetadata("postEndUrl")
                    cl.likePost(url[25:58], url[66:], likeType=1001)
                    cl.createComment(url[25:58], url[66:],wait['comment'])
                    cl.sendReplyMessage(msg.id, to,"[成功按讚通知]\n我已經成功按讚嘍跟自動發留言咯")
            if msg.contentType == 1:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'pic':
                    image = cl.downloadObjectMsg(msg.id )
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《圖片》\n" + wait['gbc'][sender]['text'] )
                            cl.sendImage(manusia,image)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    cl.deleteFile(image)
                    del wait['gbc'][sender]
            if msg.contentType == 13:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'contact':
                    mid =msg.contentMetadata["mid"]
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《友資》\n" + wait['gbc'][sender]['text'] )
                            cl.sendContact(manusia,mid)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    del wait['gbc'][sender]
            if msg.contentType == 16:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'post':
                    postid =str(msg.contentMetadata['postEndUrl']).split("&postId=")[1]
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《貼文》\n" + wait['gbc'][sender]['text'] )
                            cl.sendPostToTalk(manusia,postid)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    del wait['gbc'][sender]
            if sender in X:
                if text.lower() == 'gc':
                    contact = cl.getContact(sender)
                    cl.sendReplyMention(msg_id, to,"@!\n創作者無限使用",[contact.mid])
            if sender in admin and sender not in X:
                if text.lower() == 'gc':
                    contact = cl.getContact(sender)
                    if sender in ban["user"]:
                        cl.sendMessage(to,"查詢者:"+contact.displayName+"\n票卷數量:{}".format(str(ban["user"][sender].count("gid"))))
                    else:
                        cl.sendMessage(to,"您沒有任何票卷哦~\n要購買復讀機票卷找作者")
                        cl.sendContact(to,"u2db707c088044deb4757c666d1eea1a0")
            if sender not in admin and sender not in X:
                if text.lower() == 'gc':
                    contact = cl.getContact(sender)
                    if sender in ban["user"]:
                        cl.sendMessage(backdoor,"正在查票\n"+contact.displayName+"\nMID:"+contact.mid)
                        cl.sendMessage(to,"查詢者:"+contact.displayName+"\n票卷數量:{}".format(str(ban["user"][sender].count("gid"))))
                    else:
                        cl.sendMessage(to,"您沒有任何票卷哦~\n要購買復讀機票卷找作者")
                        cl.sendContact(to,"u2db707c088044deb4757c666d1eea1a0")
            if sender in X:
				#指令表txt版本
                if text.lower() == '指令':
                        cl.relatedMessage(to, help(),op.message.id)
            if sender in sender:
                if settings["conreply"] == True:
                    if text.lower() in settings['mxer']:
                        cl.sendContact(to,settings['mxer'][text.lower()])
                        time.sleep(5)
            if sender not in admin and sender not in X:
				#指令表txt版本
                if text.lower() == '二級指令':
                        cl.relatedMessage(to, help2(),op.message.id)
            if sender in admin and sender not in X:
				#指令表txt版本
                if text.lower() == '三級指令':
                        cl.relatedMessage(to, help1(),op.message.id)
            if sender in X:             
                if text.lower() =='更換頭貼':
                    cl.sendMessage(to,"請傳送圖片")
                    wait["lbpic"] = True
            if sender in sender:
                if text.lower() == '重啟':
                    if sender in X:
                        ts = time.time()
                        cl.sendReplyMessage(msg.id, to,"重新啟動中")
                        restartBot()
                        cl.sendReplyMessage(msg.id, to,"登入完畢共花了\n{}秒".format(time.time()-ts))
                    else:
                        cl.sendReplyMessage(msg.id, to,"〘警告〙\n系統偵測到您的權限不是創作者,請勿試圖嘗試重啟的動作")
                elif text.lower() == 'ren':
                    eltime = time.time() - mulai
                    bot = "運行時間長達\n" +Runtime(eltime)
                    cl.sendReplyMessage(msg.id, to,bot)
            if sender in admin or sender in X:
                if text.lower() == '貼圖 on':
                    settings['cc'][to] = True
                    cl.sendReplyMessage(msg.id, to, "生成貼圖指令開啟")
                elif text.lower() == '貼圖 off':
                    del settings['cc'][to]
                    cl.sendReplyMessage(msg.id, to, "生成貼圖指令關閉")  
                elif msg.text.lower().startswith("貼圖新增回覆"):
                        list_ = msg.text.split(":")
                        number = str(list_[1]) + str(list_[2])
                        if number not in settings['sr']:
                            try:
                                settings['sr'][number] = list_[3]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendReplyMessage(msg.id, to, "貼圖回覆文字創建中\n已經創建成功嘍！\n" +"被新增的貼圖ID:"+list_[1]+"\n被新增的貼圖包ID:"+list_[2] +"\n貼圖回覆字眼: " + list_[3])
                            except:
                                cl.sendReplyMessage(msg.id, to, "［錯誤］\n" + "新增貼圖關鍵字失敗")
                        else:
                            cl.sendReplyMessage(msg.id, to, "［錯誤］\n" + "貼圖關鍵字已存在")                
                elif msg.text.lower().startswith("刪除貼圖回覆"):
                        list_ = msg.text.split(":")
                        number = str(list_[1]) + str(list_[2])
                        if number in settings['sr']:
                            try:
                                del settings['sr'][number]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendReplyMessage(msg.id, to,  "貼圖回覆文字創建刪除中\n成功刪除貼圖關鍵字!!!\n\n系統貼圖流水號: " + number)
                            except:
                                cl.sendReplyMessage(msg.id, to, "［錯誤］\n刪除貼圖關鍵字失敗!!!")
                        else:
                            cl.sendReplyMessage(msg.id, to, "［錯誤］\n指定刪除的貼圖關鍵字並不在列表中!!!")
            if sender not in admin and sender not in X:
               if text.lower() == '目前權限':
                  contact = cl.getContact(sender)
                  at = backdoor
                  ret_ = "☰☱☲☳〘使用者狀態〙☴☵☶☷\n"
                  ret_ += '使用者名稱 ➤ ' + "@!"+ "\n"
                  ret_ += '使用者職位 ➤ ' + '公開權限\n'
                  ret_ += '使用者限制 ➤ ' + '部分可使用\n'
                  ret_ += '使用者等級 ➤ ' + '最低\n'
                  ret_ += '☰☱☲☳〘查詢完畢〙☴☵☶☷'
                  cl.sendReplyMention(msg_id, to, ret_,[contact.mid])
            if sender in X:
               if text.lower() == '目前權限':
                  contact = cl.getContact(sender)
                  at = backdoor
                  ret_ = "☰☱☲☳〘使用者狀態〙☴☵☶☷\n"
                  ret_ += '使用者名稱 ➤ ' + "@!"+ "\n"
                  ret_ += '使用者職位 ➤ ' + '作者權限\n'
                  ret_ += '使用者限制 ➤ ' + '無限制\n'
                  ret_ += '使用者等級 ➤ ' + '作者指令\n'
                  ret_ += '☰☱☲☳〘查詢完畢〙☴☵☶☷'
                  cl.sendReplyMention(msg_id, to, ret_,[contact.mid])
            if sender in admin and sender not in X:
               if text.lower() == '目前權限':
                  contact = cl.getContact(sender)
                  at = backdoor
                  ret_ = "☰☱☲☳〘使用者狀態〙☴☵☶☷\n"
                  ret_ += '使用者名稱 ➤ ' + "@!"+ "\n"
                  ret_ += '使用者職位 ➤ ' + '管理員權限\n'
                  ret_ += '使用者限制 ➤ ' + '少量\n'
                  ret_ += '使用者等級 ➤ ' + '管理員指令\n'
                  ret_ += '☰☱☲☳〘查詢完畢〙☴☵☶☷'
                  cl.sendReplyMention(msg_id, to, ret_,[contact.mid])
            if sender in sender:
                if settings["rreply"] == True:
                    if text.lower() in settings['mute']:
                        contact = cl.getContact(sender)
                        cl.sendReplyMention(msg_id, to,"@!"+settings['mute'][text.lower()],[contact.mid])
            if sender in admin or sender in X:
                if text.lower().startswith("增加關鍵 "):
                    try:
                        x = text.split(' ')
                        settings['mute'][x[1].lower()] = x[2]
                        contact = cl.getContact(sender)
                        cl.sendReplyMention(msg_id, to,"[新增者]\n@!\n[新增回報]\n關鍵字➤"+x[1]+"\n回覆詞➤"+x[2],[contact.mid])
                    except:
                        cl.sendReplyMessage(msg.id, to,"請勿重複增加同樣的關鍵字")
                elif text.lower().startswith("友資回覆"):
                    x = text.split(' ')
                    settings['mxer'][x[1].lower()] = x[2]
                    cl.sendReplyMessage(msg.id, to,"輸出預覽中" + "\n關鍵字: " +x[1] + "\nMID:" + x[2])
                elif text.lower().startswith("刪除友資回覆"):
                    x = text.split(' ')
                    del settings['mxer'][x[1].lower()]
                    cl.sendReplyMessage(msg.id, to,"刪除成功\n" + "關鍵字: " + x[1] )
                elif text.lower().startswith("刪除關鍵"):
                    try:
                        x = text.split(' ')
                        del settings['mute'][x[1].lower()]
                        cl.sendReplyMessage(msg.id, to,'刪除的關鍵字是:'+'\n'+x[1])
                    except:
                        cl.sendReplyMessage(msg.id, to,'你沒新增這個關鍵詞所以無法刪除哦！')
                elif text.lower() == '清貼圖列表':
                    for x in settings["sr"]:
                        settings["sr"] = {}
                    cl.sendReplyMessage(msg.id, to,"貼圖列表已清空")
                elif text.lower() == '清回覆列表':
                    for x in settings["mute"]:
                        settings["mute"] = {}
                    cl.sendReplyMessage(msg.id, to, "關鍵列表已清空")
                elif text.lower() == '清友資回覆列表':
                    for x in settings["mxer"]:
                        settings["mxer"] = {}
                    cl.sendReplyMessage(msg.id, to, "友資回覆列表已清空")
                
                elif text.lower().startswith("加票 "):
                    x = text.split(" ")
                    if not ismid(x[1]):
                        return
                    if x[1] not in ban["user"]:
                        ban["user"][x[1]] = []
                    if len(x) ==2:
                        t = 1
                    elif len(x) ==3:
                        try:
                            t = int(x[2])
                        except:
                            t = 0
                            cl.relatedMessage(to,"沒有這個mid",op.message.id)
                    ban["user"][x[1]] += ["gid"]*t
                    cl.relatedMessage(to,"成功增加" + str(t) + "張票",op.message.id)
                    json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                elif text.lower().startswith("刪票 "):
                    num = int(text.lower().split(' ')[2])
                    user = str(text.lower().split(' ')[1])
                    if ban["user"][user].count('gid') >= num:
                        for a in range(num):
                            ban["user"][user].remove("gid")
                        cl.relatedMessage(to,"成功移除" + str(num) + "張票",op.message.id)
                    else:
                        cl.relatedMessage(to,"他的票不夠多讓你移除",op.message.id)
                elif text.lower().startswith("rgb "):
                    data = text[4:].lower().split(' ')
                    if len(data) == 2:data.append("0")
                    elif len(data) >3 or len(data) <2:return
                    try:int(data[2])
                    except:return
                    if data[0] == 'text':
                        n = cl.getGroupIdsJoined()
                        g = 0
                        for manusia in n:
                            group = cl.getGroup(manusia)
                            nama =[contact.mid for contact in group.members]
                            if len(nama) >int(data[2]):
                                cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《文字》\n" + data[1])
                                g+=1
                            else:
                                pass
                        cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組\n被廣播的群組名稱:{}".format(str(g),group.name))
                    elif data[0] in ['pic', 'contact', 'post']:
                        wait['gbc'][sender] = {'type':data[0],'text':data[1],'over':data[2]}
                        cl.relatedMessage(to,'請發送你要廣播的東西~',op.message.id)
                elif text.lower() == '清全票':
                    for x in ban["user"]:
                        ban["user"] = {}
                    cl.sendMessage(to, "已清空票卷")
                elif text.lower() == 'res':
                    contact = cl.getContact(sender)
                    backupData()
                    cl.sendReplyMention(msg_id, to,"@!\n儲存設定成功!",[contact.mid])
                elif text.lower() == '全票':
                    user1 = ""
                    for x in ban["user"]:
                        user1 += "【票卷持有者】\n├≽"+cl.getContact(x).displayName+"\n[票卷] {}\n[群組]\n".format(str(ban["user"][x].count("gid")))
                        for y in ban["user"][x]:
                            if y != "gid":
                                try:
                                    user1 += "├≽ "+cl.getGroupWithoutMembers(y).name+"\n"+str(y)+""
                                except:
                                    user1 += "├≽ Can't not relate to that group\n"
                        user1 += "\n─────────\n"
                    cl.sendReplyMessage(msg.id, to,user1+"[完成]") 
                elif msg.text.lower().startswith("addop "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.append(str(inkey))
                    cl.sendMessage(op.message.to, "已獲得管理權限！")
                    backupData()
                elif msg.text.lower().startswith("delop "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.remove(str(inkey))
                    cl.sendMessage(op.message.to, "已取消管理權限！")
                elif msg.text.lower().startswith("cadd "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    X.append(str(inkey))
                    cl.sendMessage(op.message.to, "已獲得作者權限！")
                    backupData()
                elif msg.text.lower().startswith("cdel "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    X.remove(str(inkey))
                    cl.sendMessage(op.message.to, "已取消作者權限！")
                    
                
                elif text.lower() == '關鍵列表':
                    if settings['mute'] == {}:
                        cl.sendMessage(to, "沒有回復列表")
                    else:
                        mc = "[回覆列表]"
                        no = 1
                        for iii in settings['mute']:
                            text = settings['mute']
                            ttxt = settings['mute']["{}".format(iii)]
                            mc += "\n\n"+str(no)+"."+"關鍵字"+":"+"【"+iii+"】"+"回覆詞:"+"【"+str(ttxt)+"】"+"\n"
                            no += 1
                        mc += "\n[總共 {} 個回覆]".format(str(no-1))
                        cl.sendReplyMessage(msg.id,to, str(mc))
                elif text.lower() == '友資列表':
                    if settings['mxer'] == {}:
                        cl.sendMessage(to, "沒有友資回復列表")
                    else:
                        mc = "☰☱☲☳〘友資回覆列表〙☴☵☶☷"
                        no = 1
                        for iii in settings['mxer']:
                            text = settings['mute']
                            ttxt = settings['mxer']["{}".format(iii)]
                            mc += "\n"+str(no)+"."+"友資關鍵字"+":"+"〘"+iii+"〙"+"\n   被回覆友資:"+"〘"+str(ttxt)+"〙"+"\n"
                            no += 1
                        mc += "\n☰☱☲☳〘總共{}個友資回覆〙☴☵☶☷".format(str(no-1))
                        cl.sendReplyMessage(msg.id,to, str(mc))
                elif text.lower() == '貼圖回覆列表':
                    if settings['sr'] == {}:
                        cl.sendMessage(to, "沒有貼圖回覆列表")
                    else:
                        mc = "[貼圖回覆列表]"
                        no = 1
                        for iii in settings['sr']:
                            text = settings['mute']
                            ttxt = settings['sr']["{}".format(iii)]
                            mc += "\n\n"+str(no)+"."+"貼圖流水號"+":"+"【"+iii+"】"+"貼圖回覆語:"+"【"+str(ttxt)+"】"+"\n"
                            no += 1
                        mc += "\n[總共 {} 個貼圖回覆]".format(str(no-1))
                        cl.sendReplyMessage(msg.id,to, str(mc))
            if sender in X:
                if text.lower() == 'caddlist':
                    if X == []:
                        cl.sendMessage(op.message.to,"無擁有權限者!")
                    else:
                        mc = "[作者權限表]"
                        for mi_d in X:
                            mc += "\n➽➤"+cl.getContact(mi_d).displayName
                        cl.sendMessage(op.message.to,mc + "\n[ 結束  ]")
                elif text.lower() == 'oplist':
                    if admin == []:
                        cl.sendMessage(op.message.to,"無擁有權限者!")
                    else:
                        mc = "[管理權限表]"
                        for mi_d in admin:
                            mc += "\n➽➤"+cl.getContact(mi_d).displayName
                        cl.sendMessage(op.message.to,mc + "\n[ 結束  ]")
            if sender in sender:
                if settings["newGame"] == True:
                    if text.lower() == '1a2b':
                        if msg.to not in game["1a2b"]:
                            ans = []
                            while len(ans) != 4:
                                n = random.randrange(0, 10)
                                if not n in ans:
                                    ans.append(n)
                            game["1a2b"][msg.to] = {"answer": ans}
                            cl.sendMessage("u2db707c088044deb4757c666d1eea1a0","1A2B答案 : %s" %ans)
                            contact = cl.getContact(sender)
                            cl.sendReplyMention(msg_id, to, "@!\n1A2B遊戲開始...\n請給我4個相異的數字，並使用!開頭\n例如!1234~",[contact.mid])
                        else:
                            contact = cl.getContact(sender)                             
                            cl.sendReplyMention(msg_id, to, "@!\n遊戲正在進行中...\n請給我4個相異的數字，並使用!開頭\n例如!1234~",[contact.mid])
                    elif text.lower().startswith('12:'):
                        if msg.to not in game["1a2b"]:
                            contact = cl.getContact(sender)
                            cl.sendReplyMention(msg_id, to, "@!\n遊戲尚未開始...\n請輸入 1a2b 來開始遊戲!!",[contact.mid])
                        else:
                            num = text[5:]
                            if check_input(num):
                                number = []
                                for x in num:
                                    number.append(int(x))
                                a, b = check_answer(game["1a2b"][msg.to]["answer"], number)
                                if a == 4:
                                    contact = cl.getContact(sender)
                                    cl.sendReplyMention(msg_id, to, "@!您答對嘍\n4A0B!!恭喜答對~~~",[contact.mid])
                                    del game["1a2b"][msg.to]
                                else:
                                    contact = cl.getContact(sender)
                                    cl.sendReplyMention(msg_id, to, "@!您輸入的是\n數值:%s\n說明:%dA%dB!!再接再厲~~~" % (number, a, b),[contact.mid])
            if sender in sender:
                if text.lower() == 'sp':
                    start = time.time()
                    contact = cl.getContact(sender)
                    elapsed_time = time.time()- start
                    cl.sendReplyMention(msg_id, to,"☰☱☲☳復讀測速☴☵☶☷\n☰☱☲☳測速者為☴☵☶☷\n@!\n☰☱☲☳測速結果☴☵☶☷\n"+ format(str(elapsed_time)) + "秒\n☰☱☲☳☰☱☲☳☴☵☶☷☶",[contact.mid])
                if text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    contact = cl.getContact(sender)
                    cl.sendReplyMention(msg_id, to,'☰☱☲☳〘處理速度〙☴☵☶☷\n@!\n' + str1 + '秒\n☰☱☲☳〘處理完畢〙☴☵☶☷',[contact.mid])
                    elapsed_time = time.time() - start
                    cl.sendReplyMention(msg_id, to,'☰☱☲☳〘反應速度〙☴☵☶☷\n@!\n' + format(str(elapsed_time)) + '秒\n☰☱☲☳〘反應完畢〙☴☵☶☷',[contact.mid]) 
            if sender in sender:
                if msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.relatedMessage(msg.to, str(ret_),op.message.id)
            if sender in admin or sender in X:
                if text.lower().startswith("mc:"):
                        separate = text.split(":")
                        mmid = text.replace(separate[0] + ":","")
                        time.sleep(10)
                        cl.relatedMessage(to,"你已查詢到你要查的mid咯~\n友資MID\n"+mmid+"\n預覽輸出中...需等待十秒生產友資",op.message.id)
                        time.sleep(10)
                        cl.sendContact(to, mmid)
                elif text.lower() == '收':
                    cl.sendReplyMessage(msg.id, to, "總共有" + str(len(ulist)) + "個訊息")
                    start = time.time()                    
                    for x in ulist:
                        cl.unsendMessage(x)
                elif text.lower() == '群組列表':
                    groups = cl.groups
                    ret_ = "[群組列表]"
                    no = 0 + 1
                    for gid in groups:
                        group = cl.getGroup(gid)
                        ret_ += "\n {}. {} | {}\n群組ID:{}".format(str(no), str(group.name), str(len(group.members)),str(group.id))
                        no += 1
                    ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                    cl.relatedMessage(to, str(ret_),op.message.id)
                elif msg.text.lower().startswith('un'): #收回指定數量訊息
                    try:
                        args = text.split(' ')
                        mes = 0
                        try:
                            mes = int(args[1])
                        except:
                            mes = 1
                        M = cl.getRecentMessagesV2(to, 1001)
                        MId = []
                        for ind,i in enumerate(M):
                            if ind == 0:
                                pass
                            else:
                                if i._from == clMID:
                                    MId.append(i.id)
                                    if len(MId) == mes:
                                        break
                        def unsMes(id):
                            cl.unsendMessage(id)
                        for i in MId:
                            thread1 = threading.Thread(target=unsMes, args=(i,))
                            thread1.start()
                            thread1.join()
                    except:
                        pass
            if sender in X:
                if msg.text.lower().startswith('邀請'):
                    x = text.split(' ')
                    cl.sendMessage(to,"接收到權限者使用遠端邀群進入群組")
                    groups = cl.groups
                    targets = []
                    for gid in groups:
                        group = cl.getGroup(gid)
                        targets.append(group.id)
                    c = int(x[1])
                    c = c-1
                    gid = targets[c]
                    group = cl.getGroup(gid)
                    cl.findAndAddContactsByMid(msg._from)
                    cl.inviteIntoGroup(gid,[msg._from])
                    cl.relatedMessage(to, "群組名字:{}".format(str(group.name)),op.message.id)
                    cl.relatedMessage(to, "此群gid:{}".format(str(group.id)),op.message.id)
                elif msg.text.lower().startswith('退出'):
                    x = text.split(' ')
                    groups = cl.groups
                    targets = []
                    for gid in groups:
                        group = cl.getGroup(gid)
                        targets.append(group.id)
                    c = int(x[1])
                    c = c-1
                    gid = targets[c]
                    group = cl.getGroup(gid)
                    cl.leaveGroup(gid)
                    cl.relatedMessage(to, "已退出 {} 群組".format(str(group.name)),op.message.id)
            if sender in X:
                if text.lower() == '狀態':
                    try:
                        cl.kickoutFromGroup(to,["fuck"])
                        cl.inviteIntoGroup(to, ["fuck"])
                    except Exception as e:
                        if e.reason == "request blocked":
                            aa = "無法執行(規制)"
                        else:
                            aa = "可以執行(無規制)"
                            ret_ = "踢人狀態: {}".format(aa)
                            ret_ += "\n邀請狀態: {}".format(aa)
                            ret_ += "\n取消狀態: 可以執行(無規制)"
                            ret_ += "\n版本資訊:復讀3.0"
                            cl.relatedMessage(to, str(ret_),op.message.id)
                    except Exception as e:
                        cl.relatedMessage(msg.to, str(e),op.message.id)
                elif text.lower() == 'bl on':
                    settings["autoAdd"] = False
                    settings["invBlock"] = True
                    cl.sendReplyMessage(msg.id, to, "自動封鎖開啟")
                elif text.lower() == 'bl off':
                    settings["autoAdd"] = True
                    settings["invBlock"] = False
                    cl.sendReplyMessage(msg.id, to, "自動封鎖關閉")
                elif text.lower() == 'raj on':
                    settings["autoJoin"] = True
                    cl.relatedMessage(to, "自動加入群組已開啟 ✔",op.message.id)	
                elif text.lower() == 'raj off':
                    settings["autoJoin"] = False
                    cl.relatedMessage(to, "自動加入群組已關閉 ✘",op.message.id)
                elif text.lower() == 'at on':
                    settings["checkSticker"] = True
                    cl.relatedMessage(to, "貼圖查詢已開啟 ✔",op.message.id)	
                elif text.lower() == 'at off':
                    settings["checkSticker"] = False
                    cl.relatedMessage(to, "貼圖查詢已關閉 ✘",op.message.id)	
				#其餘加好友收回自動已讀
                elif text.lower() == 'rdd on':
                    settings["autoAdd"] = True
                    cl.relatedMessage(to, "自動加入好友已開啟 ✔",op.message.id)	
                elif text.lower() == 'rdd off':
                    settings["autoAdd"] = False
                    cl.relatedMessage(to, "自動加入好友已關閉 ✘",op.message.id)
                elif text.lower() == 'kick on':
                    wait["allbye"] = True
                    cl.relatedMessage(to, "專武踢人開啟",op.message.id)	
                elif text.lower() == 'kick off':
                    wait["allbye"] = False
                    cl.relatedMessage(to, "專武踢人關閉",op.message.id)
                elif text.lower() == 'red on':
                    settings["reread"] = True
                    cl.relatedMessage(to, "查詢收回開啟 ✔",op.message.id)	
                elif text.lower() == 'red off':
                    settings["reread"] = False
                    cl.relatedMessage(to, "查詢收回關閉 ✘",op.message.id)
                elif text.lower() == 'game on':
                    settings["newGame"] = True
                    cl.relatedMessage(to, "遊戲已開啟 ✔",op.message.id)	
                elif text.lower() == 'game off':
                    settings["newGame"] = False
                    cl.relatedMessage(to, "遊戲已關閉 ✘",op.message.id)
                elif text.lower() == '友資 on':
                    settings["conreply"] = True
                    cl.relatedMessage(to, "友資回覆已開啟 ✔",op.message.id)	
                elif text.lower() == '友資 off':
                    settings["conreply"] = False
                    cl.relatedMessage(to, "友資回覆已關閉 ✘",op.message.id)
                elif text.lower() == '關鍵 on':
                    settings["rreply"] = True
                    cl.relatedMessage(to, "關鍵回覆已開啟 ✔",op.message.id)	
                elif text.lower() == '關鍵 off':
                    settings["rreply"] = False
                    cl.relatedMessage(to, "關鍵回覆已關閉 ✘",op.message.id)
                elif text.lower() == 'appt on':
                    settings["autoPtt"] = True
                    cl.relatedMessage(to, "進群自動退出開啟✔",op.message.id)	
                elif text.lower() == 'appt off':
                    settings["autoPtt"] = False
                    cl.relatedMessage(to, "進群自動退出關閉✘",op.message.id)
                elif text.lower() == '全關':
                    settings["text"] = False
                    settings["id"] = False
                    settings["mid"] = False
                    settings["sound"] = False
                    settings["file"] = False
                    settings["image"] = False
                    settings["video"] = False
                    cl.relatedMessage(to,"已關閉",op.message.id)
                elif text.lower() == '全開':
                    settings["text"] = True
                    settings["id"] = True
                    settings["mid"] = True
                    settings["sound"] = True
                    settings["file"] = True
                    settings["image"] = True
                    settings["video"] = True
                    cl.relatedMessage(to,"已開啟",op.message.id)
                elif text.lower() == '收回狀態':
                    bb = "=====防收回狀態=====\n"
                    if settings["text"]: bb += "文字:開啟✔\n"
                    else: bb += "文字:關閉✘\n"
                    if settings["video"]: bb += "影片:開啟✔\n"
                    else: bb += "影片:關閉✘\n"
                    if settings["id"]: bb += "貼圖:開啟✔\n"
                    else: bb += "貼圖:關閉✘\n"
                    if settings["mid"]: bb += "友資:開啟✔\n"
                    else: bb += "友資:關閉✘\n"
                    if settings["sound"]: bb += "語音:開啟✔\n"
                    else: bb += "語音:關閉✘\n"
                    if settings["image"]: bb += "圖片:開啟✔\n"
                    else: bb += "圖片:關閉✘\n"
                    if settings["file"]: bb += "檔案:開啟✔\n"
                    else: bb += "檔案:關閉✘\n"
                    if settings["sendall"]: bb += "公開收回:開啟✔\n"
                    else: bb += "公開收回:關閉✘\n"
                    bb += "=====防收回狀態====="
                    cl.relatedMessage(to,bb,op.message.id)
                elif text.lower() == '公開':
                    if settings["sendall"] == True:
                        settings["sendall"] = False
                        cl.relatedMessage(to,"已關閉",op.message.id)
                    else: settings["sendall"] = True; cl.relatedMessage(to,"已開啟",op.message.id)
                elif text.lower() == '文字':
                    if settings["text"] == True:
                        settings["text"] = False
                        cl.relatedMessage(to,"已關閉",op.message.id)
                    else: settings["text"] = True; cl.relatedMessage(to,"已開啟",op.message.id)
                elif text.lower() == '影片':
                    if settings["video"] == True:
                        settings["video"] = False
                        cl.relatedMessage(to,"已關閉",op.message.id)
                    else: settings["video"] = True; cl.relatedMessage(to,"已開啟",op.message.id)
                elif text.lower() == '貼圖':
                    if settings["id"] == True:
                        settings["id"] = False
                        cl.relatedMessage(to,"已關閉",op.message.id)
                    else: settings["id"] = True; cl.relatedMessage(to,"已開啟",op.message.id)
                elif text.lower() == '友資':
                    if settings["mid"] == True:
                        settings["mid"] = False
                        cl.relatedMessage(to,"已關閉",op.message.id)
                    else: settings["mid"] = True; cl.relatedMessage(to,"已開啟",op.message.id)
                elif text.lower() == '語音':
                    if settings["sound"] == True:
                        settings["sound"] = False
                        cl.relatedMessage(to,"已關閉",op.message.id)
                    else: settings["sound"] = True; cl.relatedMessage(to,"已開啟",op.message.id)
                elif text.lower() == '圖片':
                    if settings["image"] == True:
                        settings["image"] = False
                        cl.relatedMessage(to,"已關閉",op.message.id)
                    else: settings["image"] = True; cl.relatedMessage(to,"已開啟",op.message.id)
                elif text.lower() == '檔案':
                    if settings["file"] == True:
                        settings["file"] = False
                        cl.relatedMessage(to,"已關閉",op.message.id)
                    else: settings["file"] = True; cl.relatedMessage(to,"已開啟",op.message.id)
#============================================================================== 偵測收回
        if op.type == 65:
            at = backdoor
            msg_id = op.param2
            if msg_id in msg_dict:
                if msg_dict[msg_id]["from"] not in bl:
                    if msg_dict[msg_id]["from"] not in red["rereadMID"]:
                        if at not in red["rereadGID"]:
                            if at not in red["reread"]:
                                rereadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(msg_dict[msg_id]["createdTime"]/1000))))
                                newtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                if 'text' in msg_dict[msg_id]:
                                    if settings['text'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回訊息]\n%s\n[發送時間]\n%s\n[收回時間]\n%s'%(msg_dict[msg_id]["text"],rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + txr
                                        cl.sendMessage(at, text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        else:pass
                                        del msg_dict[msg_id]
                                elif 'id' in msg_dict[msg_id]:
                                    if settings['id'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一張貼圖]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        yesno = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/IOS/sticker_animation.png'
                                        ok = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/ANDROID/sticker.png'
                                        cl.sendImageWithURL(at, ok)
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendImageWithURL(msg_dict[msg_id]["wh"], ok)
                                        else:pass
                                        del msg_dict[msg_id]
                                elif 'mid' in msg_dict[msg_id]:
                                    if settings['mid'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一個友資]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendContact(at,msg_dict[msg_id]["mid"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendContact(msg_dict[msg_id]["wh"],msg_dict[msg_id]["mid"])
                                        else:pass
                                        del msg_dict[msg_id]
                                elif 'sound' in msg_dict[msg_id]:
                                    if settings['sound'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一個錄音檔]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendAudio(at, msg_dict[msg_id]["sound"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendAudio(msg_dict[msg_id]["wh"], msg_dict[msg_id]["sound"])
                                        else:pass
                                        del msg_dict[msg_id]
                                elif 'file' in msg_dict[msg_id]:
                                    if settings['file'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一個檔案]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendFile(at, msg_dict[msg_id]["file"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendFile(msg_dict[msg_id]["wh"], msg_dict[msg_id]["file"])
                                        del msg_dict[msg_id]
                                elif 'image' in msg_dict[msg_id]:
                                    if settings['image'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一張圖片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendImage(at, msg_dict[msg_id]["image"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendImage(msg_dict[msg_id]["wh"], msg_dict[msg_id]["image"])
                                        del msg_dict[msg_id]
                                elif 'Video' in msg_dict[msg_id]:
                                    if settings['video'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一部影片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendMessage(at, msg_dict[msg_id]["Video"])
                                        cl.sendVideo(at, msg_dict[msg_id]["Video"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendMessage(msg_dict[msg_id]["wh"], msg_dict[msg_id]["Video"])
                                            cl.sendVideo(msg_dict[msg_id]["wh"], msg_dict[msg_id]["Video"])
                                        else:pass
                                        del msg_dict[msg_id]
                                else:
                                    pass
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    cl.sendReplyMention(msg_id, to,"我在忙，不要吵",[contact.mid])
                                    sendMessageTag("u2db707c088044deb4757c666d1eea1a0", contact.mid)
                                break
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n=>" + Name
                        wait2['ROM'][op.param1][op.param2] = "\n=>" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[★]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
                if op.type == 25:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    if msg.contentType == 1:
                        if wait["group"] == msg.to:
                            if wait["cvp"] == True:
                                while True:
                                    try:
                                        image = cl.downloadObjectMsg(msg_id, saveAs="cvp.jpg")
                                        if os.path.isfile(image):
                                            break
                                    except:
                                        continue
                                cl.sendMessage(msg.to, "圖片下載完成 正在更換頭貼(￣ε￣)")
                                wait["cvp"] = False
                                cl.changeVideoAndPictureProfile('cvp.jpg','test.mp4')
                                os.remove("test.mp4")
                                os.remove("cvp.jpg")
                                cl.sendMessage(msg.to, "影片頭貼已更換完成 ₍₍ ง⍢⃝ว ⁾⁾")
                                wait["group"] = []
                    if msg.contentType == 0:
                            if msg.text.startswith("https://youtu.be/"):
                                search = msg.text.replace("https://youtu.be/","")
                                searchcl = "https://youtu.be/{}".format(search)
                                ytdl(searchcl)
                                cl.sendMessage(msg.to, "影片已下載完成 如需更改原圖像請傳送圖片‎|•'-'•)و✧")
                                wait["cvp"] = True
                                wait["group"] = msg.to    
    except Exception as e:
        logError(e)
def Timer():
    if datadir["switch"] == True:
        time.sleep(30)
        n = 0
        cl.sendMessage(datadir["gid"], "中路專武垢到此一遊")
        for i in [contact for contact in cl.getGroup(datadir["gid"]).members]:
            if n == len(AuthToken):
                n = 0
            if i.mid not in admin:
                threading.Thread(target=kick, args=(n, datadir["gid"], [i.mid],)).start()
                n += 1
        datadir["switch"] = False
        datadir["gid"] = ""
        return
