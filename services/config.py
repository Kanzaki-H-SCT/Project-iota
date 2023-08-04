# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re

class Config(object):
    LINE_HOST_DOMAIN                     = 'https://ga2.line.naver.jp'
    LINE_LEGY_HOST_DOMAIN                = 'https://legy-jp.line.naver.jp'

    LINE_OBS_DOMAIN                      = 'https://obs.line-apps.com'
    LINE_OBS_CDN_DOMAIN                  = 'https://obs.line-scdn.net'
    LINE_PROFILE_CDN_DOMAIN              = 'https://profile.line-scdn.net'
    LINE_SHOP_CDN_DOMAIN                 = 'https://shop.line-scdn.net'
    LINE_STICKERSHOP_CDN_DOMAIN          = 'https://stickershop.line-scdn.net'

    LINE_LEGY_BETA_DOMAIN                = 'https://legy-beta.line-apps-beta.com'
    LINE_OBS_BETA_DOMAIN                 = 'https://obs-beta.line-apps.com'
    LINE_OBS_CDN_BETA_DOMAIN             = 'https://cdn-obs-beta.line-apps.com/line'
    LINE_SHOP_DL_BETA_DOMAIN             = 'https://dl.shop.line.beta.naver.jp'
    LINE_STICKERSHOP_DL_BETA_DOMAIN      = 'https://dl.stickershop.line.beta.naver.jp'
    LINE_LAN_BETA_DOMAIN                 = 'https://lan.line-beta.me'
    LINE_NOTICE_CDN_DOMAIN               = 'https://notice.line-beta.me'

    LINE_LEGY_RC_DOMAIN                  = 'https://legy-rc.line-apps-rc.com'
    LINE_OBS_RC_DOMAIN                   = 'https://obs-rc.line-apps.com'
    LINE_OBS_CDN_RC_DOMAIN               = 'https://dl.common.line.naver.jp'

    LINE_NOTICE_DOMAIN                   = 'https://notice.line.me'
    LINE_TV_DOMAIN                       = 'https://tv.line.me'
    LINE_TV2_DOMAIN                      = 'https://www.linetv.tw'
    LINE_STORE_DOMAIN                    = 'https://store.line.me'
    LINE_MELODY_DOMAIN                   = 'https://melody.line.me'
    LINE_POD_GAME_DOMAIN                 = 'https://pod.game.line.me'
    LINE_WEBTOONS_DOMAIN                 = 'https://www.webtoons.com'
    LINE_LINEFRIENDS_STORE_DOMAIN        = 'https://store.linefriends.com'
    LINE_LINEFRIENDS_TW_DOMAIN           = 'https://www.linefriends.com.tw'
    LINE_LINEFRIENDS_JP_DOMAIN           = 'https://www.linefriends.jp'
    LINE_SHOP_DOMAIN                     = 'https://shop.line.me'
    LINE_BUY_DOMAIN                      = 'https://buy.line.me'
    LINE_TODAY_DOMAIN                    = 'https://today.line.me'
    LINE_TRAVEL_DOMAIN                   = 'https://travel.line.me'
    LINE_FACTCHECKER_DOMAIN              = 'https://fact-checker.line.me'
    LINE_MUSIC_DOMAIN                    = 'https://music.line.me'
    LINE_LIVE_DOMAIN                     = 'https://live.line.me'
    LINE_MANGA_DOMAIN                    = 'https://manga.line.me'

    LINE_ENCRYPTION_ENDPOINT             = '/enc'
    LINE_AGE_CHECK_ENDPOINT              = '/ACS4'
    LINE_AUTH_ENDPOINT                   = '/RS3'
    LINE_AUTH_ENDPOINT_V4                = '/RS4'
    LINE_AUTH_EAP_ENDPOINT               = '/ACCT/authfactor/eap/v1'
    LINE_BEACON_ENDPOINT                 = '/BEACON4'
    LINE_BUDDY_ENDPOINT                  = '/BUDDY3'
    LINE_CALL_ENDPOINT                   = '/V3'
    LINE_CANCEL_LONGPOLLING_ENDPOINT     = '/CP4'
    LINE_CHANNEL_ENDPOINT                = '/CH3'
    LINE_CHANNEL_ENDPOINT_V4             = '/CH4'
    LINE_PERSONAL_ENDPOINT_V4             = '/PS4'
    LINE_CHAT_APP_ENDPOINT               = '/CAPP1'
    LINE_COIN_ENDPOINT                   = '/COIN4'
    LINE_COMPACT_E2EE_MESSAGE_ENDPOINT   = '/ECA5'
    LINE_COMPACT_MESSAGE_ENDPOINT        = '/C5'
    LINE_COMPACT_PLAIN_MESSAGE_ENDPOINT  = '/CA5'
    LINE_CONN_INFO_ENDPOINT              = '/R2'
    LINE_EXTERNAL_INTERLOCK_ENDPOINT     = '/EIS4'
    LINE_IOT_ENDPOINT                    = '/IOT1'
    LINE_LIFF_ENDPOINT                   = '/LIFF1'
    LINE_NORMAL_ENDPOINT                 = '/S3'
    LINE_SECONDARY_QR_LOGIN_ENDPOINT     = '/acct/lgn/sq/v1'
    LINE_SHOP_ENDPOINT                   = '/SHOP3'
    LINE_SHOP_AUTH_ENDPOINT              = '/SHOPA'
    LINE_SNS_ADAPTER_ENDPOINT            = '/SA4'
    LINE_SNS_ADAPTER_REGISTRATION_ENDPOINT  = '/api/v4p/sa'
    LINE_SQUARE_ENDPOINT                 = '/SQ1'
    LINE_SQUARE_BOT_ENDPOINT             = '/BP1'
    LINE_UNIFIED_SHOP_ENDPOINT           = '/TSHOP4'
    LINE_WALLET_ENDPOINT                 = '/WALLET4'
    LINE_SECONDARY_PWLESS_LOGIN_ENDPOINT = "/acct/lgn/secpwless/v1"
    LINE_SECONDARY_PWLESS_LOGIN_PERMIT_ENDPOINT = "/acct/lp/lgn/secpwless/v1"
    LINE_SECONDARY_AUTH_FACTOR_PIN_CODE_ENDPOINT = "/acct/authfactor/second/pincode/v1"
    LINE_PWLESS_CREDENTIAL_MANAGEMENT_ENDPOINT = "/acct/authfactor/pwless/manage/v1"
    LINE_PWLESS_PRIMARY_REGISTRATION_ENDPOINT = "/ACCT/authfactor/pwless/v1"
    LINE_VOIP_GROUP_CALL_YOUTUBE_ENDPOINT = "/EXT/groupcall/youtube-api"
    LINE_E2EE_KEY_BACKUP_ENDPOINT = "/EKBS4"
    SECONDARY_DEVICE_LOGIN_VERIFY_PIN_WITH_E2EE = "/LF1"
    SECONDARY_DEVICE_LOGIN_VERIFY_PIN = "/Q"
    LINE_NOTIFY_SLEEP_ENDPOINT  = "/F4"

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
