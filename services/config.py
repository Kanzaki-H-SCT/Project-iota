# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re

class Config(object):
    LINE_HOST_DOMAIN                 = 'https://ga2.line.naver.jp'
    LINE_LEGY_HOST_DOMAIN            = 'https://legy-jp.line.naver.jp'

    LINE_OBS_DOMAIN                  = 'https://obs-jp.line-apps.com'
    LINE_TIMELINE_API                = 'https://ga2.line.naver.jp/mh/api'
    LINE_TIMELINE_MH                 = 'https://ga2.line.naver.jp/mh'
    LINE_LIFF_SEND                   = 'https://api.line.me/message/v3/share'
    LINE_PERMISSION_API              = 'https://access.line.me/dialog/api/permissions'
    LINE_QRCODE_LOGIN_PATH           = 'https://ga2.line.naver.jp/acct/lgn/sq/v1'
    LINE_PERMIT_NOTICE_PATH          = 'https://ga2.line.naver.jp/acct/lp/lgn/sq/v1'

    LINE_LOGIN_QUERY_PATH            = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH             = '/api/v4/TalkService.do'

    LINE_LEGY_RC_DOMAIN              = 'https://legy-rc.line-apps-rc.com'
    LINE_OBS_RC_DOMAIN               = 'https://obs-rc.line-apps.com'
    LINE_OBS_CDN_RC_DOMAIN           = 'https://dl.common.line.naver.jp'

    LINE_LAN_DOMAIN                  = 'https://lan.line.me'
    LINE_LAN_ANDROID_URL             = 'https://lan.line.me/v1/line/android/notification'
    LINE_LAN_IOS_URL                 = 'https://lan.line.me/v1/line/ios/notification'
    LINE_MUSIC_WEBAPP_URL            = 'https://music.line.me/webapp'
    LINE_AMP_LOG_URL                 = 'https://log1-amp.line-apps.com/log'
    LINE_SECONDYARY_REGISTER_API_URL = 'https://w.line.me/lrs/r'
    
    LINE_NOTICE_DOMAIN               = 'https://notice.line.me'
    LINE_STORE_DOMAIN                = 'https://store.line.me'
    LINE_MELODY_DOMAIN               = 'https://melody.line.me'
    LINE_POD_GAME_DOMAIN             = 'https://pod.game.line.me'
    LINE_WEBTOONS_DOMAIN             = 'https://www.webtoons.com'
    LINE_LINEFRIENDS_STORE_DOMAIN    = 'https://store.linefriends.com'
    LINE_SHOP_DOMAIN                 = 'https://shop.line.me'
    LINE_BUY_DOMAIN                  = 'https://buy.line.me'
    LINE_TODAY_DOMAIN                = 'https://today.line.me'
    LINE_TRAVEL_DOMAIN               = 'https://travel.line.me'
    LINE_FACTCHECKER_DOMAIN          = 'https://fact-checker.line.me'
    LINE_MUSIC_DOMAIN                = 'https://music.line.me'
    LINE_LIVE_DOMAIN                 = 'https://live.line.me'
    LINE_MANGA_DOMAIN                = 'https://manga.line.me'

    LINE_API_QUERY_PATH_FIR          = '/S4'
    LINE_POLL_QUERY_PATH_FIR         = '/P4'
    LINE_CALL_QUERY_PATH             = '/V4'
    LINE_LIFF_QUERY_PATH             = '/LIFF1'
    LINE_CERTIFICATE_PATH            = '/Q'
    LINE_CHAN_QUERY_PATH             = '/CH4'
    LINE_SQUARE_QUERY_PATH           = '/SQS1'
    LINE_SHOP_QUERY_PATH             = '/SHOP4'

    LINE_LAN_DOMAIN                      = 'https://lan.line.me'
    LINE_LAN_ANDROID_URL                 = 'https://lan.line.me/v1/line/android/notification'
    LINE_LAN_IOS_URL                     = 'https://lan.line.me/v1/line/ios/notification'
    LINE_MUSIC_WEBAPP_URL                = 'https://music.line.me/webapp'
    LINE_AMP_LOG_URL                     = 'https://log1-amp.line-apps.com/log'
    LINE_SECONDYARY_REGISTER_API_URL     = 'https://w.line.me/lrs/r'

    CHANNEL_ID = {
        #'HELLO_WORLD': 'CT',
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_VERSION = {
        'ANDROID': '12.3.1',
        'IOS': '13.10.0',
        'DESKTOPWIN': '8.1.1',
        'DESKTOPMAC': '8.1.1',
        'IOSIPAD': '13.10.0',
        'CHROMEOS': '3.0.2',
        'DEFAULT': '13.10.0'
    }

    SYSTEM_VERSION = {
        'ANDROID': '10.0',
        'IOS': '13.4.1',
        'DESKTOPWIN': '10.0.0-NT-x64',
        'DESKTOPMAC': '10.15.1',
        'IOSIPAD': '13.4.1',
        'CHROMEOS': '88.0',
        'DEFAULT': '10.0'
    }

    APP_TYPE    = 'DESKTOPWIN'
    APP_VER     = APP_VERSION[APP_TYPE] if APP_TYPE in APP_VERSION else APP_VERSION['DEFAULT']
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'CTCoreTeam LINE CODE:iota'
    SYSTEM_VER  = SYSTEM_VERSION[APP_TYPE] if APP_TYPE in SYSTEM_VERSION else SYSTEM_VERSION['DEFAULT']
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    URL_REGEX   = re.compile(r'^(?:http|ftp)s?://' r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' r'localhost|' r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' r'(?::\d+)?' r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    MID_REGEX   = re.compile(r'u\w{32}')
    GID_REGEX   = re.compile(r'c\w{32}')
    RID_REGEX   = re.compile(r'r\w{32}')
    ALLIDS_REGEX= re.compile(r'(?:u\w{32}|c\w{32}|r\w{32})')

    def __init__(self, appType=None):
        if appType:
            self.APP_TYPE = appType
            self.APP_VER = self.APP_VERSION[self.APP_TYPE] if self.APP_TYPE in self.APP_VERSION else self.APP_VERSION['DEFAULT']
        self.APP_NAME = '%s\t%s\t%s\t%s' % (self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
        self.USER_AGENT = 'Line/%s' % self.APP_VER
