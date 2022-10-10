import hashlib
import requests
import time
import random


def generateSaltSign(text, appVersion):
    '''
    var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
        }
    };
    '''
    t = hashlib.md5(appVersion.encode()).hexdigest()
    r = str(round(time.time()*1000))
    i = r + str(round(10*random.random()))
    sign = hashlib.md5("fanyideskweb{}{}Ygy_4c=r#e#4EX^NUGUc5".format(
        text, i).encode()).hexdigest()
    return {
        'lts': r,
        'bv': t,
        'salt': i,
        'sign': sign,
    }


def getCookie():
    url = "https://fanyi.youdao.com/"
    r = requests.get(url)
    return r.cookies.get_dict()


def translate(text):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }
    cookies = getCookie()
    url = "https://fanyi.youdao.com/translate_o"
    params = {
        "smartresult": "rule"
    }

    '''
        "from": "AUTO",
        "to": "AUTO",
        var t = {
            "中文": "zh-CHS",
            "英语": "en",
            "韩语": "ko",
            "日语": "ja",
            "法语": "fr",
            "俄语": "ru",
            "西班牙语": "es",
            "葡萄牙语": "pt",
            "印地语": "hi",
            "阿拉伯语": "ar",
            "丹麦语": "da",
            "德语": "de",
            "希腊语": "el",
            "芬兰语": "fi",
            "意大利语": "it",
            "马来语": "ms",
            "越南语": "vi",
            "印尼语": "id",
            "荷兰语": "nl",
            "泰语": "th"
        };
    '''

    data = {
        "i": text,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    saltSign = generateSaltSign(
        text, '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36')
    # print(saltSign)
    data.update(saltSign)
    response = requests.post(url, headers=headers,
                             params=params, data=data, cookies=cookies)

    print(response.text)


translate('辣条真好吃。')
